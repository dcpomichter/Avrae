multiline
!cc delete "Hungry Jaws"
!a import {{get_gvar("90bfd768-1491-46ae-ac35-28c78bfc339a") if "Lizardfolk" in character().get_cvar('race') else ''}}
!embed <drac2>
lizard=character().get_cvar('race')
if "Lizardfolk" in lizard:
    cc="Hungry Jaws"
    desc="As a bonus action, or as one attack during an Attack action, you can make a bite attack against an adjacent creature. If the attack hits, it deals 1d6 damage. If the creature is neither undead nor a construct, you also gain temporary hit points equal to the damage dealt. The damage increases to 2d6 at 6th-level, 3d6 at 11th-level, and 4d6 at 16th-level.\n\nAfter you use Hungry Jaws, you can't use it again until you complete a short or long rest."
    character().create_cc_nx(cc,0,1,'short','hex',1,desc=desc)
    text=f'''-title "{name} is Hungry like the Lizardfolk" -f "{cc}|{character().cc_str(cc)}" -f "{desc}" -thumb {image}'''
else:
    text=f'''!embed -title "{name}, no one hungers like a Lizardfolk" -f "Race| {lizard}" -thumb {image}'''
return text
</drac2>
