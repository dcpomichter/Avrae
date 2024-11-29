embed <drac2>
ch=character()
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
myBags=bag.load_bags()
CC="Ration Box"
dd="Waterskin"
JJ="Healer's Kit"
desc2="Stores up to five basic food rations."
desc3="Holds enough liquid for five drink rations."
desc16="This kit is a leather pouch containing bandages, salves, and splints. The kit has five uses. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check. In addition while in the Wilds you may expend a charge during a Short Rest to expend hit dice when you are Bloodied. And a charge may be expended to close a Wound."
ch.create_cc_nx(CC, 0, 5, None, "bubble", desc=desc2, initial_value=5)
ch.create_cc_nx(dd, 0, 5, None, "bubble", desc=desc3, initial_value=5)
ch.create_cc_nx(JJ, 0, 5, None, "bubble", desc=desc16, initial_value=5)
rations_bag=bag.find_bag_with_item(myBags, item="Rations")
water_bag=bag.find_bag_with_item(myBags, item="Water (Ration)")
healer_bag=bag.find_bag_with_item(myBags, item="Bandage")
rations=''
if rations_bag:
    rations, *_=bag.display_bag(rations_bag)
water=''
healer=''
if rations_bag!=water_bag and water_bag:
    water, *_=bag.display_bag(water_bag)
if rations_bag!=healer_bag:
    if water_bag!=healer_bag and healer_bag:
        healer, *_=bag.display_bag(healer_bag)
text=f''' -title "{name} checks on their supplies." -f "{CC}|{character().cc_str(CC)}" -f "{dd}|{character().cc_str(dd)}" -f "{JJ}|{character().cc_str(JJ)}" {" ".join(rations)} {" ".join(water)} {" ".join(healer)} '''
return text
</drac2> -thumb {{image}}