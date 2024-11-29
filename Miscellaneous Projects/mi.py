-f "Magical Inspiration|If a creature has a Bardic Inspiration die from you and casts a spell that restores hit points or deals damage, the creature can roll that die and choose a target affected by the spell. Add the number rolled as a bonus to the hit points regained or the damage dealt. The Bardic Inspiration die is then lost"
<drac2>
c=combat()
ch=character()
args=argparse(&ARGS&)
targets=args.get('t')
desc="If you cast a spell that restores hit points or deals damage, you can roll the Bardic Inspiration die and choose a target affected by the spell. Add the number rolled as a bonus to the hit points regained or the damage dealt."
for t in targets:
  if c:
    if cmbt:=c.get_combatant(t):
        cmbt.add_effect(name="Magical Inspiration", desc=desc, buttons=[{"label": "Use Inspiration","verb": "used their Inspiration","style": 4,"automation":[{"type": "remove_ieffect"}]}])
</drac2>
