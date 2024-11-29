embed
<drac2>
ch, c, args, n = character(), combat(), &ARGS&, "\n"
cc="Exhaustion"
val, mod, f = 0, "", ""
#Create a Custom Counter for the Active Character if one does not exist
ch.create_cc_nx("Exhaustion", minVal=0, maxVal=6, reset="long", dispType="bubble", reset_by=-1, desc="While you are subjected to the Exhausted Condition you experience the following effects:\n**Levels of Exhaustion.** This Condition is cumulative. Each time you receive it, you gain 1 level of exhaustion. You die if your exhaustion level reaches 6.\n**D20 Tests Affected.** When you make a d20 Test, you subtract 2 times your exhaustion level from the d20 roll.\n**Speed Reduced.** Your Speed is reduced by a number of feet equal to 5 times your Exhaustion level.\n**Ending the Condition.** Finishing a Long Rest removes 1 of your levels of exhaustion. When your exhaustion level reaches 0, you are no longer Exhausted.", initial_value=0)
# Get Exhaustion Value (val) and Sign/Mode (mod)
if "clear" in args:
    mod = "clears their"
else:
    for arg in args:
        if arg.strip("+-").isdigit():
            if "-" in arg:
                mod = "loses"
            else:
                mod = "gains"
            val = int(arg.strip("+-"))
# Get Combatant/Target
args = argparse(args)
t = args.last("t")
if t:
    if c:
        cb = c.get_combatant(t)
    else:
        cb = t
else:
    if c:
        cb = c.get_combatant(ch.name)
    else:
        cb = ch.name
# Help Mode
if not mod and not val:
    # Embed info
    title = "Combat Exhaustion Alias"
    desc = f'Exhaustion is measured in six levels. An Effect can give a creature one or more levels of exhaustion, as specified in the effect’s description. This Condition is cumulative. Each time you receive it, you gain 1 level of exhaustion. You die if your exhaustion level reaches 6.{n}**d20 Rolls Affected.** When you make a d20 Test, you subtract twice your exhaustion level from the d20 roll.{n}**Speed Reduced.** Your Speed is reduced by a number of feet equal to 5 times your Exhaustion level.{n}**Ending the Condition.** Finishing a Long Rest removes 1 of your levels of exhaustion. When your exhaustion level reaches 0, you are no longer Exhausted.'
    # Combatant Status
    if c:
        if exEff:=cb.get_effect("Exhaustion"):
            exLvl = int(exEff.name[12] if len(exEff.name)==14 else exEff.name[12:14])
        elif cb.name == ch.name:
            exLvl = ch.cc(cc).value
        else:
            exLvl = 0
        exDesc= "When you make a d20 Test, you subtract twice your exhaustion level from the d20 roll.\n- Your speed is reduced by 5 times your Exhaustion level"
        exArgs = {"to_hit_bonus":-(int(exLvl*2)),"save_bonus":-(int(exLvl*2)),"check_bonus":-(int(exLvl*2))}
        if cb.get_effect("Exhaustion"):
            cb.remove_effect("Exhaustion")
        cb.add_effect(f'Exhaustion ({exLvl})', desc = exDesc, passive_effects = exArgs)
    else:
        exLvl = ch.cc("Exhaustion").value
# Modify Exhaustion Mode
elif cb:
    # Get Exhaustion Level
    if c:
        if exEff:=cb.get_effect("Exhaustion"):
            exLvl = int(exEff.name[12] if len(exEff.name)==14 else exEff.name[12:14])
        elif cb.name == ch.name:
            exLvl = ch.cc(cc).value
        else:
            exLvl = 0
    else:
        exLvl = ch.cc(cc).value
    # Determine new Exhaustion Level within bounds
    if mod == "gains":
        exLvl += val
    elif mod == "loses":
        exLvl -= val
    elif mod == "clears their":
        exLvl = 0
    exLvl = min(10,max(0,exLvl))
    #Modify Exhaustion Counter
    if c:
        if cb.name == ch.name:
            ch.set_cc(cc,exLvl)
    else:
        if cb == ch.name:
            ch.set_cc(cc,exLvl)
    # Generate and Apply ieffect
    exDesc= "When you make a d20 Test, you subtract twice your exhaustion level from the d20 roll.\n- Your speed is reduced by 5 times your Exhaustion level"
    exArgs = {"to_hit_bonus":-(int(exLvl*2)),"save_bonus":-(int(exLvl*2)),"check_bonus":-(int(exLvl*2))}
    if c:
        if cb.get_effect("Exhaustion"):
            cb.remove_effect("Exhaustion")
        cb.add_effect(f'Exhaustion ({exLvl})', desc = exDesc, passive_effects = exArgs)
    title = f'{cb.name if c else cb} {mod} Exhaustion!'
    desc = " "
# Generate Exhaustion Status if Combatant is found
if cb:
    if c:
        if exEff:=cb.get_effect("Exhaustion"):
            f = f'''-f "{cb.name}'s Exhaustion: **Level {exLvl}**|{exEff.name}: {exEff.desc}" ''' + f
        elif cb.name == ch.name:
            f = f'''-f "{cb.name}'s Exhaustion: **Level {exLvl}**|{ch.cc("Exhaustion").name}: {ch.cc_str("Exhaustion")}:{n} {exDesc}" ''' + f
    else:
        f = f'''-f "{cb}'s Exhaustion: **Level {exLvl}**|Exhaustion {exLvl}:{n} {exDesc}" ''' + f
</drac2>
-title "{{title}}" -desc "{{desc}}" -footer "Usage: {{ctx.prefix}}{{ctx.alias}} [mod] -t [target]" -thumb <image> {{f}}
