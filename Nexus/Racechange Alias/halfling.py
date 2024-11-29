embed <drac2>
halfling=character().get_cvar('race')
if "Halfling" in halfling:
    cc="Lucky"
    desc="When you roll a natural 1 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll.\n\nAfter you use Lucky, you can't use it again until you either (a) complete a short or long rest or (b) you roll a natural 20 on an attack roll, ability check, or saving throw."
    character().create_cc_nx(cc,0,1,'short','hex',1,desc=desc)
    text=f''' -title "{name} is as Lucky as a Halfling" -f "{cc}|{character().cc_str(cc)}" -f "{desc}" -thumb {image}'''
else:
    text=f''' -title "{name}, no one is quite as lucky as a Halfling" -f "Race| {halfling}" -thumb {image}'''
return text
</drac2>
