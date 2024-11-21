embed <drac2>
ch=character()
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
G=get_gvar("5993c861-05c5-4518-8d86-7d9121f6339e")
L=G.split("\n")
F=vroll('1d100')
I=L.pop(0 if F.total<=6 else 1 if F.total<=12 else 2 if F.total<=18 else 3 if F.total<=24 else 4 if F.total<=30 else 5 if F.total<=36 else 6 if F.total<=42 else 7 if F.total<=48 else 8 if F.total<=54 else 9 if F.total<=60 else 10 if F.total<=66 else 11 if F.total<=72 else 12 if F.total<=77 else 13 if F.total<=82 else 14 if F.total<=87 else 15 if F.total<=91 else 16 if F.total<=96 else 17).title()
a=argparse(&ARGS&)
affliction={
    "fearful": "Fearful, Disadvantage on Wisdom Checks and Saves",
    "lethargic": "Lethargic, +1 Exhaustion until affliction removed",
    "masochistic": "Masochistic, Disadvantage on Constitution Checks and Saves",
    "irrational": "Irrational, Disadvantage on Intelligence Checks and Saves",
    "paranoid": "Paranoid, Speed is halved",
    "selfish": "Selfish, Disadvantage on Charisma Checks and Saves",
    "panic": "Panic, Disadvantage on Dexterity Checks and Saves",
    "hopelessness": "Hopelessness, Disadvantage on Strength Checks and Saves",
    "mania": "Mania, Disadvantage on attack rolls",
    "anxiety": "Anxiety, Disadvantage on Stress Checks",
    "hypochondria": "Hypochondria, Hit point maximum is halved",
    "narcissistic": "Narcissistic, Disadvantage on Ability Checks",
    "powerful": "Powerful, +2 to all damage rolls",
    "focused": "Focused, +2 to all attack rolls",
    "stalwart": "Stalwart, +2 AC",
    "acute": "Acute, Advantage on Intelligence Checks and Saves",
    "perceptive": "Perceptive, Advantage on Wisdom Checks and Saves",
    "courageous": "Courageous, Advatage on Charisma Checks and Saves"
    }
removal=''
mod=''
if "&1&".lower() in affliction:
    remove="&1&".lower()
    removal=affliction[remove]
i=a.get('i')
n=a.last('n', 0, int)
adv=1 if "adv" in a else -1 if "dis" in a else 0
dice=["1d20", "2d20kh1", "2d20kl1"][adv]
if n==0:
    treat=vroll(f'{dice}')
elif n>=1:
    treat=vroll(n)
myBags=bag.load_bags()
secondBags=bag.save_state(myBags)
affliction_bag=bag.get_bag(myBags, bag_id="Afflictions", create_on_fail=True)
afflicted_bag=bag.get_bag(secondBags, bag_id="Afflictions", create_on_fail=True)
if treat.total==1:
    success=f'''(**Critical Failure**) '''
    if not i:
        affliction_bag, *_=bag.modify_item(myBags, item=f'{I}',quantity=1,bag_name="Afflictions",create_on_fail=True)
        bag.save_bags(myBags)
        afflicted, *_=bag.display_bag(affliction_bag)
        mod=f''' -f "You fail to cure your Affliction, gaining a new one in the process." -f "Affliction Roll|{F}" -f "New Affliction|{I}" {" ".join(afflicted)} '''
    else:
        mod=f''' -f "You fail to cure your Affliction, gaining a new one in the process." -f "Update your Afflictions| Please correct your 'Afflictions' bag with the correct affliction based on this result, use `!qb 'Afflictions' '{I}'` to add the new affliction and `!qb 'Afflictions' -<old affliction>` to clear the previous.*Replace `<old affliction>` with the actual name in the bag.*" '''
elif treat.total<=9:
    afflicted, *_=bag.display_bag(affliction_bag)
    success=f'''(**Failure**) '''
    mod=f''' -f "You fail to cure your Affliction." {" ".join(afflicted)}'''
elif treat.total<=19:
    success=f'''(**Success**) '''
    affliction_bag, *_=bag.modify_item(myBags, item=f'{removal}',quantity=-1,bag_name="Afflictions",create_on_fail=False)
    bag.save_bags(myBags)
    afflicted, *_=bag.display_bag(affliction_bag)
    mod=f''' -f "You cured your Affliction.| ~~{removal}~~" {" ".join(afflicted)} '''
elif treat.total==20:
    success=f'''(**Critical Success**) '''
    minimum=ch.get_cc_min('Stress')
    stress=(ch.get_cc('Stress')-minimum)
    ch.set_cc('Stress', minimum)
    bag.delete_bag(myBags, bag_name="Afflictions")
    affliction_bag=bag.new_bag(myBags, bag_name="Afflictions")
    bag.save_bags(myBags)
    afflicted, *_=bag.display_bag(affliction_bag)
    mod=f''' -f "In a moment of clarity, you cleared yourself of all Afflictions and Stress." {" ".join(afflicted)} -f "Stress|{ch.cc_str('Stress')} (-{stress})" '''
return f''' -title "{name} works to cure their Afflictions" -f "Treatment Roll|{treat} {success}" {mod} '''
</drac2>  -image https://media.discordapp.net/attachments/879551881557454859/1125496724295778375/Stress.jpg
