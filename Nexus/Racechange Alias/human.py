embed <drac2>
human=character().get_cvar('race')
if "Human" in human:
    cc="Human Determination"
    desc="You are filled with determination. If you fail an attack roll, ability check, or saving throw, you can reroll one d20. You must keep the new result.\n\nAfter you use Human Determination, you can't use it again until you complete a short or long rest."
    character().create_cc_nx(cc,0,1,'short','hex',1,desc=desc)
    text=f''' -title "{name} is a stubborn Human" -f "{cc}|{character().cc_str(cc)}" -f "{desc}" -thumb {image}'''
else:
    text=f''' -title "{name}, no one is quite as stubborn as a Human" -f "Race| {human}" -thumb {image}'''
return text
</drac2>
