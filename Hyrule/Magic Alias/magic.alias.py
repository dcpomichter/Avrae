<drac2>
a=&ARGS&
ch=character()
h,ignore,cc,sb,spt,n,g=a[0] in "help?" if a else True,"-i" in a,"Magic Meter",ch.spellbook.spells,[0,2,3,5,6,7,9,10,11,12],a[0].lower() if a else '',load_json(get_gvar("51541795-21c7-47b4-bd5d-12a5efcf8b27"))
("" if [set('g',g+load_json(get_gvar(x))) for x in load_json(brewspells) if get_gvar(x)] else "") if exists("brewspells") else ""
E,P=[x for x in g if n==x.name.lower() and (ignore or x.name in [y.name for y in sb])],[x for x in g if n in x.name.lower()]
P=P if ignore or h else [x for x in P if x.name in [y.name for y in sb]]
E=E[0] if E else P[0] if P and len(P)==1 else ""
fl=int(a[a.index("-l")+1]) if "-l" in a and len(a)>a.index("-l") else int(E.level) if E else 0
spcm=int(a[a.index("-mp")+1]) if "-mp" in a and len(a)>a.index("-mp") else 0
spc=spt[fl]+spcm
sbv=E and E.name in [x.name for x in sb]
v=not h and E and ch.cc_exists(cc) and ch.get_cc(cc)>=spc
ch.mod_cc(cc,min(0,-spc)) if v and not ignore else ""
text=get_gvar("a0995f19-86e8-44ff-bf67-48cf48df3d5b") if h else "embed -t 60 -title 'Multiple Matches Found' -desc \'Which one were you looking for? \nRepeat the command with `!magic \"spell name\"`\n"+"\n".join(["**["+str(i+1)+"]** - "+P[i].name.replace("'","’") for i in range(min(10,len(P)))])+("\n...\n(*Result truncated)*" if len(P)>10 else "")+"\'" if P and not E else f'cast "{E.name}" -i {" ".join(a)} -f "{cc}|{ch.cc_str(cc) if ch.cc_exists(cc) else "*None*"}{""if not v or ignore else " ("+str(-1*spc)+")" if spc else ""}{""if not v or ignore else " (Cost Modifier: "+str(spcm)+")" if spcm else ""}"' if (v and sbv) or (ignore and E) else '-title "Cannot cast spell!" -desc "Not enough magic meter remaining, or spell is not in known spell list!\nUse `!game longrest` to restore all spell points if this is a character, or pass `-i` to ignore restrictions."'
return text
</drac2> -color <color> -thumb <image>
