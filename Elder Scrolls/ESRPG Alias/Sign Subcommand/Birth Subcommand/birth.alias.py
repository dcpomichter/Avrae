embed <drac2>
ch=character()
n="\n"
args="&*&"
signs=["The Ritual","The Lover","The Lord","The Mage","The Shadow","The Steed","The Apprentice","The Warrior","The Lady","The Tower","The Atronach","The Thief","The Serpent"]
born=ch.get_cvar("birthsign",None)
birth=vroll("1d12")
serpent=vroll("1d12")
rolls=''
if not args and not born:
    rolls=f""" -f "Birth Month|{birth}|inline" -f "The Serpent's Influence|{serpent}|inline" """
if birth.total==serpent.total:
    ch.set_cvar_nx("birthsign",signs[12])
else:
    ch.set_cvar_nx("birthsign",signs[birth.total-1])
if args:
    for sign in signs:
        if args.lower() in sign.lower():
            ch.set_cvar("birthsign",sign)
newborn=ch.get_cvar("birthsign",None)
details=load_json(get_gvar("ffff2c1d-c9ed-4a49-9eb6-fc45df26991c"))
information=[f""" -title "{name} {'was' if born else 'is'} born under the sign of..." {rolls} -f "Birthsign|{newborn}" """]
for items in details[1:]:
    if newborn.lower() in items["name"].lower():
        information.append(f""" -desc "{items.desc}" """)
        information.append(f""" -thumb {items.thum if items.thum else image} """)
        break
currentCounters=[x.name for x in ch.consumables]
newCounters=[]
counterCreation=load_json(get_gvar("381e57b3-f0f5-4544-88e6-e9df04c7cfc0"))
for x, y in counterCreation.items():
    if newborn.lower() in x.lower():
        i=0
        counters=counterCreation.get(x,[])
        while i<len(counters):
            ch.create_cc_nx(name=counters[i].name,minVal=0,maxVal=counters[i].maxValue[level-counters[i].level] if typeof(counters[i].maxValue)=='SafeList' else counters[i].maxValue,reset=counters[i].reset,dispType=counters[i].display if counters[i].display else None,desc=counters[i].desc)
            if ch.get_cc_max(counters[i].name)!= counters[i].maxValue[lvl-counters[i].level] if typeof(counters[i].maxValue)=='SafeList' else counters[i].maxValue:
                ch.edit_cc(counters[i].name,maxVal=counters[i].maxValue[lvl-counters[i].level] if typeof(counters[i].maxValue)=='SafeList' else counters[i].maxValue)
            i+=1
createdCounters=''
for newcounter in ch.consumables:
    if newcounter.name not in currentCounters:
        newCounters.append(f"{newcounter.name}: {ch.cc_str(newcounter.name)}")
if newCounters!=[]:
    createdCounters=f'''-f "Counters Created|{n.join(newCounters)}" '''
information.append(f"""{createdCounters}""")
return n.join(information)
</drac2>
