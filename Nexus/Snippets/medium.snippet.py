<drac2>
a=argparse(&ARGS&)
t=a.last('t')
if c:=combat():
  if cmbt:=c.get_combatant(t):
    return f' -d -{cmbt.stats.prof_bonus//2} -f "Medium Armor| While wearing Medium armor reduce any Nonmagical Piercing, Slashing, or Bludgeoning Damage by half of your proficiency Bonus (rounded down), to a minimum of 1" '
</drac2>
