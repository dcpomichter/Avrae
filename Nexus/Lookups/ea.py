embed {{A,g=&ARGS&,load_json(get_gvar("623838bb-ecd9-4328-a00f-5c1320ba6f04"))}}
{{a=' '.join([i for i in A])}}
{{b=[act for act in g[1:] if (a.lower() in act.name.lower() or all([x in act.name.lower() for x in a.lower().split()])) ] if a else ""}}
{{c=b[0] if len(b)==1 else (([act for act in g[1:] if a.lower()==act.name.lower()]+[""])[0]) if A else ""}}
{{B="\n".join([act.name for act in b])}}
{{f'-title "Exploration Phase Containing: {a}" -desc "{B}" ' if len(b)>1 and not c else '-title "Exploration Phase: '+c.name+'" '+('-desc "'+c.desc+'" ' if c.desc!="" else f'-image "{c.iurl}" ') if c else f'-desc "No matches found." ' if a else f'-title "Exploration Phase" -desc "{g[0].gend}" '}}
{{f'-thumb "https://media.discordapp.net/attachments/879551881557454859/1104084192721113149/Greedfall01-675x378.png" ' if not c else f'-thumb "{c.thum}" '}} -color <color> -footer "`!explore [role]` -- Tip: `!ea` can be used instead of `!explore` for all commands."
