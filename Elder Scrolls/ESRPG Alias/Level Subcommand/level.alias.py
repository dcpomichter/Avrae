embed <drac2>
ch=character()
n="\n"
args=&ARGS&
total=ch.levels.total_level
barbarian=ch.levels.get('Barbarian')
bard=ch.levels.get('Bard')
crusader=ch.levels.get('Crusader')
mage=ch.levels.get('Mage')
monk=ch.levels.get('Monk')
necromancer=ch.levels.get('Necromancer')
nightblade=ch.levels.get('Nightblade')
priest=ch.levels.get('Priest')
ranger=ch.levels.get('Ranger')
rogue=ch.levels.get('Rogue')
sorcerer=ch.levels.get('Sorcerer')
spellsword=ch.levels.get('Spellsword')
thief=ch.levels.get('Thief')
warden=ch.levels.get('Warden')
warrior=ch.levels.get('warrior')
classes=load_json(get_gvar("001d4cc5-ad61-4d66-b947-cdfee9436b02"))
currentSubclasses=load_json(get("subclass", "{}"))
def merge_dicts(dict1, dict2):
  for class_name, details in dict2.items():
    if class_name in dict1:
      dict1[class_name]["sub_level"]=details.get("sub_level", dict1[class_name]["sub_level"])
      dict1[class_name]["hit_die"]=details.get("hit_die", dict1[class_name]["hit_die"])
      dict1[class_name]["subclasses"].extend(details.get("subclasses", []))
      dict1[class_name]["counters"].extend(details.get("counters",[]))
    else:
      dict1[class_name] = details
  return dict1
server_classes=load_json(get_svar('esclass_info', '{}'))
classes=merge_dicts(classes, server_classes)
uvar_classes=load_json(get_uvar('esclass_info', '{}'))
classes=merge_dicts(classes, uvar_classes)
prevCounters=[x.name for x in ch.consumables]
newCounters=[]
dice_out = []
sub_out  = []
note_out = []
hit_dice = {}
if len(args)>=2:
    arg_cls, arg_sub=args[:2]
    arg_cls=([cls for cls in classes if arg_cls.lower() in cls.lower() and ch.levels.get(cls) >= classes[cls].sub_level] + [""])[0]
    arg_sub=([sub for sub in classes.get(arg_cls, {}).get("subclasses", []) if arg_sub.lower() in sub.lower()] + [""])[0]
    if arg_cls and arg_sub:
        size=classes[arg_cls].get("hit_die", 0)
        if not hit_dice.get(size):
            hit_dice[size]={'str': "", 'int': 0}
        currentSubclasses[f"{arg_cls}Level"] = arg_sub
        ch.set_cvar("subclass", dump_json(currentSubclasses))
        hit_dice[size]['str']+=f"+{arg_cls}Level"
        hit_dice[size]['int']+=ch.levels.get(arg_cls)
if barbarian>=1:
    ch.create_cc(name="Rage",minVal=0,maxVal=2 if barbarian<=2 else 3 if barbarian<=5 else 4 if barbarian<=11 else 5 if barbarian<=16 else 6, reset="long",dispType="hex",desc="On your turn, you can enter a rage as a bonus action.While raging, you gain the following benefits if you aren’t wearing heavy armor:\n- You have advantage on Strength checks and Strength saving throws.\n- When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column o f the Barbarian table.\n- You have resistance to bludgeoning, piercing, and slashing damage.\n- If you are able to cast spells, you can’t cast them or concentrate on them while raging.\n\nYour rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven’t attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.\nOnce you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again.")
    if barbarian>=11:
        ch.create_cc(name="Relentless Rage",minVal=0, reset="short", reset_to=0,desc="Your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you’re raging and don’t die outright, you can make a DC 10 Endurance saving throw. If you succeed, you drop to 1 hit point instead.\n\nEach time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10.")
if bard>=1:
    ch.create_cc(name="Bardic Inspiration",minVal=0,maxVal=max(charismaMod,1), reset="long" if bard<=4 else "short",dispType="square",desc="You use a bonus action on your turn to choose one creature, other than yourself, within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a d6.\n\nOnce within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the GM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time.\n\nYou can use this feature a number of times equal to your Personality modifier (a minimum of once). You regain any expended uses when you finish a long rest.\n\nYour Bardic Inspiration die changes when you reach certain levels in the class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level.")
if crusader>=1:
    ch.create_cc(name="Divine Sense",minVal=0,maxVal=charismaMod+1, reset="long",dispType="hex",desc="As an action, you can open your awareness to detect such forces. Until the end of your next turn, you know the location of any celestial (aedra), fiend (daedra), or undead within 60 feet of you that is not behind total cover. You know the type of any being whose presence you sense, but not its identity. Within the same radius, you also detect the presence of any place or object that has been consecrated or desecrated, as with the hallow spell.\n\nYou can use this feature a number of times equal to 1 + your Personality modifier. When you finish a long rest, you regain all expended uses.")
    ch.create_cc(name="Lay on Hands",minVal=0,maxVal=CrusaderLevel*5,reset="long",desc="You have a pool of healing power that replenishes when you take a long rest. As an action, you can touch a creature and draw power from the pool to restore a number of hit points to that creature, up to the maximum amount remaining in your pool.\n\nAlternatively, you can expend 5 hit points from your pool of healing to cure the target of one disease or neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single use of Lay on Hands, expending hit points separately for each one.\n\nThis feature has no effect on undead and constructs.")
    if crusader>=3:
        ch.create_cc(name="Channel Divinity",minVal=0,maxVal=1,reset="short",dispType="hex",desc="Your devotion allows you to channel divine energy to fuel magical effects. Each Channel Divinity option provided by your devotion explains how to use it.\n\nWhen you use your Channel Divinity, you choose which option to use. You must then finish a short or long rest to use your Channel Divinity again.")
    if crusader>=14:
        ch.create_cc(name="Cleansing Touch",minVal=0,maxVal=max(charismaMod,1),reset="long",dispType="hex",desc="You can use your action to end one spell on yourself or on one willing creature that you touch.\n\nYou can use this feature a number of times equal to your Personality modifier (a minimum of once). You regain expended uses when you finish a long rest.")
if mage>=1:
    ch.create_cc(name="Focus Points",minVal=0,maxVal=2 if mage<=2 else 3 if mage<=4 else 4 if mage<=6 else 5 if mage<=8 else 6 if mage<=10 else 7 if mage<=12 else 8 if mage<=14 else 9 if mage<=16 else 10 if mage<=18 else 11 if mage==19 else 12,reset="long",dispType="bubble",desc="You have focus points, and you gain more as you reach higher levels, as shown in the Focus Points column of the Mage table. You can never have more focus points than shown on the table for your level. You regain all spent focus points when finish a long rest.")
    if mage==20:
        ch.create_cc(name="Signature Spells",minVal=0,maxVal=2,reset="short",dispType="bubble",desc="Choose two 3rd level spells that you know as your signature spells. You can cast each spell once without expending any magicka. When you do so, you can't do so again until you finish a short or long rest.")
if monk>=1:
    if monk>=2:
        ch.create_cc(name="Stamina",minVal=0,maxVal=MonkLevel,reset="short",desc="Your training allows you to harness the energy of stamina. Your access to this energy is represented by a number of stamina points. Your monk level determines the number of points you have, as shown in the Stamina Points column of the Monk table.\n\nYou can spend these points to fuel various stamina features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more stamina features as you gain levels in this class.\n\nWhen you spend a stamina point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended stamina back into yourself. You must spend at least 30 minutes of the rest meditating to regain your stamina points.\n\nSome of your stamina features require your target to make a saving throw to resist the feature's effects. The saving throw DC is calculated as follows:\n\nStamina save DC = 8 + your proficiency bonus + your Willpower modifier")
if necromancer>=1:
    if necromancer>=2:
        ch.create_cc(name="Soul Points",minVal=0,maxVal=max(intelligenceMod,0),reset="long",dispType="hex",desc="Once per turn, when a creature with a Challenge Rating of 1 or higher dies within 30 feet of you, you gain one Soul Point. You can collect a maximum amount of Soul Points equal to your Intelligence modifier.\n\nAs an action on your turn, you can expend one or more Soul Points to regain 1d8 hit points for each Soul Point used.")
    if necromancer==20:
        ch.create_cc(name="Reanimate",minVal=0,maxVal=1,reset="long",dispType="hex",desc="When an ally that you can see dies, you can use your reaction to return their soul back to their bodies and undo any damage dealt to them from their killing blow. The ally is returned to life with 1 hit point.\n\nAdditionally, you can expend Soul Points as part of this reaction to restore an additional amount of hit points to the ally equal to 1d6 for each Soul Point used. Once you use this feature, you can't use it again until you finish a long rest.")
if nightblade>=1:
    ch.create_cc(name="Nightblade Magicka",minVal=0,maxVal=2 if nightblade==1 else 4 if nightblade==2 else 7 if nightblade==3 else 9 if nightblade==4 else 14 if nightblade==5 else 17 if nightblade==6 else 23 if nightblade==7 else 24 if nightblade==8 else 26 if nightblade==9 else 32 if nightblade==10 else 33 if nightblade==11 else 34 if nightblade==12 else 35 if nightblade==13 else 36 if nightblade==14 else 37 if nightblade==15 else 38 if nightblade==16 else 39 if nightblade==17 else 40 if nightblade==18 else 41 if nightblade==19 else 42,reset="short",desc="The Nightblade table shows how much magicka you have to cast your nightblade spells of 1st level and higher. The table also shows what the level spells you can cast. To cast one of your nightblade spells of 1st level or higher, you must expend magicka, as noted in the spell's description and the Magicka Cost table found in chapter 10 of the Basic Rules. You regain all expended magicka when you finish a short or long rest.")
    if nightblade>=11:
        ch.create_cc(name="Night Magic, 6th Level Spell",minVal=0,maxVal=1,reset="long",dispType="bubble",desc="At 11th level, your continued research in the esoteric studies of shadow magic has unlocked an arcane secret known as night magic. Choose one 6th-level spell from the nightblade spell list. You can cast this unique spell once without expending any magicka. You must finish a long rest before you can do so again.")
    if nightblade>=13:
        ch.create_cc(name="Night Magic, 7th Level Spell",minVal=0,maxVal=1,reset="long",dispType="bubble",desc="At higher levels, you gain more nightblade spells of your choice that can be cast in this way: one 7th-level spell at 13th level. You can cast this unique spell once without expending any magicka. You regain all uses of your Night Magic spells when you finish a long rest.")
    if nightblade>=15:
        ch.create_cc(name="Night Magic, 8th Level Spell",minVal=0,maxVal=1,reset="long",dispType="bubble",desc="At higher levels, you gain more nightblade spells of your choice that can be cast in this way: one 8th-level spell at 15th level. You can cast this unique spell once without expending any magicka. You regain all uses of your Night Magic spells when you finish a long rest.")
    if nightblade>=17:
        ch.create_cc(name="Night Magic, 9th Level Spell",minVal=0,maxVal=1,reset="long",dispType="bubble",desc="At higher levels, you gain more nightblade spells of your choice that can be cast in this way: one 9th-level spell at 17th level. You can cast this unique spell once without expending any magicka. You regain all uses of your Night Magic spells when you finish a long rest.")
    if nightblade>=18:
        ch.create_cc(name="Spell Thief",minVal=0,maxVal=1,reset="long",dispType="bubble",desc="Immediately after a creature casts a spell on you, or if you are within it's area of affect, you can use your reaction to force the creature to make a saving throw with it's spellcasting attribute. The DC equals your spell save DC. On a failed save, you negate the spell effect against you, and you steal the knowledge of the spell if it is at least 1st level and of a level that you can cast (it doesn't need to be a nightblade spell). For the next 8 hours, you know the spell and can cast it, using magicka as normal. The creature can't cast that spell until 8 hours have passed.\n\nOnce you use this feature, you can't use it again until you finish a long rest.")
    if nightblade==20:
        ch.create_cc(name="Shade",minVal=0,maxVal=1,reset="long",dispType="hex",desc="As a bonus action on your turn, you can summon a shadowy version of yourself which appears from your shadow. This creature shares all of your statistics, including your current hit points, and is wearing the same equipment as you. The shade can communicate with you telepathically, knows everything that you know, and shares your alignment, background, and motivations. The shade disappears when it drops to 0 hit points, or you use a bonus action to dismiss it back to the shadow realm.\n\nAs a part of your turn, you can direct the shade to move a distance equal to your speed. You can also direct the shade to make one weapon attack.\n\nAdditionally, as a bonus action on your turn, you can swap places with your shade, as long as you are within 60 feet of each other. Once you use this feature, you must finish a long rest before you can use it again.")
if priest>=1:
    if priest>=2:
        ch.create_cc(name="Channel Divinity",minVal=0,maxVal=1 if priest<=5 else 2 if priest<=17 else 3,reset="short",dispType="hex",desc="You gain the ability to channel divine energy directly from your deity, using that energy to fuel magical effects. You start with three such effects: Turn Undead and an effect determined by your calling. Some callings grant you additional effects as you advance in levels, as noted in the calling description.\n\nWhen you use your Channel Divinity, you choose which effect to create. You must then finish a short or long rest to use your Channel Divinity again.\n\nSome Channel Divinity effects require saving throws. When you use such an effect from this class, the DC equals your priest spell save DC.\n\nBeginning at 6th level, you can use your Channel Divinity twice between rests, and beginning at 18th level, you can use it three times between rests. When you finish a short or long rest, you regain your expended uses.")
    if priest>=10:
        ch.create_cc(name="Divine Intervention",minVal=0,maxVal=1,reset="long",dispType="hex",desc="You can call on your deity to intervene on your behalf when your need is great.\n\nImploring your deity’s aid requires you to use your action. Describe the assistance you seek, and roll percentile dice. If you roll a number equal to or lower than your priest level, your deity intervenes. The GM chooses the nature of the intervention; the effect of any priest spell or priest calling spell would be appropriate.\n\nIf your deity intervenes, you can’t use this feature again for 7 days. Otherwise, you can use it again after you finish a long rest.\n\nAt 20th level, your call for intervention succeeds automatically, no roll required.")
if ranger>=1:
    if ranger>=3:
        ch.create_cc(name="Primeval Sense",minVal=0,maxVal=1,reset="long",dispType="hex",desc="You can use an action to attune your senses to determine if any of your favored enemies lurk nearby. For 1 minute, you can sense whether any of your favored enemies are present within 1 mile of you (or within up to 6 miles if you are in your favored terrain). This feature reveals which of your favored enemies are present, their numbers, and the creatures’ general direction and distance (in miles) from you. If there are multiple groups of your favored enemies within range, you learn this information for each group.\n\nAny favored enemy within 30 feet of you has a faint outline surrounding it, which is only visible to you. The outline is visible through most barriers, but it is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.\n\nOnce you use this feature, you can’t do so again until you finish a long rest.")
    if ranger>=17:
        ch.create_cc(name="Primal Connection",minVal=0,maxVal=1,reset="long",dispType="hex",desc="If you spend 1 minute in uninterrupted meditation while outdoors, you gain knowledge of the land within 3 miles of you. In caves and other natural underground settings, the radius is limited to 300 feet. You don't gain this knowledge in areas where nature has been replaced by construction, such as dungeons and towns.\n\nYou instantly gain knowledge of up to three facts of your choice about any of the following subjects as they relate to the area:\n- terrain and bodies of water\n- prevalent plants, minerals, animals, or peoples\n- powerful beasts, fey, fiends, elementals, or undead\n- influence from other planes of existence\n- buildings\n\nFor example, you could determine the location of powerful undead in the area, the location of major sources of safe drinking water, and the location of any nearby towns.\n\nOnce you use this feature, you can’t use it again until you finish a long rest.")
if rogue>=1:
    if rogue>=20:
        ch.create_cc(name="Stroke of Luck",minVal=0,maxVal=1,reset="short",dispType="hex",desc="You have an uncanny knack for succeeding when you need to. If your attack misses a target within range, you can turn the miss into a hit. Alternatively, if you fail an ability check, you can treat the d20 roll as a 20.\n\nOnce you use this feature, you can't use it again until you finish a short or long rest.")
if sorcerer>=1:
    sorcMagicka=4 if sorcerer==1 else 6 if sorcerer==2 else 14 if sorcerer==3 else 17 if sorcerer==4 else 27 if sorcerer==5 else 32 if sorcerer==6 else 38 if sorcerer==7 else 44 if sorcerer==8 else 57 if sorcerer==9 else 64 if sorcerer==10 else 73 if sorcerer==11 else 73 if sorcerer==12 else 83 if sorcerer==13 else 83 if sorcerer==14 else 94 if sorcerer==15 else 94 if sorcerer==16 else 107 if sorcerer==17 else 114 if sorcerer==18 else 123 if sorcerer==19 else 133
    ch.create_cc(name="Bonus Sorcery Magicka",minVal=0,maxVal=1 if sorcerer==1 else 2 if sorcerer==2 else 3 if sorcerer==3 else 4 if sorcerer==4 else 5 if sorcerer==5 else 8 if sorcerer==6 else 9 if sorcerer==7 else 11 if sorcerer==8 else 14 if sorcerer==9 else 16 if sorcerer==10 else 18 if sorcerer<=12 else 20 if sorcerer<=14 else 23 if sorcerer<=16 else 26 if sorcerer==17 else 28 if sorcerer==18 else 30 if sorcerer==19 else 33,reset="none",desc="Sorcerer's have access to a large pool of magicka, but their natural gift is stunted by reduced regeneration.\n\nUnlike other spellcasters, sorcerer's do not regain all of their magicka at the end of a long rest. Instead, you only regain half of your expended magicka, rounding up (minimum of 1).")
    if sorcerer>=3:
        ch.create_cc(name="Power Overwhelming",minVal=0,maxVal=1,reset="long",dispType="bubble",desc="When you cast a spell that you know, you can choose to cast it at a spell level one higher than your current maximum, using magicka as normal (maximum of 9th level). Once you cast a spell in this way, you must finish a long rest before you can do so again.")
    if sorcerer>=17:
        ch.create_cc(name="Power Overwhelming, 6th Level Spell",minVal=0,maxVal=1,reset="long",dispType="bubble",desc="When you reach 17th level, you can cast 1 additional 6th level spel using magicka as normal.")
    if sorcerer>=19:
        ch.create_cc(name="Power Overwhelming, 7th Level Spell",minVal=0,maxVal=1,reset="long",dispType="bubble",desc="When you reach 19th level, you can cast 1 additional 7th level spell, using magicka as normal.")
    if sorcerer>=10:
        ch.create_cc(name="Equilibrium",minVal=0,maxVal=1,reset="long",dispType="hex",desc="You can choose to impose one of the following effects:\n- As a bonus action, you can expend up to half of your available sorcerer Hit Dice. You restore magicka points equal to half of the total rolled on the Hit Dice.\n- During a short rest, you can spend magicka points, as though you were casting a spell, to restore an amount of sorcerer Hit Dice equal to the spell level cast.\n\nOnce you use this feature, you must complete a long rest before you can do so again.")
    if sorcerer==20:
        ch.create_cc(name="Sorcerous Restoration",minVal=0,maxVal=1,reset="long",dispType="bubble",desc="You can spend 1 minute meditating to regain half of your expended magicka, rounding up. Once you regain magicka with this feature, you must finish a long rest before you can do so again.")
if spellsword>=1:
    if spellsword>=15:
        ch.create_cc(name="Arcane Might",minVal=0,maxVal=1,reset="short",dispType="hex",desc="When you make a Strength, Agility, or Endurance attribute check, you can add your Intelligence modifier to the roll.\n\nOnce you use this feature, you can't use it again until you finish a short or long rest.")
if thief>=1:
    pass
if warden>=1:
    if warden>=2:
        ch.create_cc(name="Mark of Balance",minVal=0,maxVal=2,reset="short",dispType="hex",desc="You gain a supernatural connection with the circle of nature, which requires a balance between life and death. As a bonus action you can mark a creature as either an Ally or an Enemy. A marked creature gains certain benefits. Your mark may gain additional effects determined by your conclave.\n\nYou can use this feature twice. You regain expended uses when you finish a short or long rest.\n\nThe mark lasts for 1 hour, unless you use a bonus action to end it, or if you fall unconscious. As a bonus action, you can move the Mark of Balance to another creature and choose to mark them as an Ally or Enemy.")
    if warden>=18:
        ch.create_cc(name="Mark of Harmony",minVal=0,maxVal=1,reset="long",dispType="hex",desc="When you use your Mark of Balance feature, you can also choose any number of creatures that you can see within 60 feet of you and mark them as either an Ally or an Enemy. Creatures marked in this way remain marked for 1 minute, or until you are knocked unconscious.\n\nOnce you use this feature, you must finish a long rest before you can do so again.")
if warrior>=1:
    ch.create_cc(name="Second Wind",minVal=0,maxVal=1,reset="short",dispType="square",desc="You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your warrior level. Once you use this feature, you must finish a short or long rest before you can use it again.")
    if warrior>=2:
        ch.create_cc(name="Action Surge",minVal=0,maxVal=1 if warrior<=16 else 2,reset="short",dispType="hex",desc="Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action on top of your regular action and a possible bonus action.\n\nOnce you use this feature you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn.")
    if warrior>=9:
        ch.create_cc(name="Indomitable",minVal=0,maxVal=1 if warrior<=12 else 2 if warrior<=16 else 3,reset="short",dispType="hex",desc="Beginning at 9th level, you can reroll a saving throw you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest. \n\nYou can use this feature twice between long rests starting at 13th level and three times between longs rests beginning at 17th level.")

caster=0
fullCaster=0
halfCaster=0
subCaster=0
full=0
half=0
subs=0
castersFull=["Bard","Mage","Necromancer","Priest","Sorcerer","Warden"]
castersHalf=["Crusader","Spellsword"]
castersSub=["Ranger","Thief"]
for cls, lvl in ch.levels:
    cls_info=classes.get(cls, {})
    sub=currentSubclasses.get(f"{cls}Level")
    size=cls_info.get("hit_die", 0)
    if not hit_dice.get(size):
        hit_dice[size]={'str': "", 'int': 0}
    if size:
        if not f"{cls}Level" in hit_dice[size].get('str'):
            hit_dice[size]['str']+=f"+{cls}Level"
            hit_dice[size]['int']+=lvl
    if lvl >= cls_info.get('sub_level', 21) and not sub:
        note_out.append(f"""You're missing a subclass for {cls}. Use `{ctx.prefix+ctx.alias} level "{cls}" [sub name]` to set it.""")
    sub_out.append(f"{cls} {f'({sub})' if sub else ''}: {lvl}")
    if cls in castersFull:
        fullCaster+=lvl
        full+=1
    if cls in castersHalf:
        halfCaster+=lvl
        half+=1
    if cls in castersSub:
        if sub:
            if "green pact" or "twilight shroud" in sub.lower():
                subCaster+=lvl
                subs+=1
    counters=cls_info.get("counters",[])
    for counter in counters:
        if sub:
            i=0
            while i<len(counters):
                if counters[i].subclass in sub:
                    if lvl>=counters[i].level:
                        ch.create_cc_nx(name=counters[i].name,minVal=0,maxVal=counters[i].maxValue[lvl-counters[i].level] if typeof(counters[i].maxValue)=='SafeList' else counters[i].maxValue,reset=counters[i].reset,dispType=counters[i].display,desc=counters[i].desc)
                        if ch.get_cc_max(counters[i].name)!= counters[i].maxValue[lvl-counters[i].level] if typeof(counters[i].maxValue)=='SafeList' else counters[i].maxValue:
                            ch.edit_cc(counters[i].name,maxVal=counters[i].maxValue[lvl-counters[i].level] if typeof(counters[i].maxValue)=='SafeList' else counters[i].maxValue)
                i+=1
for size, num in hit_dice.items():
    cc_name = f"Hit Dice (d{size})"
    cc = ch.create_cc_nx(cc_name, minVal=0, maxVal=num.int, reset=None)
    if ch.get_cc_max(cc_name)!=num.int:
        ch.edit_cc(cc_name, maxVal=num.int)
    dice_out.append(f"""{num.int}d{size}""")
caster+=fullCaster+(halfCaster//2)+(subCaster//3)
if caster!=0:
    if fullCaster!=0:
        maximum=4 if caster==1 else 6 if caster==2 else 14 if caster==3 else 17 if caster==4 else 27 if caster==5 else 32 if caster==6 else 38 if caster==7 else 44 if caster==8 else 57 if caster==9 else 64 if caster==10 else 73 if caster==11 else 73 if caster==12 else 83 if caster==13 else 83 if caster==14 else 94 if caster==15 else 94 if caster==16 else 107 if caster==17 else 114 if caster==18 else 123 if caster==19 else 133
        if sorcerer>=1:
            ch.create_cc(name="Magicka",minVal=0,maxVal=maximum,reset="none",desc="Your Class table shows how much magicka you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend magicka, as noted in the spell's description and the Magicka Cost table found in chapter 10 of the Basic Rules. You regain all expended magicka when you finish a long rest.",initial_value=maximum)
            maxMagicka=ch.get_cc_max("Magicka")
            normalRestore=maxMagicka-sorcMagicka
            note_out.append(f"""You're a Sorcerer, be aware of your Stunted Magicka Feature. {sorcMagicka} points in your Magicka pool recover at a slower rate. You can recover Magicka up to {normalRestore} from other sources on a long rest. Any Sorcerer Magicka can be restored through the `!essorcerer` alias""")
        else:
            ch.create_cc(name="Magicka",minVal=0,maxVal=maximum,reset="long",desc="Your Class table shows how much magicka you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend magicka, as noted in the spell's description and the Magicka Cost table found in chapter 10 of the Basic Rules. You regain all expended magicka when you finish a long rest.")
    elif halfCaster!=0:
        if half>0 and half>=2:
            ch.create_cc(name="Magicka",minVal=0,maxVal=4 if caster==1 else 6 if caster==2 else 14 if caster==3 else 17 if caster==4 else 27 if caster==5 else 32 if caster==6 else 38 if caster==7 else 44 if caster==8 else 57 if caster==9 else 64 if caster==10 else 73 if caster==11 else 73 if caster==12 else 83 if caster==13 else 83 if caster==14 else 94 if caster==15 else 94 if caster==16 else 107 if caster==17 else 114 if caster==18 else 123 if caster==19 else 133,reset="long",desc="Your Class table shows how much magicka you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend magicka, as noted in the spell's description and the Magicka Cost table found in chapter 10 of the Basic Rules. You regain all expended magicka when you finish a long rest.")
        elif half>0 and subs>0:
            ch.create_cc(name="Magicka",minVal=0,maxVal=4 if caster==1 else 6 if caster==2 else 14 if caster==3 else 17 if caster==4 else 27 if caster==5 else 32 if caster==6 else 38 if caster==7 else 44 if caster==8 else 57 if caster==9 else 64 if caster==10 else 73 if caster==11 else 73 if caster==12 else 83 if caster==13 else 83 if caster==14 else 94 if caster==15 else 94 if caster==16 else 107 if caster==17 else 114 if caster==18 else 123 if caster==19 else 133,reset="long",desc="Your Class table shows how much magicka you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend magicka, as noted in the spell's description and the Magicka Cost table found in chapter 10 of the Basic Rules. You regain all expended magicka when you finish a long rest.")
        else:
            ch.create_cc(name="Magicka",minVal=0,maxVal=4 if halfCaster==2 else 6 if halfCaster==3 else 10 if halfCaster==4 else 14 if halfCaster==5 else 15 if halfCaster==6 else 17 if halfCaster==7 else 19 if halfCaster==8 else 22 if halfCaster==9 else 27 if halfCaster==10 else 30 if halfCaster==11 else 35 if halfCaster==12 else 38 if halfCaster==13 else 40 if halfCaster==14 else 44 if halfCaster==15 else 50 if halfCaster==16 else 57 if halfCaster==17 else 60 if halfCaster==18 else 64 if halfCaster==19 else 64,reset="long",desc="Your Class table shows how much magicka you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend magicka, as noted in the spell's description and the Magicka Cost table found in chapter 10 of the Basic Rules. You regain all expended magicka when you finish a long rest.")
    elif subCaster!=0:
        if subs>0 and subs>=2:
            ch.create_cc(name="Magicka",minVal=0,maxVal=4 if caster==1 else 6 if caster==2 else 14 if caster==3 else 17 if caster==4 else 27 if caster==5 else 32 if caster==6 else 38 if caster==7 else 44 if caster==8 else 57 if caster==9 else 64 if caster==10 else 73 if caster==11 else 73 if caster==12 else 83 if caster==13 else 83 if caster==14 else 94 if caster==15 else 94 if caster==16 else 107 if caster==17 else 114 if caster==18 else 123 if caster==19 else 133,reset="long",desc="Your Class table shows how much magicka you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend magicka, as noted in the spell's description and the Magicka Cost table found in chapter 10 of the Basic Rules. You regain all expended magicka when you finish a long rest.")
        else:
            ch.create_cc(name="Magicka",minVal=0,maxVal=4 if subCaster==3 else 6 if subCaster<=6 else 14 if subCaster<=8 else 17 if subCaster<=12 else 27 if subCaster<=15 else 32 if subCaster<=18 else 38,reset="long",desc="Your Class table shows how much magicka you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend magicka, as noted in the spell's description and the Magicka Cost table found in chapter 10 of the Basic Rules. You regain all expended magicka when you finish a long rest.")
createdCounters=''
for newcounter in ch.consumables:
    if newcounter.name not in prevCounters and "Hit Dice" not in newcounter.name:
        newCounters.append(f"{newcounter.name}: {ch.cc_str(newcounter.name)}")
if newCounters!=[]:
    createdCounters=f'''-f "Counters Created|{n.join(newCounters)}" '''
out=[f""" -title "Level Summary for {name}:" -f "Total Level|{total}" """]
out.append(f""" -f "Hit Dice|{n.join(dice_out)}|inline" """)
out.append(f""" -f "Class Levels|{n.join(sub_out)}|inline"   """)
if note_out:
  out.append(f""" -f 《Notes|{n.join(note_out)}》 """)
out.append(f"""{createdCounters}""")
return n.join(out)
</drac2>
