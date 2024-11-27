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
adv=arg.adv()
misc=arg.last('-b',0)
stat=''
bonus=0
if arg:
    for stat in stats:
        if arg[0].lower() in stat:
            bonus+=ch.stats.get(stat)
            stat=stat.title()
            break
    for check in checks:
        if arg[0].lower() in checks:
            if check==checks[0]:
                if args.get(properties[1]):
                    bonus+=ch.stats.get_mod(max(stats[0],stats[1]))
                else:
                    bonus+=ch.stats.get_mod(stats[0])
                stat=check.title()
                break
            if check==checks[1]:
                if args.get(properties[0]):
                    bonus+=ch.stats.get_mod(max(stats[0],stats[1]))
                else:
                    bonus+=ch.stats.get_mod(stats[1])
                stat=check.title()
                break
            if check==checks[2]:
                for caster in wisCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus+=ch.stats.get_mod(stats[4])
                for caster in intCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus+=ch.stats.get_mod(stats[3])
                for caster in chaCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus+=ch.get_mod(stats[5])
                stat=check.title()
                break
bonus+=misc+bonus
check=vroll(1d20+bonus)
text=f''' -title "{name} makes a {stat} check!" -f "{check}" '''
return text
</drac2>
