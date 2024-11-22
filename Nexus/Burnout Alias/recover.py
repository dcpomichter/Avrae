embed <drac2>
cc="Burnout"
desc= "If you are a spellcaster, take a d12 for full caster, d10 for half caster or d8 for third caster—this is your Burnout die. If you are multiclassed, use the maximum burnout die of whichever caster class you have the most levels in. In the case of a tie, use the largest.\n\nWhenever you attempt to cast a magic spell, roll the Burnout die. On a 1 or 2, the power is overwhelming and you trigger a burnout event"
subclasses=get("subclass", "")
class_list=[('Wizard', 0), ('Sorcerer', 0), ('Bard', 0), ('Cleric', 0), ('Druid', 0), ('Paladin', 1), ('Ranger', 1), ('Artificer', 1), ('Warlock', 0)]
if "Eldritch Knight" in subclasses:
  class_list.append(("Fighter", 2))
if "Arcane Trickster" in subclasses:
  class_list.append(("Rogue", 2))
highest, value=max(class_list, key=lambda x:(character().levels.get(x[0]), 2-x[1]))
character().create_cc_nx(cc, 0, 4, 'long', 'hex', value, desc=desc, initial_value=value)
burnout=character().get_cc(cc)
ch=character()
HD_types=[x.name for x in ch.consumables if 'Hit Dice' in x.name]
HD_output='\n'.join(f"{x}: {character().cc_str(x)}" for x in HD_types)
output=f''' -f "Hit Dice| No hit dice available!" '''
dice=['d6','d8','d10','d12']
text=f''' -title "{name} tries to cool down and rest." -f "Burnout| {character().cc_str(cc)}" {output} '''
if burnout>value:
    for hd in HD_types:
        if ch.cc_exists(hd) and ch.get_cc(hd):
            ch.mod_cc(hd, -1)
            output=f''' -f "{hd}|{ch.cc_str(hd)} (-1)" '''
            character().mod_cc("Burnout", -1)
            text=f''' -title "{name} cools down and rests." -f "Burnout| {character().cc_str("Burnout")} (-1)" {output} -f "Effect| You can spend a hit die during a short rest to grow your burnout die by one step. You don't gain any healing from hit die spent in this way." '''
            break
else:
    text=f''' -title "{name} tries to cool down and rest." -f "Burnout| {character().cc_str("Burnout")}" -f "Hit Dice| {HD_output}" -f "Effect| You cannot grow your Burnout Die beyond your maximum" '''
return text
</drac2> -thumb {{image}}
