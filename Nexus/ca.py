embed -title "Camping Activities"

-desc "
<drac2>
using ( cagvar = "cbe22b9d-d24a-4112-9d93-512fa8a60acb"
 )

x = "&1&".lower()
frterms = ["foraging","forage","frg",]
crterms = ["craft", "crafting","cft","cra"]
hterms = ["hunting", "hunt", "hun", "tracking", "track"]
lterms = ["lookout", "look", "guard"]
grterms = ["reagents", "reag", "herbs"]
gmterms = ["materials", "minerals", "mat", "min"]
sterms = ["survey", "recon", "sur"]
ckterms = ["cooking", "cook", "meal"]
brterms = ["brewing", "brew", "ale"]
srterms = ["story", "st"]
mterms = ["music", "song", "mus"]
rterms = ["repair", "rep"]
rxterms = ["relax", "zzz", "meditate"]
gterms = ["game", "play", "dice", "chess"]

if x in crterms :
 return cagvar.crafting_activity
elif x in gterms :
 return cagvar.game_activity
elif x in frterms :
 return cagvar.foraging_activity
elif x in hterms :
 return cagvar.hunting_activity
elif x in lterms :
 return cagvar.lookout_activity
elif x in grterms :
 return cagvar.reagents_activity
elif x in gmterms :
 return cagvar.materials_activity
elif x in sterms :
 return cagvar.survey_activity
elif x in ckterms :
 return cagvar.cooking_activity
elif x in brterms :
 return cagvar.brewing_activity
elif x in srterms :
 return cagvar.story_activity
elif x in mterms :
 return cagvar.music_activity
elif x in rterms :
 return cagvar.repair_activity
elif x in rxterms :
 return cagvar.relax_activity


else:
 return '''**Notes:**\n- Camping activites are specific to player characters. Familiars, companions, npcs etc, cannot do them.\n- There are two types of camping activities. Tiring Activities and Relaxing Activities.\n - **Tiring Activities**: Activities that the watch spent doing them, still counts towards overall travel time for the day. You can only do two watches of them per day. Any more and you risk fatigue.\n - **Relaxing Activities**: Activities that you can do without risk of fatigue. You can do as many of them as you want. \n\n### Tiring Activities\n- Gather Reagents :herb: \n- Gather Materials :pick: \n- Forage :basket: \n- Survey :telescope: \n- Track :feet: \n### Relaxing Activities\n- Lookout :eye: \n- Cooking :cooking: \n- Brewing :beer: \n- Crafting :tools: \n- Play Music :notes: \n- Tell A Story :book: \n- Repair An Item :hammer: \n- Play A Game :game_die: \n- Relax In Solitude :man_in_lotus_position:\n\nYou can use `!ca <activity>` to learn more about each camping activity'''
</drac2>"
-footer "!ca [activity]" -color <color> -thumb url.to.a.camping.jpg
