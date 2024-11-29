embed <drac2>
druid=character().levels.get('Druid')
if druid>=1:
    if druid>=2:
        cc="Wild Bestiary"
        desc="As a druid, you can shapeshift into a number of different wild shapes—this collection is called your Wild Bestiary.\n\nYour bestiary can hold a total number of shapes equal to your druid level. If you forget a shape from your bestiary, you will have to relearn it again.\n\nTo add a new shape to your bestiary (or replace an existing one), you must closely observe a live beast to study it. This requires 1 hour of focus per CR of the beast (minimum 1 hour), during which you develop a primal understanding of the creature's essence.\n\nIf the beast is friendly, reduce the required time by half —but if it is acting hostile, double the time."
        character().create_cc_nx(cc,0,druid,None,'star',desc=desc,initial_value=0)
        text=f''' -title "{name} is in touch with their primal nature" -f "Druid Level|{druid}" -f "{cc}|{character().cc_str(cc)}" -f "{desc}" '''
    else:
        text=f''' -title "{name} is in touch with their primal nature" -f "Druid Level|{druid}" -f "At higher levels you may run this command again to create your Wild Bestiary counter" '''
else:
    text=f''' -title "{name} is not in touch with their primal nature" -f "Druid Level|{druid}" -f "Try this command again when you have attuned to the way of the world." '''
return text
</drac2> -thumb {{image}}
