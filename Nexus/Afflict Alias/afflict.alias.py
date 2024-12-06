embed <drac2>
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
G=get_gvar("5993c861-05c5-4518-8d86-7d9121f6339e")
L=G.split("\n")
F=vroll('1d100')
I=L.pop(0 if F.total<=6 else 1 if F.total<=12 else 2 if F.total<=18 else 3 if F.total<=24 else 4 if F.total<=30 else 5 if F.total<=36 else 6 if F.total<=42 else 7 if F.total<=48 else 8 if F.total<=54 else 9 if F.total<=60 else 10 if F.total<=66 else 11 if F.total<=72 else 12 if F.total<=77 else 13 if F.total<=82 else 14 if F.total<=87 else 15 if F.total<=91 else 16 if F.total<=96 else 17).title()
a=argparse(&ARGS&)
i=a.get('i')
myBags=bag.load_bags()
if not i:
    affliction_bag, *_=bag.modify_item(myBags, item=f'{I}',quantity=1,bag_name="Afflictions",create_on_fail=True)
    bag.save_bags(myBags)
    afflicted, *_=bag.display_bag(affliction_bag)
    mod=f''' {" ".join(afflicted)} '''
else:
    mod=f''' -f "Update your Afflictions| Please correct your 'Afflictions' bag with the correct affliction based on this result, use `!qb 'Afflictions' '{I}'` to add the new affliction and `!qb 'Afflictions' -<old affliction>` to clear the previous.*Replace `<old affliction>` with the actual name in the bag.*" '''
return f''' -f "Affliction Roll|{F}" -f "New Affliction|{I}" {mod} '''
</drac2>  -title "The Stress is mounting!" -image https://media.discordapp.net/attachments/879551881557454859/1125496724295778375/Stress.jpg
