embed <drac2>
cc="Death Saves"
desc="While you are dying, you must make a death saving throw at the start of your turn to see how long you can cling onto life—if you fail three death saving throws, you die.\n\nWhen you make a death saving throw, roll a d20 and check the Death Saving Throw table below to see what happens to you.\n\n**1:** You fail two death saving throws.\n**2-9:** You fail one death saving throw.\n**10-19:** No change.\n**20:** You regain 1 hit point and the dying condition ends.\n\n*Persistent Saves*\nDeath saving throws don't reset after a short rest—instead, you recover one failed death saving throw after completing a long rest. Take care to rest properly."
character().create_cc_nx(cc, 0, 3, 'long', 'star', reset_by=-1, desc=desc, initial_value=0)
a=argparse(&ARGS&)
if "adv" in a:
    death=vroll('2d20kh1')
elif "dis" in a:
    death=vroll('2d20kl1')
else:
    death=vroll('1d20')
if death.total==1:
    character().mod_cc(cc, +2)
    text=f''' -title "{name} rolls a Death saving throw!" -f "{death} **Critical Failure**" -f "{cc}| {character().cc_str(cc)+' (+2)'}" -f "**You are Dead**"''' if character().get_cc(cc)==3 else f''' -title "{name} rolls a Death saving throw!" -f "{death} **Critical Failure**" -f "{cc}| {character().cc_str(cc)+' (+2)'}" '''
elif death.total<=9:
    character().mod_cc(cc, +1)
    text=f''' -title "{name} rolls a Death saving throw!" -f "{death} **Failure**" -f "{cc}| {character().cc_str(cc)+' (+1)'}" -f "**You are Dead**" ''' if character().get_cc(cc)==3 else f''' -title "{name} rolls a Death saving throw!" -f "{death} **Failure**" -f "{cc}| {character().cc_str(cc)+' (+1)'}" '''
elif death.total==20:
    character().set_hp(1)
    text=f''' -title "{name} rolls a Death saving throw!" -f "{death} **Success**" -f "{cc}| {character().cc_str(cc)}" -f "Hit Points| {character().hp_str()}" '''
else:
    text=f''' -title "{name} rolls a Death saving throw!" -f "{death}" -f "{cc}| {character().cc_str(cc)}" '''
return text
</drac2> -thumb {{image}}
