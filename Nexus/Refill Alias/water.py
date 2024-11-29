embed <drac2>
ch=character()
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
myBags=bag.load_bags()
secondBags=bag.save_state(myBags)
dd="Waterskin"
desc3="Holds enough liquid for five drink rations."
ch.create_cc_nx(dd, 0, 5, None, "bubble", desc=desc3, initial_value=5)
a=argparse(&ARGS&)
n=0
maximum=ch.get_cc_max(dd)
water_bag=bag.find_bag_with_item(secondBags, item="Water (Ration)")
if water_bag:
    if water_bag[0]=="Storage":
        bag.swap_pos(secondBags, bag_name="Storage", position=9)
        water_bag=bag.find_bag_with_item(secondBags, item="Water (Ration)")
skin_bag=bag.find_bag_with_item(secondBags, item="Waterskin")
if skin_bag:
    if skin_bag[0]=="Storage":
        bag.swap_pos(secondBags, bag_name="Storage", position=9)
        skin_bag=bag.find_bag_with_item(secondBags, item="Waterskin")
watered_bag=bag.find_bag_with_item(myBags, item="Water (Ration)")
if watered_bag:
    if watered_bag[0]=="Storage":
        bag.swap_pos(myBags, bag_name="Storage", position=9)
        watered_bag=bag.find_bag_with_item(myBags, item="Water (Ration)")
skinned_bag=bag.find_bag_with_item(myBags, item="Waterskin")
if skinned_bag:
    if skinned_bag[0]=="Storage":
        bag.swap_pos(myBags, bag_name="Storage", position=9)
        skinned_bag=bag.find_bag_with_item(myBags, item="Waterskin")
water=''
if water_bag and water_bag[0]!="Storage":
    for item_type, amount in water_bag[1].items():
        while amount:
            value=ch.get_cc(dd)
            if value<maximum:
                if "Water (Ration)" in item_type:
                    ch.mod_cc(dd, +1)
                    watered_bag, *_=bag.modify_item(myBags, item="Water (Ration)",quantity=-1,create_on_fail=False,recursive_search=True)
                    n+=+1
            amount-=1
if skin_bag and skin_bag[0]!="Storage":
    for item_type, amount in skin_bag[1].items():
        while amount:
            value=ch.get_cc(dd)
            if value<maximum:
                if "Waterskin" in item_type:
                    ch.set_cc(dd, maximum)
                    watered_bag, *_=bag.modify_item(myBags, item="Waterskin",quantity=-1,create_on_fail=False,recursive_search=True)
                    used=maximum-value
                    leftover=5-used
                    if leftover>0:
                        rationed_bag, *_=bag.modify_item(myBags, item="Water (Ration)",quantity=leftover,bag_name="Bag",create_on_fail=False)
                    n+=+(used)
            amount-=1
bag.save_bags(myBags)
if watered_bag:
    water, *_=bag.display_bag(watered_bag)
text=f''' -title "{name} {'tries to ' if n==0 else ' '}refill{'' if n==0 else 's'} their supplies." -f "{dd}|{character().cc_str(dd)} (+{n})" {" ".join(water)} '''
return text
</drac2> -thumb {{image}}
