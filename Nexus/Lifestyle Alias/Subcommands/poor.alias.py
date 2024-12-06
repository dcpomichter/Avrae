embed <drac2>
ch=character()
a=argparse(&ARGS&)
i=a.get('i')
EE="Hunger"
ff="Thirst"
FF="Fatigue"
ee="Exhaustion"
desc6="Few things burn through calories as fast as adventuring, so keep some snacks in your pocket. If your Hunger reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Hunger level below 5"
desc7="Adventure, travel, and combat are thirsty work. Keep a waterskin close by to avoid dehydration. If your Thirst reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Thirst level below 5"
desc8="It takes a keen mind to watch out for danger, so get regular sleep to stay alert and aware. If your Fatigue reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Fatigue level below 5"
desc4="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
ch.create_cc_nx(EE, 0, 6, None, 'hex', 0, desc=desc6, initial_value=0)
ch.create_cc_nx(ff, 0, 6, None, 'hex', 0, desc=desc7, initial_value=0)
ch.create_cc_nx(FF, 0, 6, None, 'hex', 0, desc=desc8, initial_value=0)
ch.create_cc_nx(ee, 0, 6, None,"bubble", 0, desc=desc4, initial_value=0)
coinpurse=''
if not i:
    ch.coinpurse.modify_coins(gp=-1, sp=-5)
    coinpurse=f""" -f "Coinpurse|{ch.coinpurse.compact_str()} (-1.5)" """
ch.set_hp((ch.max_hp)*0.75)
prehunger=ch.get_cc(EE)
prethirst=ch.get_cc(ff)
prefatigue=ch.get_cc(FF)
ch.set_cc(EE, 4)
ch.set_cc(ff, 4)
ch.set_cc(FF, 4)
hunger=ch.get_cc(EE)
thirst=ch.get_cc(ff)
fatigue=ch.get_cc(FF)
output=''
if prehunger>=5 and hunger<=4:
    ch.mod_cc(ee, -1)
    output=f''' -f "{ee}| {ch.cc_str(ee)}" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
if prethirst>=5 and thirst<=4:
    ch.mod_cc(ee, -1)
    output=f''' -f "{ee}| {ch.cc_str(ee)}" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
if prefatigue>=5 and fatigue<=4:
    ch.mod_cc(ee, -1)
    output=f''' -f "{ee}| {ch.cc_str(ee)}" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
HD_types=[x.name for x in ch.consumables if 'Hit Dice' in x.name]
for hd in HD_types:
        if ch.cc_exists(hd):
            ch.set_cc(hd, (ch.get_cc_max(hd)//2))
HD_output='\n'.join(f"{x}: {ch.cc_str(x)}" for x in HD_types)
text=f''' -title "{name} lives a Poor life." -f "{EE}| {ch.cc_str(EE)}" -f "{ff}| {ch.cc_str(ff)}" -f "{FF}| {ch.cc_str(FF)}" {output} -f "{name} new Max HP| {ch.hp}" -f "Starting Hit Dice| {HD_output}" {coinpurse} '''
return text
</drac2> -thumb {{image}}
