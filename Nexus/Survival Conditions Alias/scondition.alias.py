embed <drac2>
ch=character()
cc="Hunger"
CC="Thirst"
DD="Fatigue"
ee="Exhaustion"
desc1="Few things burn through calories as fast as adventuring, so keep some snacks in your pocket. If your Hunger reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Hunger level below 5"
desc2="Adventure, travel, and combat are thirsty work. Keep a waterskin close by to avoid dehydration. If your Thirst reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Thirst level below 5"
desc3="It takes a keen mind to watch out for danger, so get regular sleep to stay alert and aware. If your Fatigue reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Fatigue level below 5"
desc4="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
ch.create_cc_nx(cc, 0, 6, None, 'hex', 0, desc=desc1, initial_value=0)
ch.create_cc_nx(CC, 0, 6, None, 'hex', 0, desc=desc2, initial_value=0)
ch.create_cc_nx(DD, 0, 6, None, 'hex', 0, desc=desc3, initial_value=0)
ch.create_cc_nx(ee, 0, 6, None,"bubble", 0, desc=desc4, initial_value=0)
text=f''' -title "{name} checks their condition" -f "{cc}|{ch.cc_str(cc)}" -f "{CC}|{ch.cc_str(CC)}" -f "{DD}|{ch.cc_str(DD)}" -f "{ee}|{ch.cc_str(ee)}" '''
return text
</drac2> -thumb {{image}}
