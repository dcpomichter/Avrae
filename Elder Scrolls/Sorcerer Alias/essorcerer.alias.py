embed <drac2>
ch=character()
sorcerer=ch.levels.get('Sorcerer')
magicka=''
bonMagicka=''
magic=ch.cc_exists('Magicka')
bonus=ch.cc_exists('Bonus Sorcery Magicka')
false=''
sorcMagicka=4 if sorcerer==1 else 6 if sorcerer==2 else 14 if sorcerer==3 else 17 if sorcerer==4 else 27 if sorcerer==5 else 32 if sorcerer==6 else 38 if sorcerer==7 else 44 if sorcerer==8 else 57 if sorcerer==9 else 64 if sorcerer==10 else 73 if sorcerer==11 else 73 if sorcerer==12 else 83 if sorcerer==13 else 83 if sorcerer==14 else 94 if sorcerer==15 else 94 if sorcerer==16 else 107 if sorcerer==17 else 114 if sorcerer==18 else 123 if sorcerer==19 else 133
if sorcerer>=1:
    restored=0
    if magic:
        magicMax=ch.get_cc_max('Magicka')
        current=ch.get_cc('Magicka')
        lost=magicMax-current
        if lost>sorcMagicka:
            setup=magicMax-sorcMagicka
            ch.set_cc('Magicka',setup)
            restored+=lost-sorcMagicka
        if magicMax!=sorcMagicka:
            restore=max(ceil(min(lost,sorcMagicka)/2),1)
            restored+=restore
        else:
            restore=max(ceil(lost/2),1)
            restored+=restore
        ch.mod_cc('Magicka',restore)
        magicka=f''' -f "Magicka|{ch.cc_str('Magicka')} (+{restored})" '''
    if bonus:
        bonMagicMax=ch.get_cc_max('Bonus Sorcery Magicka')
        bonCurrent=ch.get_cc('Bonus Sorcery Magicka')
        bonLost=bonMagicMax-bonCurrent
        bonRestore=max(ceil(bonLost/2),1)
        ch.mod_cc('Bonus Sorcery Magicka',bonRestore)
        bonMagicka=f''' -f "Bonus Sorcery Magicka|{ch.cc_str('Bonus Sorcery Magicka')} (+{bonRestore})" '''
else:
    false=f''' -f "You are not a Sorcerer" '''
return f''' -title "{name} {'attempts to ' if not magic and not bonus else ''}restore{'' if not magic and not bonus else 's'} their stunted Magicka." {magicka} {bonMagicka} {false}'''
</drac2>
