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
day=['dawn', 'noon', 'dusk']
restore=f"""-f "To recover Hunger and Thirst use the `!eat` and `!drink` aliases." """
output=''
text=f''' -title "{name} is ready to get through the day" -f "{cc}|{ch.cc_str(cc)}" -f "{CC}|{ch.cc_str(CC)}" -f "{DD}|{ch.cc_str(DD)}" -f "{ee}|{ch.cc_str(ee)}"  '''
if "&1&".lower() in day:
  if "&1&".lower()==day[0]:
    prehunger=ch.get_cc(cc)
    prethirst=ch.get_cc(CC)
    ch.mod_cc(cc, +1)
    ch.mod_cc(CC, +1)
    hunger=ch.get_cc(cc)
    thirst=ch.get_cc(CC)
    if prehunger<=4 and hunger>=5:
        ch.mod_cc(ee, +1)
        output=f''' -f "{ee}| {ch.cc_str(ee)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
        if prethirst<=4 and thirst>=5:
            ch.mod_cc(ee, +1)
            output=f''' -f "{ee}| {ch.cc_str(ee)} (+2)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
    elif prethirst<=4 and thirst>=5:
            ch.mod_cc(ee, +1)
            output=f''' -f "{ee}| {ch.cc_str(ee)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5."  '''
    text=f''' -title "{name} starts their day." -f "{cc}|{ch.cc_str(cc)+' (+1)'}" -f "{CC}|{ch.cc_str(CC)+' (+1)'}" {output} -thumb https://media.discordapp.net/attachments/879551881557454859/1126902510095970415/2169475-bigthumbnail.png '''
  elif "&1&".lower()==day[1]:
    prefatigue=ch.get_cc(DD)
    ch.mod_cc(DD, +1)
    fatigue=ch.get_cc(DD)
    output=''
    if prefatigue<=4 and fatigue>=5:
        ch.mod_cc(ee, +1)
        output=f''' -f "{ee}| {ch.cc_str(ee)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
    text=f''' -title "{name} continues through the day." -f "{DD}|{ch.cc_str(DD)+' (+1)'}" {output} -thumb https://media.discordapp.net/attachments/879551881557454859/1126902439400968193/86cbaf1e8a6778e1e79ec5a803ac8860.png?width=828&height=580 '''
  else:
    prehunger=ch.get_cc(cc)
    prethirst=ch.get_cc(CC)
    prefatigue=ch.get_cc(DD)
    ch.mod_cc(cc, +1)
    ch.mod_cc(CC, +1)
    ch.mod_cc(DD, +1)
    hunger=ch.get_cc(cc)
    thirst=ch.get_cc(CC)
    fatigue=ch.get_cc(DD)
    output=''
    if prehunger<=4 and hunger>=5:
        ch.mod_cc(ee, +1)
        output=f''' -f "{ee}| {ch.cc_str(ee)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
        if prethirst<=4 and thirst>=5:
            ch.mod_cc(ee, +1)
            output=f''' -f "{ee}| {ch.cc_str(ee)} (+2)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
            if prefatigue<=4 and fatigue>=5:
                ch.mod_cc(ee, +1)
                output=f''' -f "{ee}| {ch.cc_str(ee)} (+3)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
        elif prefatigue<=4 and fatigue>=5:
            ch.mod_cc(ee, +1)
            output=f''' -f "{ee}| {ch.cc_str(ee)} (+2)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
    elif prethirst<=4 and thirst>=5:
        ch.mod_cc(ee, +1)
        output=f''' -f "{ee}| {ch.cc_str(ee)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
        if prefatigue<=4 and fatigue>=5:
            ch.mod_cc(ee, +1)
            output=f''' -f "{ee}| {ch.cc_str(ee)} (+2)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5.\n\nYou can have 1 Exhaustion level per Condition." '''
    elif prefatigue<=4 and fatigue>=5:
        ch.mod_cc(ee, +1)
        output=f''' -f "{ee}| {ch.cc_str(ee)} (+1)" -f "Survival| If one of your Survival Conditions reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering that Survival Condition below 5." '''
    text=f''' -title "{name} finishes their day." -f "{cc}|{ch.cc_str(cc)+' (+1)'}" -f "{CC}|{ch.cc_str(CC)+' (+1)'}" -f "{DD}|{ch.cc_str(DD)+' (+1)'}" {output} -thumb https://media.discordapp.net/attachments/879551881557454859/1126902358367010817/1096617-landscape-fantasy-art-sunset-artwork-sunrise-evening-morning-dusk-dawn-landmark-screenshot-atmospheric-phenomenon-computer-wallpaper.png?width=828&height=458 '''
return text+restore
</drac2>
