embed <drac2>
ch=character()
cc="Hunger"
CC="Thirst"
dd="Fatigue"
ee="Exhaustion"
desc1="Few things burn through calories as fast as adventuring, so keep some snacks in your pocket. If your Hunger reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Hunger level below 5"
desc2="Adventure, travel, and combat are thirsty work. Keep a waterskin close by to avoid dehydration. If your Thirst reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Thirst level below 5"
desc3="It takes a keen mind to watch out for danger, so get regular sleep to stay alert and aware. If your Fatigue reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Fatigue level below 5"
desc4="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
ch.create_cc_nx(cc, 0, 6, None, 'hex', 0, desc=desc1, initial_value=0)
ch.create_cc_nx(CC, 0, 6, None, 'hex', 0, desc=desc2, initial_value=0)
ch.create_cc_nx(dd, 0, 6, None, 'hex', 0, desc=desc3, initial_value=0)
ch.create_cc_nx(ee, 0, 6, None,"bubble", 0, desc=desc4, initial_value=0)
ch.coinpurse.modify_coins(gp=0)
ch.set_hp((ch.max_hp)//2)
prehunger=ch.get_cc(cc)
prethirst=ch.get_cc(CC)
prefatigue=ch.get_cc(dd)
ch.set_cc(cc, 6)
ch.set_cc(CC, 6)
ch.set_cc(dd, 6)
hunger=ch.get_cc(cc)
thirst=ch.get_cc(CC)
fatigue=ch.get_cc(dd)
output=''
if prehunger<=4 and hunger>=5:
    ch.mod_cc(ee, +1)
    output=f''' -f "{ee}| {ch.cc_str(ee)}" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
if prethirst<=4 and thirst>=5:
    ch.mod_cc(ee, +1)
    output=f''' -f "{ee}| {ch.cc_str(ee)}" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
if prefatigue<=4 and fatigue>=5:
    ch.mod_cc(ee, +1)
    output=f''' -f "{ee}| {ch.cc_str(ee)}" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
HD_types=[x.name for x in ch.consumables if 'Hit Dice' in x.name]
for hd in HD_types:
        if ch.cc_exists(hd):
            ch.set_cc(hd, 0)
HD_output='\n'.join(f"{x}: {character().cc_str(x)}" for x in HD_types)
text=f''' -title "{name} lives a Wretched life." -f "{cc}| {ch.cc_str(cc)}" -f "{CC}| {ch.cc_str(CC)}" -f "{dd}| {ch.cc_str(dd)}" {output} -f "{name} new Max HP| {ch.hp}" -f "Starting Hit Dice| {HD_output}" -f "Coinpurse|{ch.coinpurse.compact_str()}" '''
return text
</drac2> -thumb {{image}}
