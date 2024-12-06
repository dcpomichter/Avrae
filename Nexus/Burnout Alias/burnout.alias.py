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
dice=[12, 10, 8, 6, 4][character().get_cc(cc)]
stress={
'minor':['1','1 Notch', '1'],
'moderate':['1d4','2 Notches', '2'],
'major':['1d6','4 Notches', '4'],
'monstrous':['1d6+4','8 Notches', '6']
}
text=f''' -title "{name} checks on their Burnout." -f "{cc}|{character().cc_str(cc)}" -f "Burnout Die| {f'1d{dice}'}"'''
if "&1&".lower() in stress or "&1&".lower()=="cantrip":
    burnout=vroll(f'1d{dice}')
    if burnout.total>=3:
        text=f''' -title "{name} is safe from Burnout, for now!" -f "Burnout|{burnout}" -f "{cc}|{character().cc_str(cc)}" '''
    elif "&1&".lower()=="cantrip" and burnout.total<=2:
        character().mod_cc(cc, +1)
        text=f''' -title "{name} suffers from Burnout!" -f "Burnout|{burnout}" -f "Effect|Your Burnout die gets smaller. Each time you suffer burnout the die becomes one size smaller." -f "{cc}|{character().cc_str(cc)+' (+1)'}"'''
    elif "&1&".lower() in stress and burnout.total<=2:
        character().mod_cc(cc, +1)
        consequence=vroll('1d100')
        stressed=vroll(stress["&1&".lower()][0])
        if consequence.total<=45:
            character().mod_cc('Stress', stressed.total)
            text=f''' -title "{name} suffers from Burnout!" -f "Burnout|{burnout}" -f "Consequences|{consequence}" -f "Effect|Your Burnout die gets smaller. Each time you suffer burnout the die becomes one size smaller." -f "{cc}|{character().cc_str(cc)+' (+1)'}" -f "Stress|{character().cc_str('Stress')+f' (+{stressed.total})' if character().cc_exists('Stress') else '**No Counter**'}" '''
        elif consequence.total<=70:
            text=f''' -title "{name} suffers from Burnout!" -f "Burnout|{burnout}" -f "Consequences|{consequence}" -f "Effect|Your Burnout die gets smaller. Each time you suffer burnout the die becomes one size smaller." -f "{cc}|{character().cc_str(cc)+' (+1)'}" -f "Effect|An Item gains {stress["&1&".lower()][1]}" '''
        elif consequence.total<=80:
            character().mod_cc('Hunger', +int(stress["&1&".lower()][2]))
            text=f''' -title "{name} suffers from Burnout!" -f "Burnout|{burnout}" -f "Consequences|{consequence}" -f "Effect|Your Burnout die gets smaller. Each time you suffer burnout the die becomes one size smaller." -f "{cc}|{character().cc_str(cc)+' (+1)'}" -f " Hunger|{character().cc_str('Hunger')+f' (+{stress["&1&".lower()][2]})' if character().cc_exists('Hunger') else '**No Counter**'}" '''
        elif consequence.total<=90:
            character().mod_cc('Thirst', +int(stress["&1&".lower()][2]))
            text=f''' -title "{name} suffers from Burnout!" -f "Burnout|{burnout}" -f "Consequences|{consequence}" -f "Effect|Your Burnout die gets smaller. Each time you suffer burnout the die becomes one size smaller." -f "{cc}|{character().cc_str(cc)+' (+1)'}" -f " Thirst|{character().cc_str('Thirst')+f' (+{stress["&1&".lower()][2]})' if character().cc_exists('Thirst') else '**No Counter**'}" '''
        else:
            character().mod_cc('Fatigue', +int(stress["&1&".lower()][2]))
            text=f''' -title "{name} suffers from Burnout!" -f "Burnout|{burnout}" -f "Consequences|{consequence}" -f "Effect|Your Burnout die gets smaller. Each time you suffer burnout the die becomes one size smaller." -f "{cc}|{character().cc_str(cc)+' (+1)'}" -f " Fatigue|{character().cc_str('Fatigue')+f' (+{stress["&1&".lower()][2]})' if character().cc_exists('Fatigue') else '**No Counter**'}" '''
return text
</drac2>  -thumb https://media.discordapp.net/attachments/879551881557454859/1126890054443352065/tumblr_oqm9y2nSQm1qgm6fno1_1280.png
