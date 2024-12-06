multiline
!a import {{get_gvar("685f5cc1-109d-40b3-af35-1f8419f99cc0") if character().levels.get('Ranger')>=1  else ''}}
!embed <drac2>
ranger=character().levels.get('Ranger')
if ranger>=1:
    if ranger>=2:
        cc="Hunter's Mark"
        desc="At 2nd-level, you gain the ability to mark a creature as your quarry. Add the Hunter's Mark spell to your known spell list as an extra spell. You may cast this as a 1st-level spell for free (no spell slot required) a number of times equal to your Wisdom modifier (minimum 1).\n\nYou regain all expended uses of this feature when you finish a long rest. You may also cast this spell as normal per your spellcasting ability by spending a spell slot."
        character().create_cc_nx(cc,0,max(wisdomMod, 1),'long','star', desc=desc),
        text=f''' -title "{name} is learning more everyday!" -f "Ranger Levels|{ranger}" -f "{cc}|{character().cc_str(cc)}" -f "{desc}" '''
    else:
        text=f''' -title "{name} wishes to learn about this land." -f "Ranger Levels|{ranger}" -f "At higher levels you will learn more and gain additional benefits. Run this command again then." '''
else:
    text=f''' -title "{name} wishes to learn about this land." -f "Ranger Levels|{ranger}" -f "You are not yet a ranger. Come back when you have built a true connection to the land." '''
return text
</drac2> -thumb {{image}}
