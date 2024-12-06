embed <drac2>
barb=character().levels.get('Barbarian')
if barb>=1:
    text=f''' -title "{name} would like to Rage." -f "Barbarian Level| {barb}" -f "Subcommands| `frenzy` - Will apply the drawbacks of a Frenzy Rage, checking for d12 hit die and deducting 1 if available" '''
else:
    text=f''' -title "{name} can't Rage." -f "Barbarian Level| {barb}" -f "This alias is for Barbarians. Come back when you have the anger." '''
return text
</drac2> -thumb {{image}}
