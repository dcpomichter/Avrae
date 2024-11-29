embed <drac2>
ch=character()
args=&ARGS&
cc="Fatigue"
CC="Exhaustion"
desc1="It takes a keen mind to watch out for danger, so get regular sleep to stay alert and aware. If your Fatigue reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Fatigue level below 5"
desc2="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
ch.create_cc_nx(cc, 0, 6, None, 'hex', 0, desc=desc1, initial_value=0)
ch.create_cc_nx(CC, 0, 6, None,"bubble", 0, desc=desc2, initial_value=0)
subclasses=get("subclass", "")
class_list=[('Wizard', 0), ('Sorcerer', 0), ('Bard', 0), ('Cleric', 0), ('Druid', 0), ('Paladin', 1), ('Ranger', 1), ('Artificer', 1), ('Warlock', 0)]
if "Eldritch Knight" in subclasses:
    class_list.append(("Fighter", 2))
if "Arcane Trickster" in subclasses:
    class_list.append(("Rogue", 2))
highest, value=max(class_list, key=lambda x:(ch.levels.get(x[0]), 2-x[1]))
stressed=vroll('1d4')
relaxed=vroll('1d6')
a=argparse(&ARGS&)
DC=a.last('dc', 10, int)
adv=a.adv(boolwise=True)
check=vroll(ch.saves.get('con').d20(adv))
HD_types=[x.name for x in ch.consumables if 'Hit Dice' in x.name]
HD_output='\n'.join(f"{x}- {ch.cc_str(x)}" for x in HD_types)
output=''
prefatigue=ch.get_cc(cc)
fatigue_output=''
fatigue_mount=''
mount_output=''
if "mount" in args:
    dd="Fatigue-Mount"
    mount=['horse', 'donkey', 'wolf', 'ox', 'camel', 'mule', 'mastiff', 'pony', 'mount']
    for x in mount:
        real=ch.cc_exists(f"""Fatigue-{x.title()}""")
        if real:
            dd=f"""Fatigue-{x.title()}"""
            break
    DD="Exhaustion-Mount"
    for x in mount:
        real=ch.cc_exists(f"""Exhaustion-{x.title()}""")
        if real:
            DD=f"""Exhaustion-{x.title()}"""
            break
    ch.create_cc_nx(dd, 0, 6, None, 'hex', 0, desc=desc1, initial_value=0)
    ch.create_cc_nx(DD, 0, 6, None,"bubble", 0, desc=desc2, initial_value=0)
    premount=ch.get_cc(dd)
    ch.mod_cc(dd, -3)
    mountfatigue=ch.get_cc(dd)
    if premount>=5 and mountfatigue<=4:
        ch.mod_cc(DD, -1)
        fatigue_mount=f''' -f "{DD}| {ch.cc_str(DD)} (-1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
    mount_output=f''' -f "{dd}|{ch.cc_str(dd)+' (-3)'}" '''
if check.total<DC:
    ch.mod_cc(cc, -1)
    fatigue=ch.get_cc(cc)
    if prefatigue>=5 and fatigue<=4:
        ch.mod_cc(CC, -1)
        fatigue_output=f''' -f "{CC}| {ch.cc_str(CC)} (-1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
    ch.mod_cc("Stress", +stressed.total)
    text=f''' -title "{name} couldn't Sleep!" -f "DC|{DC}" -f "Sleep Check|{check} (**Failure**)" -f "{cc}|{ch.cc_str(cc)+' (-1)'}" {fatigue_output} -f "Stress|{ch.cc_str("Stress")+f' (+{stressed})'}" -f "Hit Dice| {HD_output}" {mount_output} {fatigue_mount} '''
else:
    burn=ch.cc_exists("Burnout")
    if burn:
       modify=-1 if ch.get_cc("Burnout")>=value+1 else +0
       ch.mod_cc("Burnout", modify)
    ch.mod_cc(cc, -3)
    fatigue=ch.get_cc(cc)
    if prefatigue>=5 and fatigue<=4:
        ch.mod_cc(CC, -1)
        fatigue_output=f''' -f "{CC}| {ch.cc_str(CC)} (-1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
    ch.mod_cc("Stress", -relaxed.total)
    for hd in HD_types:
        if ch.cc_exists(hd) and ch.get_cc(hd)<ch.get_cc_max(hd):
            ch.mod_cc(hd, +1)
            output=f''' -f "{hd}|{ch.cc_str(hd)} (+1)" '''
            break
    text=f''' -title "{name} Sleeps soundly." -f "DC|{DC}" -f "Sleep Check|{check} (**Success**)" -f "{cc}|{ch.cc_str(cc)+' (-3)'}" {fatigue_output} -f "Stress| {ch.cc_str("Stress")+f' (-{relaxed})'}" {output} -f "Burnout| {ch.cc_str("Burnout")} ({modify})" {mount_output} {fatigue_mount} ''' if burn else f''' -title "{name} Sleeps soundly." -f "DC|{DC}" -f "Sleep Check|{check} (**Success**)" -f "{cc}|{ch.cc_str(cc)+' (-3)'}" -f "Stress| {ch.cc_str("Stress")+f' (-{relaxed})'}" {output} {mount_output} {fatigue_mount}'''
return text
</drac2> -thumb {{image}}
