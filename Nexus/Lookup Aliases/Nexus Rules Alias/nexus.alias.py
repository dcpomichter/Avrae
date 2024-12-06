embed -title "Nexus Rules"

-desc "<drac2>
using (nrgvar = "1b76b34c-d74e-4572-aebe-c7312688076c",
       nrgvar2 = "f947fe21-9a06-40e7-b2ef-63703ddd3986"
)
x = "&1&".lower()
class_terms = ["class","classes","cl"]
barb_terms = ["barbarian","barb","bar"]
druid_terms = ["druid","dru"]
fighter_terms = ["fighter","fig"]
monk_terms = ["monk","mon"]
eldisc_terms = ["eldisc","elementaldisciplines"]
paladin_terms = ["paladin","palladin","pala","pal"]
ranger_terms = ["ranger","rang"]
exptraits_terms = ["exptraits","explorertraits"]
sorcerer_terms = ["sorcerer","sorc"]
warlock_terms = ["warlock","warl","lock"]
warlock2_terms = ["warlock2","warl2","lock2"]
wizard_terms = ["wizard","mage","wiz"]
race_terms = ["race","races","ra"]
featureMenu_terms = ["featuresmenu","featuremenu","featmenu","featuresm","featurem","featm"]
feature_terms = ["features","feature","feat"]
feature2_terms = ["features2","feature2","feat2"]
invMenu_terms = ["invmenu","inventorymenu","bagmenu","invm","inventorym","bagm"]
inv_terms = ["inv","inventory","bag"]
inv2_terms = ["inv2","inventory2","bag2"]
inv3_terms = ["inv3","inventory3","bag3"]
inv4_terms = ["inv4","inventory4","bag4"]
inv5_terms = ["inv5","inventory5","bag5"]
bulk_terms = ["bulk","bul"]
durMenu_terms = ["durabilitymenu","durmenu","durabilitym","durm"]
dur_terms = ["durability","dur"]
dur2_terms = ["durability2","dur2"]
ammo_terms = ["ammunition","amunition","ammo","amo"]
xp_terms = ["exp","xp","experience"]
spellMenu_terms = ["spellm","castm","spellcastingm","spellmenu","castmenu","spellcastingmenu"]
spell_terms = ["spell","cast","spellcasting"]
spell2_terms = ["spell2","cast2","spellcasting2"]
lightMenu_terms = ["lightingm","lightm","shadowm","lightingmenu","lightmenu","shadowmenu"]
light_terms = ["lighting","light","shadow"]
light2_terms = ["lighting2","light2","shadow2"]
light3_terms = ["lighting3","light3","shadow3"]
woundMenu_terms = ["woundm","injurym","woundsm","injuriesm","woundmenu","injurymenu","woundsmenu","injuriesmenu"]
wound_terms = ["wound","injury","wounds","injuries"]
wound2_terms = ["wound2","injury2","wounds2","injuries2"]
deathMenu_terms = ["deathm","rezm","ressurectionm","resurectionm","resm","deathmenu","rezmenu","ressurectionmenu","resurectionmenu","resmenu"]
death_terms = ["death","rez","ressurection","resurection","res"]
death2_terms = ["death2","rez2","ressurection2","resurection2","res2"]
fate_terms = ["fate","points"]
survMenu_terms = ["survm","srvm","survivalm","survmenu","srvmenu","survivalmenu"]
surv_terms = ["surv","srv","survival"]
surv2_terms = ["surv2","srv2","survival2"]
stressMenu_terms = ["stressm","sanitym","stressmenu","sanitymenu"]
stress_terms = ["stress","sanity"]
stress2_terms = ["stress2","sanity2"]
stress3_terms = ["stress3","sanity3"]
stress4_terms = ["stress4","sanity4"]
short_terms = ["short rest","short","sr"]
campMenu_terms = ["campm","campingm","campmenu","campingmenu"]
camp_terms = ["camp","camping"]
camp2_terms = ["camp2","camping2"]
longMenu_terms = ["long rest menu","longmenu","lrmenu","downtimemenu","long rest m","longm","lrm","downtimem"]
long_terms = ["long rest","long","lr","downtime"]
long2_terms = ["long rest2","long2","lr2","downtime2"]
explore_terms = ["explore","exploration"]
delve_rules = ["delving","delve","crawl"]
journey_terms = ["journey","travel","ta","jr"]

if x in class_terms:
  return nrgvar.classRules

if x in barb_terms:
  return nrgvar.barb

if x in druid_terms:
  return nrgvar.druid

if x in fighter_terms:
  return nrgvar.fighter

if x in monk_terms:
  return nrgvar.monk

if x in eldisc_terms:
  return nrgvar.eldisc

if x in paladin_terms:
  return nrgvar.paladin

if x in ranger_terms:
  return nrgvar.ranger

if x in exptraits_terms:
  return nrgvar.exptraits

if x in sorcerer_terms:
  return nrgvar.sorcerer

if x in warlock_terms:
  return nrgvar.warlock

if x in warlock2_terms:
  return nrgvar.warlock2

if x in wizard_terms:
  return nrgvar.wizard

if x in race_terms:
  return nrgvar.race

if x in featureMenu_terms:
  return nrgvar.featureMenu

if x in feature_terms:
  return nrgvar.feature

if x in feature2_terms:
  return nrgvar.feature2

if x in invMenu_terms:
  return nrgvar.invMenu

if x in inv_terms:
  return nrgvar.inv

if x in inv2_terms:
  return nrgvar.inv2

if x in inv3_terms:
  return nrgvar.inv3

if x in inv4_terms:
  return nrgvar.inv4

if x in inv5_terms:
  return nrgvar.inv5

if x in bulk_terms:
  return nrgvar.bulk

if x in durMenu_terms:
  return nrgvar.durMenu

if x in dur_terms:
  return nrgvar.dur

if x in dur2_terms:
  return nrgvar.dur2

if x in ammo_terms:
  return nrgvar.ammo

if x in xp_terms:
  return nrgvar.xp

if x in spellMenu_terms:
  return nrgvar.spellMenu

if x in spell_terms:
  return nrgvar.spell

if x in spell2_terms:
  return nrgvar.spell2

if x in lightMenu_terms:
  return nrgvar.lightMenu

if x in light_terms:
  return nrgvar.light

if x in light2_terms:
  return nrgvar.light2

if x in light3_terms:
  return nrgvar.light3

if x in woundMenu_terms:
  return nrgvar.woundMenu

if x in wound_terms:
  return nrgvar.wound

if x in wound2_terms:
  return nrgvar.wound2

if x in deathMenu_terms:
  return nrgvar2.deathMenu

if x in death_terms:
  return nrgvar.death

if x in death2_terms:
  return nrgvar2.death2

if x in fate_terms:
  return nrgvar2.fate

if x in survMenu_terms:
  return nrgvar2.survivalMenu

if x in surv_terms:
  return nrgvar2.survival

if x in surv2_terms:
  return nrgvar2.survival2

if x in stressMenu_terms:
  return nrgvar2.stressMenu

if x in stress_terms:
  return nrgvar2.stress

if x in stress2_terms:
  return nrgvar2.stress2

if x in stress3_terms:
  return nrgvar2.stress3

if x in stress4_terms:
  return nrgvar2.stress4

if x in short_terms:
  return nrgvar2.shortrest

if x in campMenu_terms:
  return nrgvar2.campMenu

if x in camp_terms:
  return nrgvar2.camp

if x in camp2_terms:
  return nrgvar2.camp2

if x in longMenu_terms:
  return nrgvar2.longrestMenu

if x in long_terms:
  return nrgvar2.longrest

if x in long2_terms:
  return nrgvar2.longrest2

if x in explore_terms:
  return nrgvar2.explore

if x in delve_rules:
  return nrgvar2.delve

if x in journey_terms:
  return nrgvar.journey

else:
  return "Welcome to The Nexus. With this alias, you can check out all the Nexus rules that are new and also those that change the rules as written.\nMost of them are from a free pdf called Darker Dungeons. You can check it out on this link if you want: http://giffyglyph.com/#giffyglyphs-darker-dungeons.\nHere is a list of all the new rules\n> ⁠Class alterations `!nr classes`\n> ⁠Race alterations `!nr races`\n> ⁠Feature alterations `!nr featuresm`\n> ⁠Inventory management rules `!nr invm`\n> ⁠Durability rules (Affects casters as well) `!nr durm`\n> ⁠Ammunition Rules `!nr ammo`\n> ⁠Xp changes `!nr xp` or `!nr exp`\n> ⁠Spellcasting rules `!nr spellm`\n> ⁠Light And Shadow rules `!nr lightm`\n> ⁠Wounds And Injuries rules `!nr woundsm`\n> ⁠Death And Ressurection rules `!nr deathm`\n> ⁠Fate Points rules `!nr fate`\n> ⁠Survival Conditions rules `!nr survm`\n> ⁠Stress And Afflictions rules `!nr stressm`\n> ⁠Short Rest  `!nr short` or  `!nr sr`\n> Camping rules   `!nr campm`\n> ⁠Long Rest And Downtime rules  `!nr longm` or  `!nr lrm`\n> ⁠Exploration Phase Rules  `!nr explore`\n> ⁠Delving Phase Rules  `!nr delve`\n> Journey (travel) Phase Rules  `!nr journey` or `!nr travel`"
</drac2>"
-footer "!nc for Nexus Contents. !nr for Nexus Rules. !ea for Exploration activities. !ta for travelling activities. !ca for Camping activities." -color <color> -thumb url.to.a.camping.jpg
