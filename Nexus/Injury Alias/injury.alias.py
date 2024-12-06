embed <drac2>
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
cc="Exhaustion"
desc1="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
(character().create_cc_nx(cc, 0, 6, None, "bubble", 0, desc=desc1, initial_value=0))
G=get_gvar("da720c77-ed4b-47b7-b5b0-b76ba40d27d9")
L=G.split("\n")
I=L.pop(roll(f'1d{len(L)}-1')).title()
a=argparse(&ARGS&)
i=a.get('i')
myBags=bag.load_bags()
if not i:
    character().mod_cc(cc, +1)
    injury_bag, *_=bag.modify_item(myBags, item=f'{I}',quantity=1,bag_name="Injuries",create_on_fail=True)
    bag.save_bags(myBags)
    injured, *_=bag.display_bag(injury_bag)
    mod=f''' -f "{cc}|{character().cc_str(cc)+' (+1)'}" -f "Effect|Each time you gain a permanent Injury, you also gain a level of exhaustion. This exhaustion is permanent for as long as your wound is open and untreated." {" ".join(injured)} '''
else:
    mod=f''' -f "Update your Injuries| Please correct your 'Injuries' bag with the correct injury based on this result, use `!qb 'Injuries' '{I}'` to add the new injury and `!qb 'Injuries' -<old injury>` to clear the previous.*Replace `<old injury>` with the actual name in the bag.*" '''
return f''' -title "{name} is unfortunate enough to {I}!" {mod} '''
</drac2>
-thumb https://media.discordapp.net/attachments/879551881557454859/1125520184711581847/DeanSpencer-filler-prostheticleg.png
