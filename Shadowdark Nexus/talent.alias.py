embed <drac2>
ch=character()
arg=&ARGS&
parseargs=argparse(arg)
value=parseargs.get('n',1,int)
melee=int(ch.get_cvar('meleeCheck',0))
ranged=int(ch.get_cvar('rangedCheck',0))
spell=int(ch.get_cvar('spellCheck',0))
bonuses=['melee','ranged','spell']
for args in arg:
    if args in bonuses[0]:
        melee+=value
    if args in bonuses[1]:
        ranged+=value
    if args in bonuses[2]:
        spell+=value
ch.set_cvar('meleeCheck',melee)
ch.set_cvar('rangedCheck',ranged)
ch.set_cvar('spellCheck',spell)
</drac2>