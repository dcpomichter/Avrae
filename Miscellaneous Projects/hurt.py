embed <drac2>
a=&ARGS&
i=len(a)
n="\n"
targ,damageRoll,damageType,phrase="&1&".lower() if i>0 else None,"&2&".lower() if i>1 else None,"&3&".lower() if i>2 else None,"&4&" if i>3 else None
b=["acid","bludgeoning","cold","fire","force","lightning","necrotic","piercing","poison","psychic","radiant","slashing","thunder"]
c=[z[:2] for z in b]
d=c.index(damageType[:2]) if damageType and damageType[:2] in c else None
magic=''
if damageType and 'ma' in damageType[:2]:
    magic='magical'
    d=c.index(damageType[8:10]) if damageType[8:10] in c else None
e="-phrase" in a
damage=b[d] if d else None
g=combat()
h=g.get_combatant(targ) if g and targ else None
k=damageRoll+f'[{magic} {damage}]' if damageRoll and damageType and damage else damageRoll if damageRoll else None
l=vroll(damageRoll) if damageRoll else None
out=[]
p=' '.join(a[(a.index("-phrase")+1):]) if e else None
m=f''' "{h.name if g else targ.title()} is dealt {damageRoll} {magic} {damage if damage else ''} damage from effect '{p if e else """for some reason"""}'.{'' if h else """ That target wasn't found in the current intiative."""}" ''' if l else None
o="Invalid number or format. Please try again using the format: \n`!hurt <target> <damageroll> <damagetype> [args (optional)]`\n\n__Valid Arguments__\n`-phrase [source of damage]` (sneak attack, drow poison, etc.)\n\n__Valid Damage Types__\n`acid, bludgeoning, cold, fire, force, lightning, necrotic, piercing, poison, psychic, radiant, slashing, thunder`\n`magical` can be added before any damage type to deal magical damage to the target, but the pair must be wrapped in quotes."
q=get_gvar("881b3eaf-696b-420e-8486-5dd659f75800")
desc=f'''-desc {m if k else o if targ else q}'''
out.append(desc)
field=f'''-f "Damage| {h.damage(k).damage if k and h else l.full}" '''
out.append(field)
footer=f'-footer "{h.name}: {h.hp_str()}"' if h and k else ''
out.append(footer)
return n.join(out)
</drac2>
