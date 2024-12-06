embed <drac2>
fighter=character().levels.get('Fighter')
if fighter>=1:
    dice=1 if fighter<=2 else 2 if fighter<=6 else 3 if fighter<=9 else 4 if fighter<=14 else 5 if fighter<=17 else 6
    wind=character().get_cc('Second Wind')
    if wind>=1:
        heal=vroll(f'{dice}d10+{fighter}')
        character().modify_hp(heal.total, overflow=False)
        character().mod_cc('Second Wind', -1)
        text=f''' -title "{name} uses their Second Wind!" -f "Healing|{heal}" -f "{character().hp_str()} (+{heal.total})" -f "Second Wind| {character().cc_str('Second Wind')} (-1)" '''
    else:
        text=f''' -title "{name} tries to use their Second Wind" -f "Second Wind|{character().cc_str('Second Wind')}" -f "{character().hp_str()}" '''
else:
    text=f''' -title "{name} needs to learn a lesson or two." -f "You are not a Fighter| Only Fighters can use Second Wind"'''
return text
</drac2> -thumb {{image}}
