embed <drac2>
ch=character()
cc="Exhaustion"
desc1="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
ch.create_cc_nx(cc, 0, 6, None, "bubble", 0, desc=desc1, initial_value=0)
barb=ch.levels.get('Barbarian')
HD_types=[x.name for x in ch.consumables if 'Hit Dice' in x.name]
HD_output='\n'.join(f"{x}: {ch.cc_str(x)}" for x in HD_types)
output=''
if barb>=1:
    for hd in HD_types:
        if ch.cc_exists(hd) and ch.get_cc(hd):
            ch.mod_cc(hd, -1)
            output=f''' -f "{hd}|{ch.cc_str(hd)} (-1)"'''
            text=f''' -title "{name} comes out of their Frenzy." {output} -f "Effect| When your frenzied rage ends, you lose one unspent hit die." '''
            break
        else:
            ch.mod_cc(cc, +1)
            text=f''' -title "{name} comes out of their Frenzy." -f "Hit Dice| {HD_output}" -f "{cc}|{ch.cc_str(cc)} (+1)" -f "Effect| When your frenzied rage ends, you lose one unspent hit die. If you don't have any hit die remaining, you instead suffer one level of exhaustion." '''
else:
    text=f''' -title "{name} wishes they could Frenzy." -f "Barbarian Level| {barb}" '''
return text
</drac2> -thumb {{image}}
