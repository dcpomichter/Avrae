embed <drac2>
ch=character()
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
myBags=bag.load_bags()
secondBags=bag.save_state(myBags)
JJ="Healer's Kit"
desc16="This kit is a leather pouch containing bandages, salves, and splints. The kit has five uses. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check. In addition while in the Wilds you may expend a charge during a Short Rest to expend hit dice when you are Bloodied. And a charge may be expended to close a Wound."
ch.create_cc_nx(JJ, 0, 5, None, "bubble", desc=desc16, initial_value=5)
a=argparse(&ARGS&)
n=0
maximum=ch.get_cc_max(JJ)
healer_bag=bag.find_bag_with_item(secondBags, item="Bandage")
if healer_bag:
    if healer_bag[0]=="Storage":
        bag.swap_pos(secondBags, bag_name="Storage", position=9)
        healer_bag=bag.find_bag_with_item(secondBags, item="Bandage")
kit_bag=bag.find_bag_with_item(secondBags, item="Healer's Kit")
if kit_bag:
    if kit_bag[0]=="Storage":
        bag.swap_pos(secondBags, bag_name="Storage", position=9)
        kit_bag=bag.find_bag_with_item(secondBags, item="Healer's Kit")
healered_bag=bag.find_bag_with_item(myBags, item="Bandage")
if healered_bag:
    if healered_bag[0]=="Storage":
        bag.swap_pos(myBags, bag_name="Storage", position=9)
        healered_bag=bag.find_bag_with_item(myBags, item="Bandage")
kited_bag=bag.find_bag_with_item(myBags, item="Healer's Kit")
if kited_bag:
    if kited_bag[0]=="Storage":
        bag.swap_pos(myBags, bag_name="Storage", position=9)
        kited_bag=bag.find_bag_with_item(myBags, item="Healer's Kit")
healer=''
if healer_bag and healer_bag[0]!="Storage":
    for item_type, amount in healer_bag[1].items():
        while amount:
            value=ch.get_cc(JJ)
            if value<maximum:
                if "Bandage" in item_type:
                    ch.mod_cc(JJ, +1)
                    healered_bag, *_=bag.modify_item(myBags, item="Bandage",quantity=-1,create_on_fail=False,recursive_search=True)
                    n+=+1
            amount-=1
if kit_bag and kit_bag[0]!="Storage":
    for item_type, amount in kit_bag[1].items():
        while amount:
            value=ch.get_cc(JJ)
            if value<maximum:
                if "Healer's Kit" in item_type:
                    ch.set_cc(JJ, maximum)
                    healered_bag, *_=bag.modify_item(myBags, item="Healer's Kit",quantity=-1,create_on_fail=False,recursive_search=True)
                    n+=+(maximum-value)
            amount-=1
bag.save_bags(myBags)
if healered_bag:
    healer, *_=bag.display_bag(healered_bag)
text=f''' -title "{name} refills their supplies." -f "{JJ}|{character().cc_str(JJ)} (+{n})" {" ".join(healer)} '''
return text
</drac2> -thumb {{image}}
