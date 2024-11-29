<drac2>
ch=character()
warlock=ch.levels.get('Warlock')
cc="Sacrificial Bargain"
desc= "Once per short rest, when you cast a warlock spell of 1st-level or higher, you may spend a number of hit die equal to your warlock spell level to cast the spell without expending a spell slot. If the spell can't be cast at a higher level, you may instead spend a number of hit die equal to the spell level."
HD_types=[x.name for x in ch.consumables if 'Hit Dice' in x.name]
HD_output='\n'.join(f"{x}: {ch.cc_str(x)}" for x in HD_types)
output=''
if warlock>=1:
    ch.create_cc_nx(cc, 0, 1, 'short', 'star', 1, desc=desc, initial_value=1)
    avail=ch.get_cc(cc)
    if avail==1:
        slot=1 if warlock<=2 else 2 if warlock<=4 else 3 if warlock<=6 else 4 if warlock<=8 else 5
        for hd in HD_types:
            if ch.cc_exists(hd) and ch.get_cc(hd)>=slot:
                ch.mod_cc(hd, -slot)
                output=f''' -f "{hd}|{ch.cc_str(hd)} (-{slot})" '''
                ch.mod_cc(cc, -1)
                text=f''' -l {slot} -i -f "{cc}|Once per short rest, when you cast a warlock spell of 1st-level or higher, you may spend a number of hit die equal to your warlock spell level to cast the spell without expending a spell slot." -f "{cc}|{ch.get_cc(cc)+' (-1)'}" {output}'''
                break
            else:
                text=f''' -f "Hit Dice| {HD_output}" -f " You do not have the strength to call on your Patron." '''
    else:
        text=f''' -f "{cc}| You do not have the will to bargain" -f "{cc}|{ch.get_cc(cc)} "'''
else:
    text=f''' -f "{cc}| You have no Patron to Bargain with" -f "{cc}|**No Counter**"'''
return text
</drac2>
