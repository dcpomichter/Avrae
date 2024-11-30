embed <drac2>
features=load_json(get_gvar("1cf450c6-43ac-4781-8e98-890c0e2ea06f"))
args="&*&".lower()
n="\n"
footer="UESTRPG Race Lookup"
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
            field=f"""  -title "Elder Scrolls Race: {name}" -desc "{desc}" -thum "{thum}" """
            matches.append(field)
    if len(matches)>1:
        matches=[f'''-title "Elder Scrolls Races Containing: {args}" -desc "Multiple Matches Found" -f "{n.join(matchingNames)}" -image "https://wiki.uestrpg.com/images/e/ee/Races-banner.png" ''']
    if len(matches)==0:
        matches=[f'-title "Elder Scrolls Races Containing: {args}" -desc "No matches found." -image "https://wiki.uestrpg.com/images/e/ee/Races-banner.png" ']
    out.append(matches[0])
else:
    lookup=f'-title "Unofficial Elder Scrolls Tabletop RPG Races" -desc "{features[0].gend}" '
    out.append(lookup)
out.append(f""" -footer "{footer}" """)
return n.join(out)
</drac2>
