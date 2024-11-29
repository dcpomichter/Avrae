embed <drac2>
ch=character()
cc="Fatigue"
ee="Exhaustion"
desc1="It takes a keen mind to watch out for danger, so get regular sleep to stay alert and aware. If your Fatigue reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Fatigue level below 5"
desc4="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
ch.create_cc_nx(cc, 0, 6, None, 'hex', 0, desc=desc1, initial_value=0)
ch.create_cc_nx(ee, 0, 6, None,"bubble", 0, desc=desc4, initial_value=0)
preFatigue=ch.get_cc(cc)
a=argparse(&ARGS&)
n=a.last('n', 1, int)
ch.mod_cc(cc, +abs(n))
Fatigue=ch.get_cc(cc)
exhaust=''
if preFatigue<=4 and Fatigue>=5:
    ch.mod_cc(ee, +1)
    exhaust=f''' -f "{ee}|{ch.cc_str(ee)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
text=f''' -title "{name} adds to their Fatigue" -f "{cc}|{ch.cc_str(cc)} (+{abs(n)})" {exhaust}'''
return text
</drac2> -thumb {{image}}
