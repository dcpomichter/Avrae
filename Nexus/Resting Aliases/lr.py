embed <drac2>

parsed = argparse(&ARGS&)
arguments = &ARGS&
n = '\n'
ch = character()

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

sb = ch.spellbook
compact = parsed.last('h',parsed.last('compact',False))
counters = ch.consumables
counterNames = [x.name for x in counters]
hitDice = [f"d{x}" for x in range(20,0,-1)]


outText = f'-title "{name} takes a Long Rest!" -desc "Reset Death Saves'
sleptInArmor = parsed.last('armor',False)
hpGain = hp-character().hp
tempHP = character().temp_hp
character().set_hp(hp)
character().set_temp_hp(0)
outText += ', Hit Points' if compact else f'''" -f "Hit Points|{character().hp_str()}{f' ({hpGain:+})' if hpGain else ''}|inline"'''
hitDieRate = int(max(1,level/(4 if sleptInArmor else 2)))+sum([int(b) for b in parsed.get('b')])
hitDieText = ''
for hd in hitDice:
 if (hitdie := f"Hit Dice ({hd})") in counterNames:
  hasHitDice = True
  if (delta :=  min(hitDieRate,ch.get_cc_max(hitdie)-ch.get_cc(hitdie))) and hitDieRate:
   hitDieRate -= delta
   ch.mod_cc(hitdie,delta)
   delta = f' ({delta:+})'
  hitDieText += f'**{hd}**: {ch.cc_str(hitdie)}{delta if delta else ""}{n}'
  delta = 0
outText += (', Hit Dice' if compact else f' -f "Hit Dice|{hitDieText}|inline"') if get('hasHitDice') else ''
if ch.cc_exists('Exhaustion'):
 pandemonium_channels = (904307969414553670, 907489560534073354, 907489639449915422, 907489704671326208, 907489748845752370)
 if ch.get_cc('Exhaustion') and not sleptInArmor and not ctx.channel.id in pandemonium_channels and not parsed.last('i'):
  exhaustionDecreased = True
  ch.mod_cc('Exhaustion',-1)
 outText += ', Exhaustion Level' if compact else f''' -f "Exhaustion|{ch.cc_str('Exhaustion')}{' (-1)' if get('exhaustionDecreased') else ''}|inline"'''
if sum([sb.get_max_slots(slotLevel) for slotLevel in range(1,10)]):
 if exists('ssSpent'):
  ch.delete_cvar('ssSpent')
 spellSlotText = ''
 for slotLevel in range(1,10):
  if sb.get_max_slots(slotLevel):
   if delta := sb.get_max_slots(slotLevel)-sb.get_slots(slotLevel):
    delta = f' ({delta:+})'
   sb.set_slots(slotLevel,sb.get_max_slots(slotLevel))
   spellSlotText += character().spellbook.slots_str(slotLevel)+(delta if delta else '')+n
 outText += ', Spell Slots' if compact else f' -f "Spell Slots|{spellSlotText}|inline"'

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
 outText += (', ' if compact else ' -f "Reset Counters|')+'" -f "Continued|'.join(counterFields)+'"'

return outText+f' -thumb {image} -color {color} -footer "{name}: <{character().hp_str()}>"'
</drac2>
