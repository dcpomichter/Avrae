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
stat=''
bonus=0
if arg:
    for stat in stats:
        if arg[0].lower() in stat:
            bonus=ch.stats.get_mod(stat)
            stat=stat.title()
            break
    for check in checks:
        if arg[0].lower() in check:
            if check==checks[0]:
                for args in arg:
                    if args in properties[1]:
                        bonus=ch.stats.get_mod(max(stats[0],stats[1]))
                        break
                    else:
                        bonus=ch.stats.get_mod(stats[0])
                stat=check.title()
                break
            if check==checks[1]:
                for args in arg:
                    if args in properties[0]:
                        bonus=ch.stats.get_mod(max(stats[0],stats[1]))
                        break
                    else:
                        bonus=ch.stats.get_mod(stats[1])
                stat=check.title()
                break
            if check==checks[2]:
                for caster in wisCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus=ch.stats.get_mod(stats[4])
                for caster in intCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus=ch.stats.get_mod(stats[3])
                for caster in chaCaster:
                    if caster in ch.get_cvar('class').lower():
                        bonus=ch.get_mod(stats[5])
                stat=check.title()
                break
if misc>0:
    bonus=f'''{bonus}+{misc}'''
dice=['1d20','2d20kh1','2d20kl1'][adv]
check=vroll(f'''{dice}+{bonus}''')
text=f''' -title "{name} makes a {stat} check!" -f "{check}" '''
return text
</drac2>
