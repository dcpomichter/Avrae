embed <drac2>
features=load_json(get_gvar("4652d85d-88e6-4c9a-b600-16f97a850654"))+load_json(get_gvar("e05faeca-8b41-45dc-abab-bf50e9cc1550"))
args="&*&".lower()
n="\n"
footer="UESTRPG Class Feature Lookup"
out=[]
if args:
    matches=[]
    matchingNames=[]
    for x in features[1:]:
        if args in x["name"].lower():
            name=x["name"]
            matchingNames.append(name)
            desc=x["desc"]
            thum=x["thum"]
            field=f"""  -title "Elder Scrolls Class Feature: {name}" -desc "{desc}" -thum "{thum}" """
            matches.append(field)
    if len(matches)>1:
        matches=[f'''-title "Elder Scrolls Class Features Containing: {args}" -desc "Multiple Matches Found" -f "{n.join(matchingNames)}" -image "https://wiki.uestrpg.com/images/4/4f/Delvebound.png" ''']
    if len(matches)==0:
        matches=[f'-title "Elder Scrolls Class Features Containing: {args}" -desc "No matches found." -image "https://wiki.uestrpg.com/images/4/4f/Delvebound.png" ']
    out.append(matches[0])
else:
    lookup=f'-title "Unofficial Elder Scrolls Tabletop RPG Class Features" -desc "{features[0].gend}" '
    out.append(lookup)
out.append(f""" -footer "{footer}" """)
return n.join(out)
</drac2>
