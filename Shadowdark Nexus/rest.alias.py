embed <drac2>

parsed = argparse(&ARGS&)
arguments = &ARGS&
n = '\n'
ch = character()
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
myBags=bag.load_bags()
secondBags=bag.save_state(myBags)
classes    = load_json(get_gvar("938be0a3-f225-4c1f-a8e5-51643299c43e"))

def merge_dicts(dict1, dict2):
  for class_name, details in dict2.items():
    if class_name in dict1:
      dict1[class_name]["hit_die"] = details.get("hit_die", dict1[class_name]["hit_die"])
    else:
      dict1[class_name] = details
  return dict1

server_classes = load_json(get_svar('class_info', '{}'))
classes = merge_dicts(classes, server_classes)

uvar_classes = load_json(get_uvar('class_info', '{}'))
classes = merge_dicts(classes, uvar_classes)

cvar_classes = load_json(get('class_info', '{}'))
classes = merge_dicts(classes, cvar_classes)

hit_dice = {}

for cls in ch.get_cvar('class', None):
  if cls:
    cls_info = classes.get(cls, {})
    size = cls_info.get("hit_die", 0)
    if size:
        if not hit_dice.get(size):
            hit_dice[size] = {'str': ""}
        hit_dice[size]['str'] += f"+{cls}"

for size, num in hit_dice.items():
  cc_name = f"Hit Dice (d{size})"
  cc = ch.create_cc_nx(cc_name, minVal=0, reset=None)

sb = ch.spellbook
compact = parsed.last('h',parsed.last('compact',False))
counters = ch.consumables
counterNames = [x.name for x in counters]

rations=''
total=parsed.last('n', 1, int)
if not parsed.last('i'):
    rations_bag=bag.find_bag_with_item(secondBags, item="Ration")
    if rations_bag:
        if rations_bag[0]=="Storage":
            bag.swap_pos(secondBags, bag_name="Storage", position=9)
            rations_bag=bag.find_bag_with_item(secondBags, item="Ration")
    rationed_bag=bag.find_bag_with_item(myBags, item="Ration")
    if rationed_bag:
        if rationed_bag[0]=="Storage":
            bag.swap_pos(myBags, bag_name="Storage", position=9)
            rationed_bag=bag.find_bag_with_item(myBags, item="Ration")
    if rations_bag and rations_bag[0]!="Storage":
        for item_type, amount in rations_bag[1].items():
            if "Ration" in item_type:
                rationed_bag, *_=bag.modify_item(myBags, item="Ration",quantity=-total,create_on_fail=False,recursive_search=True)
                remaining=amount-total
                item=item_type
    bag.save_bags(myBags)
    if rationed_bag and rationed_bag[0]!="Storage":
        rations=f''' -f "{rationed_bag[0]}|{remaining} {item} (-{total})" '''

if rations!='' or parsed.last('i'):
    outText = f'-title "{name} takes a Rest!" '
    sleptInArmor = parsed.last('armor',False)
    hpGain = hp-character().hp
    tempHP = character().temp_hp
    character().set_hp(hp)
    character().set_temp_hp(0)
    outText += ', Hit Points' if compact else f''' -f "Hit Points|{character().hp_str()}{f' ({hpGain:+})' if hpGain else ''}|inline" '''
    if ch.cc_exists('Exhaustion'):
        if ch.get_cc('Exhaustion') and not sleptInArmor and not parsed.last('i'):
            exhaustionDecreased = True
            ch.mod_cc('Exhaustion',-1)
        outText += ', Exhaustion Level' if compact else f''' -f "Exhaustion|{ch.cc_str('Exhaustion')}{' (-1)' if get('exhaustionDecreased') else ''}|inline" '''

    countersToResetO = {counter.name + (f" {not counterNames.pop(counterNames.index(counter.name)) or i-1}" if (i := counterNames.count(counter.name))>1 else ""):{"reset_to":counter.reset_to,"reset_by":counter.reset_by, "cc": counter} for counter in counters if counter.reset_on and counter.reset_on in 'shortlong' and counter.name.lower() not in ('exhaustion', 'short rest tokens', 'travel tokens')}
    if countersToResetO:
        countersToResetList = list(countersToResetO)
        countersToResetList.sort()
        countersToReset = {}
        countersToReset.update({x:countersToResetO[x] for x in countersToResetList})
        counterFields = ['' for i in range(20)]
        counterField = 0
        for counter in countersToReset:
            if delta := countersToReset[counter].reset_by:
                if ('-' in delta and countersToReset[counter].cc.value == countersToReset[counter].cc.min) or (not '-' in delta and countersToReset[counter].cc.value == countersToReset[counter].cc.max):
                    delta = ''
                else:
                    delta = vroll(countersToReset[counter].reset_by)
                    countersToReset[counter].cc.set(countersToReset[counter].cc.value+delta.total)
                    delta = f' ({delta})'
                    if 'd' in delta:
                        delta = delta.replace(' `',' `+') if not '-' in delta[:-6] else delta
                    else:
                        delta = delta[:delta.index('=')-1]+')'
            elif countersToReset[counter].reset_to is not None and (delta := countersToReset[counter].reset_to-countersToReset[counter].cc.value):
                countersToReset[counter].cc.set(countersToReset[counter].cc.value+delta)
                delta = f' ({delta:+})'
            elif countersToReset[counter].reset_to is None and (delta := countersToReset[counter].cc.max-countersToReset[counter].cc.value):
                countersToReset[counter].cc.set(countersToReset[counter].cc.value+delta)
                delta = f' ({delta:+})'
            counterText = countersToReset[counter].cc.name+(f'{delta if delta else ""}, ' if compact else f''': {countersToReset[counter].cc}{delta if delta else ""}{n}''')
            counterField += 1 if len(counterFields[counterField]+counterText)>1020 else 0
            counterFields[counterField] += counterText
        counterFields = [field.strip(', ') for field in counterFields if field]
        outText += ', ' if compact else f''' -f "Reset Counters|{''.join(counterFields)}"'''
    outText+=rations
else:
    outText = f'-title "{name} cannot takes a Rest!" -f "Resting|To rest, a character must consume a ration and sleep for 8 hours."'

return outText+f' -thumb {image} -color {color} -footer "{name}: <{character().hp_str()}>"'
</drac2>
