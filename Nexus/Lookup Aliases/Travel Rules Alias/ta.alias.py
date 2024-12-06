embed {{A,g=&ARGS&,load_json(get_gvar("05605340-0f32-4c18-8664-da7baa2976c8"))}}
{{a=' '.join([i for i in A])}}
{{b=[act for act in g[1:] if (a.lower() in act.name.lower() or all([x in act.name.lower() for x in a.lower().split()])) ] if a else ""}}
{{c=b[0] if len(b)==1 else (([act for act in g[1:] if a.lower()==act.name.lower()]+[""])[0]) if A else ""}}
{{B="\n".join([act.name for act in b])}}
{{f'-title "Travel Phase Containing: {a}" -desc "{B}" ' if len(b)>1 and not c else '-title "Travel Phase: '+c.name+'" '+('-desc "'+c.desc+'" ' if c.desc!="" else f'-image "{c.iurl}" ') if c else f'-desc "No matches found." ' if a else f'-title "Travel Phase" -desc "{g[0].gend}" '}}
{{f'-thumb " https://cdn.discordapp.com/attachments/757983367663976571/819984204367396864/3e0a21b109e10c8ade0649e9b9e7f0cd.jpg " ' if not c else f'-thumb "{c.thum}" '}} -color <color> -footer "`!travel [role]` -- Tip: `!ta` can be used instead of `!travel` for all commands."
