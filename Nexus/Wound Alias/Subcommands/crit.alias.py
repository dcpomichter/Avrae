embed <drac2>
ch=character()
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
cc="Exhaustion"
desc1="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
(ch.create_cc_nx(cc, 0, 6, None,"bubble", 0, desc=desc1, initial_value=0))
a=argparse(&ARGS&)
adv= 2 if "dis" in a else 1 if "adv" in a else 0
dice=['1d20', '2d20kh1', '2d20kl1'][adv]
myBags=bag.load_bags()
secondBags=bag.save_state(myBags)
wounds_bag=bag.get_bag(secondBags, bag_id="Wounds")
wounded_bag=bag.get_bag(myBags, bag_id="Wounds")
HD_types=[x.name for x in ch.consumables if 'Hit Dice' in x.name]
output=''
out=''
exhaust=''
for wound_type, amount in wounds_bag[1].items():
    while amount:
        if wound_type=="Open Wound":
            check=f'1d20 (**1**) = `1`'
            out+=f"\n{check}"
            for hd in HD_types:
                if ch.cc_exists(hd) and ch.get_cc(hd):
                    ch.mod_cc(hd, -1)
                    output+=f"\n{hd}: {ch.cc_str(hd)} (-1)"
                    break
        if wound_type=="Treated Wound":
            check=vroll(f'{dice}')
            out+=f"\n{check}"
            if check.total==1:
                ch.mod_cc(cc, +1)
                exhaust+=f"\n{cc}: {ch.cc_str(cc)} (+1)"
                wounded_bag, *_=bag.modify_item(myBags, item="Treated Wound",quantity=-1,bag_name="Wounds",create_on_fail=False, recursive_search=False)
                wounded_bag, *_=bag.modify_item(myBags, item="Open Wound",quantity=1,bag_name="Wounds",create_on_fail=False, recursive_search=False)
                for hd in HD_types:
                    if ch.cc_exists(hd) and ch.get_cc(hd):
                        ch.mod_cc(hd, -1)
                        output+=f"\n{hd}: {ch.cc_str(hd)} (-1)"
                        break
            elif check.total<=8:
                ch.mod_cc(cc, +1)
                exhaust+=f"\n{cc}: {ch.cc_str(cc)} (+1)"
                wounded_bag, *_=bag.modify_item(myBags, item="Treated Wound",quantity=-1,bag_name="Wounds",create_on_fail=False, recursive_search=False)
                wounded_bag, *_=bag.modify_item(myBags, item="Open Wound",quantity=1,bag_name="Wounds",create_on_fail=False, recursive_search=False)
        amount-=1
bag.save_bags(myBags)
wounded, *_=bag.display_bag(wounded_bag)
return f''' -title "{name} just got Crit with Wounds!" -f "Wound Checks| {" ".join(out)}" -f "Hit Dice|{output}" -f "{exhaust}" {" ".join(wounded)} '''
</drac2> -thumb https://media.discordapp.net/attachments/879551881557454859/1125513078914695209/1194318-women-artwork-ArtStation-fantasy-art-fantasy-girl.png?width=422&height=597
