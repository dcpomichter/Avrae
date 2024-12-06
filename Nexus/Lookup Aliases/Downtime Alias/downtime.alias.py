embed <drac2>
A,g=&ARGS&,load_json(get_gvar("c7dbe307-ac57-476e-a678-8fbe2f55a38b"))
a=' '.join([i for i in A])
b=[act for act in g[1:] if (a.lower() in act.name.lower() or all([x in act.name.lower() for x in a.lower().split()])) ] if a else ""
c=b[0] if len(b)==1 else (([act for act in g[1:] if a.lower()==act.name.lower()]+[""])[0]) if A else ""
B="\n".join([act.name for act in b])
text= f'-title "Downtime Activities Containing: {a}" -desc "{B}" ' if len(b)>1 and not c else f'-title "Downtime Activity: '+c.name+'" '+(f'-desc "'+c.desc+'"' if c.desc!="" else f'-image "{c.iurl}" ' if c else f'-desc "No matches found."') if a else f' -title "Downtime Activities" -desc "{g[0].gend}" '
image=f'-thumb "https://i.imgur.com/w8V9tXW.png" ' if not c else f'-thumb "{c.thum}" '
return text+image
</drac2> -color <color>
