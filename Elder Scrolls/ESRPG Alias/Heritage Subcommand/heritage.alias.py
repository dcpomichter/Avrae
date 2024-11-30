embed <drac2>
ch=character()
arg=&ARGS&
n="\n"
state=ch.levels.total_level
prevCounters=[x.name for x in ch.consumables]
newCounters=[]
createdCounters=''
heritage=["altmer","argonian","bosmer","breton","dunmer","imperial","khajiit","nord","orsimer","redguard"]
ch.set_cvar_nx("speed","30 ft.")
ch.set_cvar_nx("languages","")
ch.set_cvar_nx("size","Medium")
ch.set_cvar_nx("creatureType","Humanoid")
ch.set_cvar_nx("resist","")
ch.set_cvar_nx("immune","")
ch.set_cvar_nx("cimmune","")
ch.set_cvar_nx("vuln","")
ch.set_cvar_nx("senses","")
checks=["speed","languages","size","creatureType","resist","immune","cimmune","vuln","senses"]
lang=""
if "&1&".lower() in heritage:
    culture=[]
    if "&1&".lower()==heritage[0]:
        ch.set_cvar("race",heritage[0].title())
        ch.set_cvar("subrace","")
        ch.set_cvar("languages","Common, Altmeris")
        lang=f''' -f "Additional Language|You learn one additional common or uncommon language of your choice." '''
        ch.create_cc(name="Highborn Magicka",minVal=0,maxVal=2 if state<=2 else 3 if state<=5 else 4 if state<=9 else 5,reset='long',dispType='bubble',desc="You have an innate well of magicka within you. You have {{maxVal}} magicka points that you can use to cast spells. Additionally, you know one cantrip and one 1st level spell from the mage spell list.\n\nAdditionally, when you reach 3rd level, you learn a 2nd level spell of your choice from the mage spell list. You regain all expended magicka when you finish a long rest.\n\nIntelligence, Willpower, or Personality is your spellcasting ability for these spells (your choice when you choose this ancestry), you must expend magicka to cast them.")
    if "&1&".lower()==heritage[1]:
        culture=["saxhleel","naga"]
        ch.set_cvar("race",heritage[1].title())
        ch.set_cvar("subrace","")
        ch.set_cvar("speed","30 ft., Swim 40 ft.")
        ch.set_cvar("languages","Common, Jel")
        if "&2&".lower() in culture:
            ch.set_cvar("subrace","&2&".title())
            if ch.get_cvar("subrace",None).lower()==culture[0]:
                ch.create_cc_nx(name="Histskin",minVal=0,maxVal=1,reset='long',dispType='square',desc="You can invoke the power of the Hist to quickly recover your injuries. When your current hit points are less than half your hit point maximum, you can use an action to immediately expend any number of your available Hit Dice. For each Hit Die spent in this way, roll your Hit Die and add your Endurance modifier to it. You regain hit points equal to the total. You can decide to spend an additional Hit Die after each roll. Once you use this trait, you must complete a long rest before you are able to use it again.")
            if ch.get_cvar("subrace",None).lower()==culture[1]:
                ch.create_cc_nx(name="Strength of the Hist",minVal=0,maxVal=1,reset='long',dispType='bubble',desc="You can call on the Hist to provide its strength when you need it most. As a bonus action, your scales harden and your bite becomes deadly for the next minute. Your sharp teeth become a natural weapon, which you can use to make unarmed strikes. If you hit with it, you deal piercing damage equal to 2d6 + your Strength modifier, and this attack is considered magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage. The armor provided by your Protective Scales trait increases to 14 + your Agility modifier. Once you use this trait, you must finish a long rest before you can do so again.")
    if "&1&".lower()==heritage[2]:
        ch.set_cvar("race",heritage[2].title())
        ch.set_cvar("subrace","")
        ch.set_cvar("speed","35 ft.")
        ch.set_cvar("languages","Common, Bosmeris, Beast Tongue")
        ch.set_cvar("resist","Poison")
        ch.create_cc_nx(name="Y'ffre's Gift: Animal Friendship",minVal=0,maxVal=1,reset='long',dispType='bubble',desc="You know one cantrip of your choice from the warden spell list. You also know the animal friendship spell and can cast it once with this trait. You regain the ability to cast it again when you finish a long rest. Intelligence, Willpower, or Personality is your spellcasting ability for these spells (your choice when you choose this ancestry).")
    if "&1&".lower()==heritage[3]:
        ch.set_cvar("race",heritage[3].title())
        ch.set_cvar("subrace","")
        ch.set_cvar("languages","Common, Cyrodiilic")
        ch.create_cc_nx(name="Dragon Skin",minVal=0,maxVal=1,reset='long',dispType='bubble',desc="Your skin thickens to become that of a dragon when harmed. When you take damage from a spell, you can use your reaction to gain resistance against the damage dealt by the spell until the start of your next turn. If the spell deals multiple types of damage, you gain resistance to each of them. Once you use this trait, you must finish a long rest before you can use it again.")
        ch.create_cc_nx(name="Find Familiar",minVal=0,maxVal=1,reset='long',dispType='bubble',desc="You know the find familiar spell and can cast it once with this trait. You regain the ability to cast it again when you finish a long rest.")
    if "&1&".lower()==heritage[4]:
        ch.set_cvar("race",heritage[4].title())
        ch.set_cvar("subrace","")
        ch.set_cvar("resist","Fire")
        ch.set_cvar("languages","Common, Dunmeris")
        ch.create_cc_nx(name="Ancestor Guardian",minVal=0,maxVal=1,reset='long',dispType='square',desc="When you take damage from an attack, you can use your reaction to call forth your ancestors to protect you. Your ancestors appear as incorporeal beings in an unoccupied space within 5 feet of you and within 5 feet of your attacker. The damage dealt by the attack is reduced by 1d6 + your Willpower modifier and the attacker takes an amount of damage equal to the amount rolled. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.")
    if "&1&".lower()==heritage[5]:
        culture=["colovian","nibenese"]
        ch.set_cvar("race",heritage[5].title())
        ch.set_cvar("subrace","")
        ch.set_cvar("languages","Common, Tamrielic")
        lang=f''' -f "Additional Language|You learn one additional common or uncommon language of your choice." '''
        ch.create_cc_nx(name="Imperial Luck (d4)",minVal=0,maxVal="proficiencyBonus",reset='long',dispType='square',desc="You have a number of Imperial Luck Dice, which are d4s, equal to your proficiency bonus. You can expend one Imperial Luck Die to add it to an attribute check, attack roll, or saving throw you make. You can wait until after you roll the d20 before deciding to use the Imperial Luck Dice, but must decide before the GM determines whether the roll succeeds or fails. You regain your expended Imperial Luck Dice when you finish a long rest.")
        if "&2&".lower() in culture:
            ch.set_cvar("subrace","&2&".title())
        if ch.get_cvar("subrace",None).lower()==culture[1]:
            ch.create_cc_nx(name="Voice of the Emperor",minVal=0,maxVal=1,reset='long',dispType='bubble',desc="You know the charm person spell. Once between long rests, you are able to cast this spell without expending magicka points and without your target knowing it was cast on them. Intelligence, Willpower, or Personality is your spellcasting ability for this spell (your choice when you choose this ancestry)")
    if "&1&".lower()==heritage[6]:
        culture=["alfiq","cathay","dagi","ohmes","pahmar","senche","suthay","tojay"]
        ch.set_cvar("race",heritage[6].title())
        ch.set_cvar("subrace","")
        ch.set_cvar("speed","35 ft., Climb 20 ft.")
        ch.set_cvar("senses","Darkvision 60 ft.")
        ch.set_cvar("languages","Common, Ta'agra")
        ch.create_cc_nx(name="Feline Ambush",minVal=0,maxVal=1,reset='short',dispType='square',desc="If you hit a creature with an attack roll, the creature takes an extra 2d4 damage if it hasn't taken a turn yet in the current combat. You can use this trait only once per short rest.")
        ch.create_cc_nx(name="Cat Quick",minVal=0,maxVal=1,reset='short',dispType='square',desc="When you make an Agility saving throw, you can use your reaction to add 1d4 to the roll. Once you use this trait, you must finish a short or long rest before you can do so again.")
        if "&2&".lower() in culture:
            ch.set_cvar("subrace","&2&".title())
        if ch.get_cvar("subrace",None).lower()==culture[0]:
            ch.set_cvar("size","Tiny")
            ch.create_cc_nx(name="Compensating Magicka",minVal=0,maxVal=2,reset='long',dispType='bubble',desc="You have an innate well of magicka within you. You have 2 magicka points that you can use to cast spells. Additionally, you know one cantrip and one 1st level spell from the mage spell list. You regain all expended magicka when you finish a long rest. Intelligence, Willpower, or Personality is your spellcasting ability for these spells (your choice when you choose this ancestry), you must expend magicka to cast them, and you can only cast them at their base level.")
            ch.set_cvar("resist","Fall")
        if ch.get_cvar("subrace",None).lower()==culture[2]:
            ch.set_cvar("size","Small")
            if state>=3:
                ch.create_cc_nx(name="Natural Magic: Magic Missile",minVal=0,maxVal=1,reset='long',dispType='bubble',desc="When you reach 3rd level, you can cast the magic missile spell once with this trait and regain the ability to do so when you finish a long rest. Intelligence, Willpower, or Personality is your spellcasting ability for these spells (your choice when you choose this ancestry).")
            if state>=5:
                ch.create_cc_nx(name="Natural Magic: Darkness",minVal=0,maxVal=1,reset='long',dispType='bubble',desc="When you reach 5th level, you can cast the darkness spell once with this trait and regain the ability to do so when you finish a long rest. Intelligence, Willpower, or Personality is your spellcasting ability for these spells (your choice when you choose this ancestry).")
        if ch.get_cvar("subrace",None).lower()==culture[3]:
            ch.set_cvar("speed","35 ft.")
        if ch.get_cvar("subrace",None).lower()==culture[5]:
            ch.set_cvar("size","Large")
    if "&1&".lower()==heritage[7]:
        culture=["skaal"]
        ch.set_cvar("race",heritage[7].title())
        ch.set_cvar("subrace","")
        ch.set_cvar("resist","Cold")
        ch.create_cc_nx(name="Battlecry",minVal=0,maxVal=1,reset='short',dispType='bubble',desc="As an action, you shout a battle cry that strikes fear into an enemy. Choose one creature that is within 30 feet of you that can see and hear you. That target must succeed on a Willpower saving throw or become frightened of you. The difficulty check of this save is equal to 8 + your Endurance modifier + your proficiency bonus. The frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. When you reach 5th level, you can instead choose to force each creature of your choice in a 30-foot cone to make this saving throw, rather than a single target. Once you use this trait, you can't use it again until you finish a short or long rest.")
        if "&2&".lower() in culture:
            ch.set_cvar("subrace","&2&".title())
        if ch.get_cvar("subrace",None).lower()==culture[0]:
            if state>=3:
                ch.create_cc_nx(name="Oneness: Animal Friendship",minVal=0,maxVal=1,reset='short',dispType='bubble',desc="Once you reach 3rd level, you can cast the animal friendship spell once with this trait, and you regain the ability to do so when you finish a long rest. You can also cast this spell using magicka, providing you can cast spells at this level. Intelligence, Willpower, or Personality is your spellcasting ability for these spells (your choice when you choose this ancestry).")
    if "&1&".lower()==heritage[8]:
        culture=["city","wild","wood"]
        ch.set_cvar("race",heritage[8].title())
        ch.set_cvar("subrace","")
        ch.set_cvar("languages","Common, Orcish")
        ch.create_cc_nx(name="Berserk",minVal=0,maxVal=1,reset='long',dispType='bubble',desc="As a bonus action, you gain temporary hit points equal to twice your character level for the next minute. Additionally, you gain advantage on the first attack you make on each of your turns during this time. Once you use this trait, you can't use it again until you finish a long rest.")
        if "&2&".lower() in culture:
            ch.set_cvar("subrace","&2&".title())
    if "&1&".lower()==heritage[9]:
        culture=["crowns","forebears"]
        ch.set_cvar("race",heritage[9].title())
        ch.set_cvar("subrace","")
        ch.set_cvar("languages","Common, Yoku")
        ch.create_cc_nx(name="Ra’Gada Spirit",minVal=0,maxVal=1,reset='long',dispType='square',desc="When you fail a saving throw against a spell or magical effect, you can use your reaction to reroll the saving throw, possibly turning the failure into a success. Once you use this trait, you must finish a long rest before you can do so again.")
        if "&2&".lower() in culture:
            ch.set_cvar("subrace","&2&".title())
    race=ch.get_cvar("race",None)
    subrace=ch.get_cvar("subrace",None)
    if race!=None:
        currentRace=f''' -f "Heritage Name|{race}|inline" '''
        if race.lower() in heritage:
            if race.lower()==heritage[1] or race.lower()==heritage[5] or race.lower()==heritage[6] or race.lower()==heritage[7] or race.lower()==heritage[8] or race.lower()==heritage[9]:
                currentRace=f''' -f "Heritage Name|{race}" -f "Remember...|Run this command with your Heritage and sub-culture/sub-ancestry if available to fully define and add all counters." '''
                if subrace!="":
                    currentRace=f''' -f "Heritage Name|{ch.get_cvar("subrace","")} {ch.get_cvar("race","")}|inline" '''
    else:
        currentRace=f''' -f "You have no Heritage| Run this command again with your Heritage and sub-culture/sub-ancestry to create the appropriate cvars and counters." '''
else:
    race=ch.get_cvar("race",None)
    subrace=ch.get_cvar("subrace",None)
    if race!=None and race.lower()==heritage[0]:
        if state<=2:
            ch.create_cc_nx(name="Highborn Magicka",minVal=0,maxVal=2 if state<=2 else 3 if state<=5 else 4 if state<=9 else 5,reset='long',dispType='bubble',desc="You have an innate well of magicka within you. You have {{maxVal}} magicka points that you can use to cast spells. Additionally, you know one cantrip and one 1st level spell from the mage spell list.\n\nAdditionally, when you reach 3rd level, you learn a 2nd level spell of your choice from the mage spell list. You regain all expended magicka when you finish a long rest.\n\nIntelligence, Willpower, or Personality is your spellcasting ability for these spells (your choice when you choose this ancestry), you must expend magicka to cast them.")
    if race!=None and race.lower()==heritage[6]:
        if subrace.lower()=="dagi":
            if state>=3:
                ch.create_cc_nx(name="Natural Magic: Magic Missile",minVal=0,maxVal=1,reset='long',dispType='bubble',desc="When you reach 3rd level, you can cast the magic missile spell once with this trait and regain the ability to do so when you finish a long rest. Intelligence, Willpower, or Personality is your spellcasting ability for these spells (your choice when you choose this ancestry).")
            if state>=5:
                ch.create_cc_nx(name="Natural Magic: Darkness",minVal=0,maxVal=1,reset='long',dispType='bubble',desc="When you reach 5th level, you can cast the darkness spell once with this trait and regain the ability to do so when you finish a long rest. Intelligence, Willpower, or Personality is your spellcasting ability for these spells (your choice when you choose this ancestry).")
    if race!=None and race.lower()==heritage[7]:
        if subrace.lower()=="skaal":
            if state>=3:
                ch.create_cc_nx(name="Oneness: Animal Friendship",minVal=0,maxVal=1,reset='short',dispType='bubble',desc="Once you reach 3rd level, you can cast the animal friendship spell once with this trait, and you regain the ability to do so when you finish a long rest. You can also cast this spell using magicka, providing you can cast spells at this level. Intelligence, Willpower, or Personality is your spellcasting ability for these spells (your choice when you choose this ancestry).")
    if race!=None:
        currentRace=f''' -f "Heritage Name|{race}" -f "Remember...|Run this command with your Heritage and sub-culture/sub-ancestry if available to fully define and add all counters." '''
        if subrace!=None:
            currentRace=f''' -f "Heritage Name|{ch.get_cvar("subrace","")} {ch.get_cvar("race","")}|inline" '''
    else:
        currentRace=f''' -f "You have no Heritage| Run this command again with your Heritage and sub-culture/sub-ancestry to create the appropriate cvars and counters." '''
for counter in ch.consumables:
    if counter.name not in prevCounters:
        newCounters.append(f"{counter.name}: {ch.cc_str(counter.name)}")
if newCounters!=[]:
    createdCounters=f'''-f "Counters Created|{n.join(newCounters)}" '''
out=[f""" -title "{name} {'has not ' if race==None else ' '}set{'' if race==None else 's'} their Heritage{'!' if race==None else ' to...'}{ch.get_cvar("race","")}" """]
out.append(f"""{currentRace}""")
for name, content  in ch.cvars.items():
    if content!="":
        if name in checks:
            if name=="creatureType":
                out.append(f""" -f "Creature Type|{ch.get_cvar(name,"")}|inline" """)
            else:
                out.append(f""" -f "{name.title()}|{ch.get_cvar(name,"")}|inline" """)
out.append(f"""{createdCounters}""")
return  n.join(out)
</drac2>
