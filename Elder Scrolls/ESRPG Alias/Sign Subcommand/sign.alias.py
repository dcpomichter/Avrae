embed <drac2>
features=load_json(get_gvar("ffff2c1d-c9ed-4a49-9eb6-fc45df26991c"))
args="&*&".lower()
n="\n"
footer="UESTRPG Birthsign Lookup"
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
            field=f"""  -title "Elder Scrolls Birthsign: {name}" -desc "{desc}" -thum "{thum}" """
            matches.append(field)
    if len(matches)>1:
        matches=[f'''-title "Elder Scrolls Birthsigns Containing: {args}" -desc "Multiple Matches Found" -f "{n.join(matchingNames)}" -image "https://img.photouploads.com/file/PhotoUploads-com/SdTv.jpg" ''']
    if len(matches)==0:
        matches=[f'-title "Elder Scrolls Birthsigns Containing: {args}" -desc "No matches found." -image "https://img.photouploads.com/file/PhotoUploads-com/SdTv.jpg" ']
    out.append(matches[0])
else:
    lookup=f'-title "Unofficial Elder Scrolls Tabletop RPG Birthsigns" -desc "{features[0].gend}" '
    out.append(lookup)
out.append(f""" -footer "{footer}" """)
return n.join(out)
</drac2>
