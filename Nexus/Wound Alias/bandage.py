embed <drac2>
ch=character()
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
cc="Exhaustion"
JJ="Healer's Kit"
desc1="Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."
desc16="This kit is a leather pouch containing bandages, salves, and splints. The kit has five uses. As an action, you can expend one use of the kit to stabilize a creature that has 0 hit points, without needing to make a Wisdom (Medicine) check. In addition while in the Wilds you may expend a charge during a Short Rest to expend hit dice when you are Bloodied. And a charge may be expended to close a Wound."
ch.create_cc_nx(cc, 0, 6, None,"bubble", 0, desc=desc1, initial_value=0)
ch.create_cc_nx(JJ, 0, 5, None, "bubble", desc=desc16, initial_value=5)
a=argparse(&ARGS&)
DC=a.last('dc', 10, int)
skillAdv=1 if ch.skills.medicine.adv else -1 if ch.skills.medicine.adv is not None else 0
argAdv=1 if "adv" in a else -1 if "dis" in a else 0 if "adv" and "dis" in a else 0
comboAdv=skillAdv+argAdv
trueAdv= 1 if comboAdv>=1 else -1 if comboAdv<=-1 else 0
adv=max(-1, min(1, trueAdv))
if ch.get_cc(cc):
    adv=-1 if trueAdv<=0 else 0
dice=['1d20', '1d20kh1', '2d20kl1'][adv]
mod=max(intelligenceMod, wisdomMod)+ch.skills.medicine.prof*proficiencyBonus
treat=vroll(f"{dice}{mod:+}")
aid=''
if "aid" not in a:
    ch.mod_cc(JJ, -1)
    aid=f''' -f "{JJ}|{ch.cc_str(JJ)} (-1)" '''
myBags=bag.load_bags()
wounds_bag, *_=bag.get_bag(myBags, bag_id="Wounds")
bag.save_bags(myBags)
mod=f''' -f "{treat} (**__Failure__**)" '''
if treat.total>=DC:
    openWound_bag=bag.get_bag(myBags, bag_id="Wounds", exact_match=True)
    if "Open Wound" in openWound_bag[1]:
        ch.mod_cc(cc, -1)
        wounds_bag, *_=bag.modify_item(myBags, item="Treated Wound",quantity=1,bag_name="Wounds",create_on_fail=False)
        wounds_bag, *_=bag.modify_item(myBags, item="Open Wound",quantity=-1,bag_name="Wounds",create_on_fail=False, recursive_search=False)
        bag.save_bags(myBags)
        wounded, *_=bag.display_bag(wounds_bag)
        mod=f''' -f "{treat} **__Success__**" -f "{cc}|{ch.cc_str(cc)+' (-1)'}" -f "Effect| You can spend one hour to treat a wound using first-aid knowledge and supplies—make an Intelligence (Medicine) or Wisdom (Medicine) check to patch up the wound." {" ".join(wounded)} '''
    else:
        wounded, *_=bag.display_bag(wounds_bag)
        mod=f''' -f "You can't treat a wound that isn't Open" {" ".join(wounded)} '''
return f''' -title "{name} tries to treat their Wounds!" -f "DC|{DC}" {mod} {aid}'''
</drac2> -thumb https://media.discordapp.net/attachments/879551881557454859/1125513078914695209/1194318-women-artwork-ArtStation-fantasy-art-fantasy-girl.png?width=422&height=597
