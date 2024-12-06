embed <drac2>
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
cc="Exhaustion"
desc1="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
(character().create_cc_nx(cc, 0, 6, None,"bubble", 0, desc=desc1, initial_value=0))
G=get_gvar("821e4798-b5a9-4b36-b2d7-f2588b39b014")
L=G.split("\n")
I=L.pop(roll(f'1d{len(L)}-1')).title()
myBags=bag.load_bags()
character().mod_cc(cc, +1)
wounds_bag, *_=bag.modify_item(myBags, item="Open Wound",quantity=1,bag_name="Wounds",create_on_fail=True)
bag.save_bags(myBags)
wounded, *_=bag.display_bag(wounds_bag)
mod=f''' -f "{cc}|{character().cc_str(cc)+' (+1)'}" -f "Effect|Each time you gain an open wound, you also gain a level of exhaustion. This exhaustion is permanent for as long as your wound is open and untreated." {" ".join(wounded)} '''
return f''' -title "{name} suffers an open wound on {I}!" {mod} '''
</drac2> -thumb https://media.discordapp.net/attachments/879551881557454859/1125513078914695209/1194318-women-artwork-ArtStation-fantasy-art-fantasy-girl.png?width=422&height=597
