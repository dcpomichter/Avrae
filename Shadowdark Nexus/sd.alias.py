embed <drac2>
ch=character()
arg=&ARGS&
args=argparse(arg)
stats=['strength','dexterity','constitution','intelligence','wisdom','charisma']
checks=['melee','ranged','spellcasting']
properties=['thrown','finesse']
wisCaster=['priest','seer','druid']
intCaster=['wizard']
chaCaster=['bard','knight of st ydris','witch',]
adv=args.adv()
misc=args.last('b',0,int)
DC=args.last('dc',0,int)
mastery=args.get('mastery')
if mastery:
    misc+=1+ch.levels.total_level//2
stat=''
props=' '
bonus=0
if arg:
    for stat in stats:
        if arg[0].lower() in stat:
            bonus=ch.stats.get_mod(stat)
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
                talents=int(ch.get_cvar('rangedCheck', 0))
                bonus+=talents
                stat=check.title()
                break
            if check==checks[2]:
                for caster in wisCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus=ch.stats.get_mod(stats[4])
                        props=f''' {caster.title()} '''
                        break
                for caster in intCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus=ch.stats.get_mod(stats[3])
                        props=f''' {caster.title()} '''
                        break
                for caster in chaCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus=ch.get_mod(stats[5])
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
if DC>0:
    difficulty=f''' -f "DC|{DC}" '''
    if check.total>=DC:
        text=f''' -title "{name} makes a{props}{stat} check!" {difficulty} -f "{check} **(Success)**" '''
    else:
        text=f''' -title "{name} makes a{props}{stat} check!" {difficulty} -f "{check} **(Failure)**" '''
return text
</drac2> -thumb {{image}} -footer "{{ctx.prefix}}{{ctx.alias}} [stat/action] [adv/dis] [-b] [args]|created by @dcpomichter"
