embed <drac2>
parsed = argparse(&ARGS&)
arguments = &ARGS&
mode = 'help'
n = '\n'
ch = character()
sb = ch.spellbook
compact = parsed.last('h',parsed.last('compact',False))

classes    = load_json(get_gvar("a53f12b4-bd1d-40d7-844f-9403a7dc5246"))
subclasses = load_json(get("subclass", "{}"))

def merge_dicts(dict1, dict2):
    for class_name, details in dict2.items():
        if class_name in dict1:
            dict1[class_name]["sub_level"] = details.get("sub_level", dict1[class_name]["sub_level"])
            dict1[class_name]["hit_die"] = details.get("hit_die", dict1[class_name]["hit_die"])
            dict1[class_name]["subclasses"].extend(details.get("subclasses", []))
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

for (cls, lvl) in ch.levels:
  cls_info = classes.get(cls, {})
  sub = subclasses.get(f"{cls}Level")
  size = cls_info.get("hit_die", 0)
  if size:
    if not hit_dice.get(size):
      hit_dice[size] = {'str': "", 'int': 0}
    hit_dice[size]['str'] += f"+{cls}Level"
    hit_dice[size]['int'] += lvl

for size, num in hit_dice.items():
  cc_name = f"Hit Dice (d{size})"
  cc = ch.create_cc_nx(cc_name, minVal=0, maxVal=num.int, reset=None)
  if ch.get_cc_max(cc_name) != num.int:
    ch.edit_cc(cc_name, maxVal=num.int)

counters = ch.consumables
counterNames = [x.name for x in counters]
hitDice = [f"d{x}" for x in range(20,0,-1)]

Bardness = int(get('BardLevel',1))-1
Warlockness = int(get('WarlockLevel',0))
yourRace = get("race",ch.race)
Verdan = "ro<3" if yourRace.lower()=='verdan' else ""
spentDice = []
maxed = parsed.last('max',False)
durable = 'durable' in get('feats','').lower() or parsed.last('durable',parsed.last('dur',False))
periapt = 'periapt of wound closure' in get('attunedItems','').lower() or parsed.last('periapt',parsed.last('closure',False))
ownedHitDice = []
for hd in hitDice:
  if (hitdie := f"Hit Dice ({hd})") in counterNames:
    ownedHitDice.append(hitdie)
    if '-b' in arguments:
      arguments = arguments[:arguments.index('-b')]
    for arg in arguments:
      if 'd' in arg and hd == arg[arg.index('d'):]: # and arguments[arguments.index(arg)-1] != '-b': # not arg in parsed.get('b'):
        spentDice.append({"size":hd,"counter":f"Hit Dice ({hd})","numberSpent":min(int(arg.split('d')[0] if arg.split('d')[0] else arguments[arguments.index(arg)-1] if arguments.index(arg) and arguments[arguments.index(arg)-1].isdigit() else 1),ch.get_cc(f"Hit Dice ({hd})"))})
if arguments and (arguments[0].isdigit()) and ownedHitDice and not spentDice:
  totalDice =  int(arguments[0])
  defaulthd = f"Hit Dice ({get('defaultHD',ownedHitDice[0][ownedHitDice[0].index('d'):-1])})"
  hitDieList = [defaulthd]+[die for die in ownedHitDice if die!=defaulthd]
  for hitdie in hitDieList:
    if totalDice <= 0:
      break
    if ch.cc_exists(hitdie) and ch.get_cc(hitdie):
      hd = hitdie[hitdie.index('d'):-1]
      spentDice.append({"size":hd,"counter":hitdie,"numberSpent":min(totalDice,ch.get_cc(hitdie))})
      totalDice -= ch.get_cc(hitdie)
spentDiceString = (', ' if len(spentDice)!=2 else ' and ').join([f"{'and ' if len(spentDice)>2 and spentDice[spentDice.index(die)]==spentDice[-1] else ''}{die.numberSpent} {die.size}" for die in spentDice]) or 0
hdRolls = [vroll(f"{die.numberSpent}{die.size.replace('d','*' if maxed else 'd')}{Verdan}{f'mi{max(2,constitutionMod*2)}[durable]' if durable else ''}{'*2[Periapt of Wound Closure]' if periapt else ''}+({die.numberSpent} [dice spent]*{constitutionMod} [constitution mod])") for die in spentDice]
for die in spentDice:
  ch.mod_cc(die.counter,-die.numberSpent)
hpGain = sum([Roll.total for Roll in hdRolls])
bonus = ([f"1d{2*(3+(Bardness>7)+(Bardness>11)+(Bardness>15))}[Song of Rest]"] if Bardness and spentDiceString else [])+parsed.get('b') if hpGain else []
bonusText = f', along with {(", " if len(bonus)!=2 else " and ").join([("and " if len(bonus)>2 and bonus[bonus.index(value)]==bonus[-1] else "")+value[:value.index("[") if "[" in value else None] for value in bonus])} bonus healing' if bonus else ''
bonusRolls = [vroll(value) for value in bonus]
hpGain += sum([Roll.total for Roll in bonusRolls])
ch.modify_hp(hpGain,0,0)
outText = (f' -title "{name} takes a Short Rest!"')+(f' -desc "{name} spends {spentDiceString} hit di{"c" if sum([die.numberSpent for die in spentDice])!=1 else ""}e{bonusText}, recovering a total of {hpGain} hit points."')
outText += f' -f "Healing|{n.join([str(Roll) for Roll in hdRolls])}|inline"' if hpGain else ''
outText += f' -f "Bonus Healing|{n.join([str(Roll) for Roll in bonusRolls])}|inline"' if bonus else ''

countersToResetO = {counter.name:{"reset_to":counter.reset_to,"reset_by":counter.reset_by, "cc": counter} for counter in counters if counter.reset_on and counter.reset_on in 'short'}
if countersToResetO:
  countersToResetList = list(countersToResetO)
  countersToResetList.sort()
  countersToReset = {}
  countersToReset.update({x:countersToResetO[x] for x in countersToResetList})
  counterFields = ['' for i in range(20)]
  counterField = 0
  for counter in countersToReset:
    if delta := countersToReset[counter].reset_by:
      if ('-' in delta and ch.get_cc(counter) == ch.get_cc_min(counter)) or (not '-' in delta and ch.get_cc(counter) == ch.get_cc_max(counter)):
        delta = ''
      else:
        delta = vroll(countersToReset[counter].reset_by)
        ch.mod_cc(counter,delta.total)
        delta = f' ({delta})'
        if 'd' in delta:
          delta = delta.replace(' `',' `+') if not '-' in delta[:-6] else delta
        else:
          delta = delta[:delta.index('=')-1]+')'
    elif countersToReset[counter].reset_to is not None and (delta := countersToReset[counter].reset_to-ch.get_cc(counter)):
      ch.mod_cc(counter,delta)
      delta = f' ({delta:+})'
    elif countersToReset[counter].reset_to is None and (delta := ch.get_cc_max(counter)-ch.get_cc(counter)):
      ch.mod_cc(counter,delta)
      delta = f' ({delta:+})'
    counterText = counter+f'{delta if delta else ""}, '
    counterText = countersToReset[counter].cc.name+(f'{delta if delta else ""}, ' if compact else f''': {countersToReset[counter].cc}{delta if delta else ""}{n}''')
    counterField += 1 if len(counterFields[counterField]+counterText)>1020 else 0
    counterFields[counterField] += counterText
  counterFields = [field.strip(', ') for field in counterFields if field]
  outText += ' -f "Reset Counters|'+'" -f "Continued|'.join(counterFields)+'"'
if Warlockness:
  W = int(WarlockLevel)
  slotLevel = min(ceil(W/2),5)
  totalSlots = sb.get_max_slots(slotLevel)
  pactSlots = (W>0)+(W>1)+(W>10)+(W>16)
  standardSlots = totalSlots - pactSlots
  if standardSlots:
    ch.set_cvar('ssSpent', max(0,standardSlots - sb.get_slots(slotLevel),int(get('ssSpent',0))))
  delta = min(sb.get_max_slots(slotLevel)-sb.get_slots(slotLevel)-int(get('ssSpent',0)),pactSlots)
  sb.set_slots(slotLevel,min(delta+sb.get_slots(slotLevel),sb.get_max_slots(slotLevel)))
  outText += f' -f "Spell Slots|{sb.slots_str(slotLevel)}{f" ({delta:+})" if delta else ""}"'
hitDieText = ''
for hitdie in ownedHitDice:
  delta = 0
  for dice in spentDice:
    if hitdie==dice.counter:
      delta = f" (-{dice.numberSpent})"
  hitDieText += f'**{hitdie[hitdie.index("d"):-1]}**: {character().cc_str(hitdie)}{delta if delta else ""}{n}'
outText += f' -f "Hit Dice|{hitDieText}"' if ownedHitDice else ''
outText += f' -f "{yourRace} Regeneration|{ch.cc_str("Regeneration")}|inline"' if get('regenValid') else ''
return outText+ f''' -thumb {image} -color {color} -footer "{name}: <{character().hp_str()}>" '''
</drac2>
