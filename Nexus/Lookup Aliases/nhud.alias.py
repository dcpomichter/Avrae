embed <drac2>
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
cc="Hunger"
CC="Thirst"
dd="Fatigue"
DD="Stress"
ee="Hit Dice"
EE="Exhaustion"
ff="Death Saves"
FF="Burnout"
HD_types=[x.name for x in character().consumables if 'Hit Dice' in x.name]
HD_output='\n'.join(f"{x}- {character().cc_str(x)}" for x in HD_types)
dice=[12, 10, 8, 6, 4][character().get_cc(FF)] if character().cc_exists(FF) else ''
hunger=character().get_cc(cc)
thirst=character().get_cc(CC)
fatigue=character().get_cc(dd)
stamina=min(hunger, thirst, fatigue)
dc=0 if stamina==0 else 5 if stamina==1 else 10 if stamina==2 else 15 if stamina==3 else 20 if stamina==4 else 25 if stamina==5 else 30
death=f''' Death Saves- {character().cc_str(ff)} ''' if character().cc_exists(ff) else ''
spell=f''' Burnout- {character().cc_str(FF)}\nBurnout Die- 1d{dice}''' if character().cc_exists(FF) else ''
myBags=bag.load_bags()
injured_bag=bag.get_bag(myBags, bag_id="Injuries",create_on_fail=True)
wound_bag=bag.get_bag(myBags, bag_id="Wounds",create_on_fail=True)
afflict_bag=bag.get_bag(myBags, bag_id="Afflictions",create_on_fail=True)
injured_display, *_=bag.display_bag(injured_bag)
wound_display, *_=bag.display_bag(wound_bag)
afflict_display, *_=bag.display_bag(afflict_bag)
text=f''' -title "{name} checks their current Status." -f "Survival Conditions| Hunger- {character().cc_str(cc)}\nThirst- {character().cc_str(CC)}\nFatigue- {character().cc_str(dd)}" -f "Stamina DC|{dc}" -f "Health|{character().hp_str()}\n{HD_output}\nExhaustion- {character().cc_str(EE)}\n{death}" {" ".join(injured_display)} {" ".join(wound_display)} -f "Mental State|Stress- {character().cc_str(DD)}\n{spell}" {" ".join(afflict_display)} '''
return text
</drac2>
