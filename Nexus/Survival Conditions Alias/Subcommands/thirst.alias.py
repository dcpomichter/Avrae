embed <drac2>
ch=character()
cc="Thirst"
ee="Exhaustion"
desc1="Adventure, travel, and combat are thirsty work. Keep a waterskin close by to avoid dehydration. If your Thirst reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Thirst level below 5"
desc4="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
ch.create_cc_nx(cc, 0, 6, None, 'hex', 0, desc=desc1, initial_value=0)
ch.create_cc_nx(ee, 0, 6, None,"bubble", 0, desc=desc4, initial_value=0)
prethirst=ch.get_cc(cc)
a=argparse(&ARGS&)
n=a.last('n', 1, int)
ch.mod_cc(cc, +abs(n))
thirst=ch.get_cc(cc)
exhaust=''
if prethirst<=4 and thirst>=5:
    ch.mod_cc(ee, +1)
    exhaust=f''' -f "{ee}|{ch.cc_str(ee)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
text=f''' -title "{name} adds to their Thirst" -f "{cc}|{ch.cc_str(cc)} (+{abs(n)})" {exhaust}'''
return text
</drac2> -thumb {{image}}
