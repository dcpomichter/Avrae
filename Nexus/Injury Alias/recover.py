embed <drac2>
ch=character()
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
cc="Exhaustion"
desc1="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
(ch.create_cc_nx(cc, 0, 6, None, "bubble", 0, desc=desc1, initial_value=0))
a=argparse(&ARGS&)
myBags=bag.load_bags()
injury_bag=bag.get_bag(myBags, bag_id="Injuries")
if '&1&' in injury_bag[1]:
    ch.mod_cc(cc, -1)
    injury_bag, *_=bag.modify_item(myBags, item=f'&1&',quantity=-1,bag_name="Injuries",create_on_fail=False)
    bag.save_bags(myBags)
    injured, *_=bag.display_bag(injury_bag)
    mod=f''' -f "{cc}|{ch.cc_str(cc)+' (-1)'}" -f "Effect|Once you gain an injury, it remains active on your character and causes exhaustion until it is treated." -f "~~&1&~~ (-1)" {" ".join(injured)} '''
else:
    injured, *_=bag.display_bag(injury_bag)
    mod=f''' -f "Include your Injury| Please correct your command by adding your injuries. Copy and paste your injury from the bag below and surround it in quotes." {" ".join(injured)} '''
return f''' -title "{name} seeks aid!" {mod} '''
</drac2>
-thumb https://media.discordapp.net/attachments/879551881557454859/1125520184711581847/DeanSpencer-filler-prostheticleg.png
