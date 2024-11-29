embed <drac2>
ch=character()
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
myBags=bag.load_bags()
secondBags=bag.save_state(myBags)
CC="Ration Box"
desc2="Stores up to five basic food rations."
ch.create_cc_nx(CC, 0, 5, None, "bubble", desc=desc2, initial_value=5)
a=argparse(&ARGS&)
n=0
maximum=ch.get_cc_max(CC)
rations_bag=bag.find_bag_with_item(secondBags, item="Rations")
if rations_bag:
    if rations_bag[0]=="Storage":
        bag.swap_pos(secondBags, bag_name="Storage", position=9)
        rations_bag=bag.find_bag_with_item(secondBags, item="Rations")
box_bag=bag.find_bag_with_item(secondBags, item="Ration Box")
if box_bag:
    if box_bag[0]=="Storage":
        bag.swap_pos(secondBags, bag_name="Storage", position=9)
        box_bag=bag.find_bag_with_item(secondBags, item="Ration Box")
rationed_bag=bag.find_bag_with_item(myBags, item="Rations")
if rationed_bag:
    if rationed_bag[0]=="Storage":
        bag.swap_pos(myBags, bag_name="Storage", position=9)
        rationed_bag=bag.find_bag_with_item(myBags, item="Rations")
boxed_bag=bag.find_bag_with_item(myBags, item="Ration Box")
if boxed_bag:
    if boxed_bag[0]=="Storage":
        bag.swap_pos(myBags, bag_name="Storage", position=9)
        box_bag=bag.find_bag_with_item(myBags, item="Ration Box")
rations=''
if rations_bag and rations_bag[0]!="Storage":
    for item_type, amount in rations_bag[1].items():
        while amount:
            value=ch.get_cc(CC)
            if value<maximum:
                if "Rations" in item_type:
                    ch.mod_cc(CC, +1)
                    rationed_bag, *_=bag.modify_item(myBags, item="Rations",quantity=-1,create_on_fail=False,recursive_search=True)
                    n+=+1
            amount-=1
if box_bag and box_bag[0]!="Storage":
    for item_type, amount in box_bag[1].items():
        while amount:
            value=ch.get_cc(CC)
            if value<maximum:
                if "Ration Box" in item_type:
                    ch.set_cc(CC, maximum)
                    rationed_bag, *_=bag.modify_item(myBags, item="Ration Box",quantity=-1,create_on_fail=False,recursive_search=True)
                    used=maximum-value
                    leftover=5-used
                    if leftover>0:
                        rationed_bag, *_=bag.modify_item(myBags, item="Rations",quantity=leftover,bag_name="Bag",create_on_fail=False)
                    n+=+(used)
            amount-=1
bag.save_bags(myBags)
if rationed_bag and rationed_bag[0]!="Storage":
    rations, *_=bag.display_bag(rationed_bag)
text=f''' -title "{name} {'tries to ' if n==0 else ' '}refill{'' if n==0 else 's'} their supplies." -f "{CC}|{character().cc_str(CC)} (+{n})" {" ".join(rations)} '''
return text
</drac2> -thumb {{image}}
