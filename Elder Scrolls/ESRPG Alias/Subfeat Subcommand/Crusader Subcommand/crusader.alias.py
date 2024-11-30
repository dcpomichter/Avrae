embed <drac2>
features=load_json(get_gvar("07ce0d56-4793-4bb5-a6d4-0d5e4c510f08"))
args="&*&".lower()
n="\n"
footer="UESTRPG Subclass Feature Lookup"
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
            field=f"""  -title "Elder Scrolls Subclass Feature: {name}" -desc "{desc}" -thum "{thum}" """
            matches.append(field)
    if len(matches)>1:
        matches=[f'''-title "Elder Scrolls Subclass Features Containing: {args}" -desc "Multiple Matches Found" -f "{n.join(matchingNames)}" -image "https://wiki.uestrpg.com/images/4/4f/Delvebound.png" ''']
    if len(matches)==0:
        matches=[f'-title "Elder Scrolls Subclass Features Containing: {args}" -desc "No matches found." -image "https://wiki.uestrpg.com/images/4/4f/Delvebound.png" ']
    out.append(matches[0])
else:
    lookup=f'-title "Unofficial Elder Scrolls Tabletop RPG Subclass Features" -desc "{features[0].gend}" '
    out.append(lookup)
out.append(f""" -footer "{footer}" """)
return n.join(out)
</drac2>
