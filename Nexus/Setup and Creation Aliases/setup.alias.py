embed <drac2>
ch=character()
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
myBags=bag.load_bags()
cc="Stress"
CC="Ration Box"
dd="Waterskin"
DD="Fate"
ee="Experience"
EE="Hunger"
ff="Thirst"
FF="Fatigue"
GG="Bag"
hh="Belt"
HH="Sheath"
ii="Quiver"
II="Worn"
jj="Exhaustion"
JJ="Healer's Kit"
desc1="Stress is a measure of pressure on a character's mental state, representing a build-up of negative emotions such as anger, fear, frustration, and irritation. Too much Stress is bad for your mental health and, if not treated carefully, can lead to detrimental Afflictions-or even death.\n\nCharacters can suffer up to 40 points of Stress before they reach breaking point. To prevent this, they'll need to find ways to relax and recover during downtime."
desc2="Stores up to five basic food rations."
desc3="Holds enough liquid for five drink rations."
desc4="1st-level characters start with one fate point -a reward for becoming an adventurer in the first place. You can hold up to three fate points at any one time, and fate points can't be exchanged between characters. Beyond this, fate points are extremely rare.\n\nTo gain fate, players must face-and defeat--the most dangerous monsters in your world. Dragons, liches, beholders--these fated monsters are significant threats to the party."
desc5="When a character reaches the appropriate threshold they can Spend experience to level up."
desc6="Few things burn through calories as fast as adventuring, so keep some snacks in your pocket. If your Hunger reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Hunger level below 5"
desc7="Adventure, travel, and combat are thirsty work. Keep a waterskin close by to avoid dehydration. If your Thirst reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Thirst level below 5"
desc8="It takes a keen mind to watch out for danger, so get regular sleep to stay alert and aware. If your Fatigue reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Fatigue level below 5"
desc10="A bag holds items of any size. You can draw an item from a bag with a full action."
desc11="A belt can hold only small and tiny items. You can draw an item from a belt with a free action."
desc12="A sheath holds weapons and shields. You can draw an item from a sheath with a free action."
desc13="A quiver stores bows, crossbows, arrows, quarrels, and javelins. You can draw an item from a quiver with a free action."
desc14="Space reserved for significant wearables, such as armor and awkward attire."
desc15="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
desc16="This kit is a leather pouch containing bandages, salves, and splints. The kit has five uses. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check. In addition while in the Wilds you may expend a charge during a Short Rest to expend hit dice when you are Bloodied. And a charge may be expended to close a Wound."
ch.create_cc_nx(cc, 0, 40, "long", None, 0, desc=desc1, initial_value=0)
ch.create_cc_nx(CC, 0, 5, None, "bubble", desc=desc2, initial_value=5)
ch.create_cc_nx(dd, 0, 5, None, "bubble", desc=desc3, initial_value=5)
ch.create_cc_nx(DD, 0, 3, None, "hex", 1, desc=desc4, initial_value=1)
ch.create_cc_nx(ee, 0, reset=None, reset_to=0, desc=desc5, initial_value=0)
ch.create_cc_nx(EE, 0, 6, None, 'hex', 0, desc=desc6, initial_value=0)
ch.create_cc_nx(ff, 0, 6, None, 'hex', 0, desc=desc7, initial_value=0)
ch.create_cc_nx(FF, 0, 6, None, 'hex', 0, desc=desc8, initial_value=0)
ch.create_cc_nx(jj, 0, 6, None,"bubble", 0, desc=desc15, initial_value=0)
ch.create_cc_nx(JJ, 0, 5, None, "bubble", desc=desc16, initial_value=5)
size=['small', 'medium', 'large']
text=f''' -title "{name} is almost ready with Setup!" -f "Don't Forget| Use `small` or `medium` to denote your size for Inventory tracking and Counter setup." -f "{cc}|{ch.cc_str(cc)}" -f "{CC}|{ch.cc_str(CC)}" -f "{dd}|{ch.cc_str(dd)}" -f "{JJ}|{ch.cc_str(JJ)}" -f "{DD}|{ch.cc_str(DD)}" -f "{ee}|{ch.cc_str(ee)}" -f "{EE}|{ch.cc_str(EE)}" -f "{ff}|{ch.cc_str(ff)}" -f "{FF}|{ch.cc_str(FF)}" -f "{jj}|{ch.cc_str(jj)}" '''
if "&1&".lower() in size:
    backpack_bag=bag.get_bag(myBags, bag_id="Bag", exact_match=True, create_on_fail=True)
    belt_bag=bag.get_bag(myBags, bag_id="Belt", exact_match=True, create_on_fail=True)
    sheath_bag=bag.get_bag(myBags, bag_id="Sheath", exact_match=True, create_on_fail=True)
    quiver_bag=bag.get_bag(myBags, bag_id="Quiver", exact_match=True, create_on_fail=True)
    worn_bag=bag.get_bag(myBags, bag_id="Worn", exact_match=True, create_on_fail=True)
    newstuff=bag.save_bags(myBags)
    if "&1&".lower()==size[0]:
        ch.create_cc_nx(GG, 0, int(8+max(strengthMod,constitutionMod)), None, "square", desc=desc10, initial_value=0)
        ch.create_cc_nx(hh, 0, 2, None, "square", desc=desc11, initial_value=0)
        ch.create_cc_nx(HH, 0, 1, None, "square", desc=desc12, initial_value=0)
        ch.create_cc_nx(ii, 0, 1, None, "square", desc=desc13, initial_value=0)
        ch.create_cc_nx(II, 0, 2, None, "square", desc=desc14, initial_value=0)
        text=f''' -title "{name} is ready for Nexus!" -f "{cc}|{ch.cc_str(cc)}" -f "{CC}|{ch.cc_str(CC)}" -f "{dd}|{ch.cc_str(dd)}" -f "{JJ}|{ch.cc_str(JJ)}" -f "{DD}|{ch.cc_str(DD)}" -f "{ee}|{ch.cc_str(ee)}" -f "{EE}|{ch.cc_str(EE)}" -f "{ff}|{ch.cc_str(ff)}" -f "{FF}|{ch.cc_str(FF)}" -f "{jj}|{ch.cc_str(jj)}" -f "{GG}|{ch.cc_str(GG)}" -f "{hh}|{ch.cc_str(hh)}" -f "{HH}|{ch.cc_str(HH)}" -f "{ii}|{ch.cc_str(ii)}" -f "{II}|{ch.cc_str(II)}" '''
    elif "&1&".lower()==size[1]:
        ch.create_cc_nx(GG, 0, int(10+max(strengthMod,constitutionMod)), None, "square", desc=desc10, initial_value=0)
        ch.create_cc_nx(hh, 0, 3, None, "square", desc=desc11, initial_value=0)
        ch.create_cc_nx(HH, 0, 1, None, "square", desc=desc12, initial_value=0)
        ch.create_cc_nx(ii, 0, 1, None, "square", desc=desc13, initial_value=0)
        ch.create_cc_nx(II, 0, 3, None, "square", desc=desc14, initial_value=0)
        text=f''' -title "{name} is ready for Nexus!" -f "{cc}|{ch.cc_str(cc)}" -f "{CC}|{ch.cc_str(CC)}" -f "{dd}|{ch.cc_str(dd)}" -f "{JJ}|{ch.cc_str(JJ)}" -f "{DD}|{ch.cc_str(DD)}" -f "{ee}|{ch.cc_str(ee)}" -f "{EE}|{ch.cc_str(EE)}" -f "{ff}|{ch.cc_str(ff)}" -f "{FF}|{ch.cc_str(FF)}" -f "{jj}|{ch.cc_str(jj)}" -f "{GG}|{ch.cc_str(GG)}" -f "{hh}|{ch.cc_str(hh)}" -f "{HH}|{ch.cc_str(HH)}" -f "{ii}|{ch.cc_str(ii)}" -f "{II}|{ch.cc_str(II)}" '''
    else:
        ch.create_cc_nx(GG, 0, int(12+(max(strengthMod,constitutionMod)*2)), None, "square", desc=desc10, initial_value=0)
        ch.create_cc_nx(hh, 0, 5, None, "square", desc=desc11, initial_value=0)
        ch.create_cc_nx(HH, 0, 1, None, "square", desc=desc12, initial_value=0)
        ch.create_cc_nx(ii, 0, 1, None, "square", desc=desc13, initial_value=0)
        ch.create_cc_nx(II, 0, 3, None, "square", desc=desc14, initial_value=0)
        text=f''' -title "{name} is ready for Nexus!" -f "{cc}|{ch.cc_str(cc)}" -f "{CC}|{ch.cc_str(CC)}" -f "{dd}|{ch.cc_str(dd)}" -f "{JJ}|{ch.cc_str(JJ)}" -f "{DD}|{ch.cc_str(DD)}" -f "{ee}|{ch.cc_str(ee)}" -f "{EE}|{ch.cc_str(EE)}" -f "{ff}|{ch.cc_str(ff)}" -f "{FF}|{ch.cc_str(FF)}" -f "{jj}|{ch.cc_str(jj)}" -f "{GG}|{ch.cc_str(GG)}" -f "{hh}|{ch.cc_str(hh)}" -f "{HH}|{ch.cc_str(HH)}" -f "{ii}|{ch.cc_str(ii)}" -f "{II}|{ch.cc_str(II)}" '''
return text
</drac2> -thumb {{image}}
