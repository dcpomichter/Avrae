<drac2>
a = argparse(&ARGS&)
t = a.last('t')
if c:=combat():
  if cmbt:=c.get_combatant(t):
    return f' -d -{cmbt.stats.prof_bonus} -f "Heavy Armor| While wearing Heavy Armor you reduce Nonmagical Piercing, Slashing, and  Bludgeoning damage by your proficiency bonus, to a minimum of 1." '
</drac2>
