embed <drac2>
sorcerer=character().levels.get('Sorcerer')
if sorcerer>=1:
    text=f''' -title "It's in your blood {name}" -f "Sorcerer Levels| {sorcerer}" -f "What you should know| This alias can be used to update counters and implement certain functions as changed by the Darker Dungeons pdf." -f "Subcommands|- `recover`- Creates a counter and imports an action for Sorcerous Recovery" '''
else:
    text=f''' -title "It's in the blood. Or it should be..." -f "This is an Alias for applying and tracking changes to the Sorcerer Subclass from the Darker Dungeons compendium." -f "You Won't need this| Come back when you get a level or two in Sorcerer." '''
return text
</drac2> -thumb {{image}}
