embed <drac2>
args=argparse(&ARGS&)
targets=args.get('t')
desc="If you're surprised, you can't move or take an action on your first turn of the combat, and you can't take a reaction until that turn ends."
names = ''
for t in targets:
  if c:=combat():
    if cmbt:=c.get_combatant(t):
      names += f"{cmbt.name}\n"
      cmbt.add_effect("Surprised", None, 1, end=True, desc=desc)
text= f''' -title "You are Surprised!" -desc "{desc}" -f "Targets|{names}" '''
return text
</drac2> -thumb {{image}}
