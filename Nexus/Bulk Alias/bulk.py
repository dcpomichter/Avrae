embed <drac2>
bulk=load_json(get_gvar("d396efbf-9b4a-4fef-96ea-75bc21b076a3"))
args="&*&".lower()
n="\n"
footer=[]
out=[f""" -title "Bulk Lookup- {args}" """]
if args:
    for x, y in bulk.items():
        for item, info in bulk.get(x,{}).items():
            if args in item:
                name=item.title()
                desc=info
                field=f""" -f "Item: {name}|Bulk: {x.split('_')[0].title()}{n}Slots Needed: {'0.2' if 'tiny' in x else '1' if 'small' in x else '2' if 'medium' in x else '3' if 'large' in x else '6' if 'xlarge' in x else '9'}" """
                footer.append(f"{x.split('_')[0].title()} Bulk")
                out.append(f"""{field} -f "{desc}" """)
else:
    desc="__**Bulk estimation**__\nThis page shows how to estimate bulk for objects.\n\n**Estimating Bulk**\nTo choose a bulk rating for an object, consider its general size, weight, and shape—the more uncomfortable an item is to hold, the higher the bulk rating. \n**Extremely Small Objects**: Some items are especially small and easy to pack together—pins, coins, paperclips, etc. It takes 100 of these items to fill one inventory slot.\n**Extremely Large Objects**: If you need to assign a bulk rating to an extremely large object, use a multiple of 18 for your bulk rating—18/36/54/72, etc.\n\n**Category**: Tiny\n**Bulk**: 0.2 \n**Size**: Tiny: Smaller than the palm of your hand. You can hold many of these in one hand.\n**Weight**: Negligible: A negligible or trivial weight.\n\n**Category**: Small \n**Bulk**: 1 \n**Size**: Short: Up to a handspan / 9 inches. Can be held comfortably with one hand.\n**Weight**: Light: Up to 2 lbs. The weight of a loaf of bread or a bag of sugar.\n\n**Category**: Medium \n**Bulk**: 2 \n**Size**:Medium: Up to an arms-length / 2 feet long. Can be held with one hand.\n**Weight**: Medium: Up to 5 lbs. About as heavy as a few big bags of sugar.\n\n**Category**: Large \n**Bulk**: 3 \n**Size**: Long: Longer than an arm. Usually can be held with one hand, but is most comfortable with two.\n**Weight**: Heavy: Up to 10 lbs. About as heavy as a cat or a sack of potatoes.\n\n**Category**: X-Large \n**Bulk**: 6 \n**Size**: Extra-long: Longer than the height of an average person. Requires two hands to hold.\n**Weight**: Extra-heavy: Up to 35 lbs. About a quarter of the weight of an average person.\n\n**Category**: XX-Large \n**Bulk**: 9 \n**Size**: Extensive: Longer than the height of two people. Requires two hands to hold.\n**Weight**: Leaden: Up to 70 lbs. About half as heavy as an average person.\n\nTo find an item with this alias simply input its name after `!bulk`.\nExample: `!bulk dagger`\n`!bulk Ring Mail`\n\nCapitalization will not matter and Partial matches will return all options."
    footer.append("Estimation")
    out.append(f""" -desc "{desc}" """)
if len(footer)>1:
    footer.insert(0,"Multiple Matches")
out.append(f""" -footer "Bulk Lookup|{footer[0]}" """)
return n.join(out)
</drac2>
