embed <drac2>
ch=character()
args='&*&'
using(bag="4119d62e-6a98-4153-bea9-0a99bb36da2c")
myBags=bag.load_bags()
classes={
    'fighter':'d8',
    'priest':'d6',
    'thief':'d4',
    'wizard':'d4',
    'ranger':'d8',
    'bard':'d6',
    'knight of st ydris':'d6',
    'warlock':'d6',
    'witch':'d4',
    'desert rider':'d8',
    'pit fighter':'d8',
    'ras-godai':'d6',
    'sea wolf':'d8',
    'seer':'d6'
    }
ee="Experience"
GG="Backpack"
desc5="When a character reaches the appropriate threshold they can Spend experience to level up."
desc10="A crawler can carry gear up to your Strength Score or 10 slots, whichever is higher."
ch.create_cc_nx(ee, 0, reset=None, reset_to=0, desc=desc5, initial_value=0)
backpack_bag=bag.get_bag(myBags, bag_id="bp", exact_match=True, create_on_fail=True)
storage_bag=bag.get_bag(myBags, bag_id="Storage", exact_match=True, create_on_fail=True)
newstuff=bag.save_bags(myBags)
hit_die=''
if args:
    choice=args.lower()
    for cls in classes:
        if choice in cls:
            hitDie=f'''Hit Die ({classes.get(cls)})'''
            ch.set_cvar_nx('class', cls.title())
            ch.create_cc_nx(hitDie)
            hit_die=f'''-f "{hitDie}|{ch.cc_str(hitDie)}"'''
            break
ch.set_cvar_nx('meleeCheck', 0)
ch.set_cvar_nx('rangedCheck', 0)
ch.set_cvar_nx('spellCheck', 0)
if ch.get_cvar('class')=='Fighter':
    if ch.stats.constitution>=10:
        ch.create_cc_nx(GG, 0, int(max(strength,10)+ch.stats.get_mod(con)), None, "square", desc=desc10, initial_value=0)
    else:
        ch.create_cc_nx(GG, 0, int(max(strength,10)), None, "square", desc=desc10, initial_value=0)
else:
    ch.create_cc_nx(GG, 0, int(max(strength,10)), None, "square", desc=desc10, initial_value=0)
text=f''' -title "{name} is ready for Nexus!" -f "{ee}|{ch.cc_str(ee)}" -f "{GG}|{ch.cc_str(GG)}" {hit_die}'''
return text
</drac2> -thumb {{image}} -footer "{{ctx.prefix}}{{ctx.alias}} [class]| created by @dcpomichter"
