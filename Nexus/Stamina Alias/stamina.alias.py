embed <drac2>
ch=character()
cc="Hunger"
CC="Thirst"
dd="Fatigue"
DD="Exhaustion"
desc1="Few things burn through calories as fast as adventuring, so keep some snacks in your pocket. If your Hunger reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Hunger level below 5"
desc2="Adventure, travel, and combat are thirsty work. Keep a waterskin close by to avoid dehydration. If your Thirst reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Thirst level below 5"
desc3="It takes a keen mind to watch out for danger, so get regular sleep to stay alert and aware. If your Fatigue reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Fatigue level below 5"
desc4="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
ch.create_cc_nx(cc, 0, 6, None, 'hex', 0, desc=desc1, initial_value=0)
ch.create_cc_nx(CC, 0, 6, None, 'hex', 0, desc=desc2, initial_value=0)
ch.create_cc_nx(dd, 0, 6, None, 'hex', 0, desc=desc3, initial_value=0)
ch.create_cc_nx(DD, 0, 6, None,"bubble", 0, desc=desc4, initial_value=0)
prehunger=ch.get_cc(cc)
prethirst=ch.get_cc(CC)
prefatigue=ch.get_cc(dd)
output=''
stamina=min(prehunger, prethirst, prefatigue)
dc=stamina*5
a=argparse(&ARGS&)
adv=a.adv(boolwise=True)
check=vroll(ch.saves.get('con').d20(adv))
if check.total>=dc:
    text=f''' -title "{name} makes a Stamina check." -f "DC {dc}|{check} **Success**" -f "{name} powers through|"'''
else:
    consequence=vroll('1d6')
    if consequence.total<=2:
        ch.mod_cc(cc, +1)
        hunger=ch.get_cc(cc)
        if prehunger<=4 and hunger>=5:
            ch.mod_cc(DD, +1)
            output=f''' -f "{DD}| {ch.cc_str(DD)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
        text=f''' -title "{name} makes a Stamina check." -f "DC {dc}|{check} **Failure**" -f "Consequences|{consequence}" -f "{name} struggles with Hunger|" -f "{cc}|{ch.cc_str(cc)} (+1)" {output}'''
    elif consequence.total<=4:
        ch.mod_cc(CC, +1)
        thirst=ch.get_cc(CC)
        if prethirst<=4 and thirst>=5:
            ch.mod_cc(DD, +1)
            output=f''' -f "{DD}| {ch.cc_str(DD)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
        text=f''' -title "{name} makes a Stamina check." -f "DC {dc}|{check} **Failure**" -f "Consequences|{consequence}" -f "{name} struggles with Thirst|" -f "{CC}|{ch.cc_str(CC)} (+1)" '''
    else:
        ch.mod_cc(dd, +1)
        fatigue=ch.get_cc(dd)
        if prefatigue<=4 and fatigue>=5:
            ch.mod_cc(DD, +1)
            output=f''' -f "{DD}| {ch.cc_str(DD)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
        text=f''' -title "{name} makes a Stamina check." -f "DC {dc}|{check} **Failure**" -f "Consequences|{consequence}" -f "{name} struggles with Fatigue|" -f "{dd}|{ch.cc_str(dd)} (+1)" {output}'''
return text
</drac2> -thumb {{image}}
