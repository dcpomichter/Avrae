embed <drac2>
c, ch, arg=combat(), character(), &ARGS&
args=argparse(arg)
stats=['strength','dexterity','constitution','intelligence','wisdom','charisma']
checks=['melee','ranged','spellcasting']
properties=['thrown','finesse']
wisCaster=['priest','seer','druid']
intCaster=['wizard']
chaCaster=['bard','knight of st ydris','witch',]
adv=args.adv()
misc=args.last('b',0,int)
checkDc=args.last('dc',0,int)
mastery=args.get('mastery')
if mastery:
    misc+=1+ch.levels.total_level//2
stat=''
props=' '
bonus=0
if c:
    cb=c.get_combatant(ch.name)
else:
    cb=ch.name
exhaustedStats=[]
if c:
    for option in stats:
        if cb.get_effect(f'Exhaustion ({option.title()})'):
            exhaustedStats.append(option)
if arg:
    for stat in stats:
        if arg[0].lower() in stat:
            bonus=ch.stats.get_mod(stat)
            for options in exhaustedStats:
                if stat in options:
                    if adv!=-1:
                        adv-=1
            stat=stat.title()
            break
        else:
            stat=''
    for check in checks:
        if arg[0].lower() in check:
            if check==checks[0]:
                for args in arg:
                    if args in properties[1]:
                        bonus=max(ch.stats.get_mod(stats[0]),ch.stats.get_mod(stats[1]))
                        props=f''' {properties[1]} '''
                        break
                    else:
                        bonus=ch.stats.get_mod(stats[0])
                if props!=' ':
                    if ch.stats.get_mod(stats[1])>ch.stats.get_mod(stats[0]):
                            for options in exhaustedStats:
                                if stats[1] in options:
                                    if adv!=-1:
                                        adv-=1
                    else:
                        for options in exhaustedStats:
                            if stats[0] in options:
                                if adv!=-1:
                                    adv-=1
                else:
                    for options in exhaustedStats:
                        if stats[0] in options:
                            if adv!=-1:
                                adv-=1
                talents=int(ch.get_cvar('meleeCheck', 0))
                bonus+=talents
                stat=check.title()
                break
            if check==checks[1]:
                for args in arg:
                    if args in properties[0]:
                        bonus=max(ch.stats.get_mod(stats[0]),ch.stats.get_mod(stats[1]))
                        props=f''' {properties[0]} '''
                        break
                    else:
                        bonus=ch.stats.get_mod(stats[1])
                if props!=' ':
                    if ch.stats.get_mod(stats[0])>ch.stats.get_mod(stats[1]):
                            for options in exhaustedStats:
                                if stats[0] in options:
                                    if adv!=-1:
                                        adv-=1
                    else:
                        for options in exhaustedStats:
                            if stats[1] in options:
                                if adv!=-1:
                                    adv-=1
                else:
                    for options in exhaustedStats:
                        if stats[1] in options:
                            if adv!=-1:
                                adv-=1
                talents=int(ch.get_cvar('rangedCheck', 0))
                bonus+=talents
                stat=check.title()
                break
            if check==checks[2]:
                for caster in wisCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus=ch.stats.get_mod(stats[4])
                        for options in exhaustedStats:
                            if stats[4] in options:
                                if adv!=-1:
                                    adv-=1
                        props=f''' {caster.title()} '''
                        break
                for caster in intCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus=ch.stats.get_mod(stats[3])
                        for options in exhaustedStats:
                            if stats[3] in options:
                                if adv!=-1:
                                    adv-=1
                        props=f''' {caster.title()} '''
                        break
                for caster in chaCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus=ch.get_mod(stats[5])
                        for options in exhaustedStats:
                            if stats[5] in options:
                                if adv!=-1:
                                    adv-=1
                        props=f''' {caster.title()} '''
                        break
                talents=int(ch.get_cvar('spellCheck', 0))
                bonus+=talents
                stat=check.title()
                break
bonus+=misc
dice=['1d20','2d20kh1','2d20kl1'][adv]
check=vroll(f'''{dice}+{bonus}''')
difficulty=''
text=f''' -title "{name} makes a{props}{stat} check!" -f "{check}" '''
if checkDc>0:
    difficulty=f''' -f "DC|{checkDc}" '''
    if check.total>=checkDc:
        text=f''' -title "{name} makes a{props}{stat} check!" {difficulty} -f "{check} **(Success)**" '''
    else:
        text=f''' -title "{name} makes a{props}{stat} check!" {difficulty} -f "{check} **(Failure)**" '''
return text
</drac2> -thumb {{image}} -footer "{{ctx.prefix}}{{ctx.alias}} [stat/action] [adv/dis] [-b] [args]|created by @dcpomichter"
