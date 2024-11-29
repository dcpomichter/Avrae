embed <drac2>
wizard=character().levels.get('Wizard')
if wizard>=1:
    cc="Arcane Recovery"
    desc="You have learned to regain some of your magical energy by studying your spellbook. Once per long rest when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher."
    recover=character().cc_exists(cc)
    if recover:
        character().delete_cc(cc)
    character().create_cc_nx(cc, 0, 1, 'long', 'bubble', 1, desc=desc)
    text=f''' -title "Your a wizard {name}!" -f "Arcane Recovery|{character().cc_str(cc)}" -f "Use| {desc}\n\nYou should have an Action imported from your sheet to use Arcane Recovery, check `!a list`" '''
else:
    text=f''' -title "Wizards only Fool!" -f "This Alias is meant for Wizards to apply the Darker Dungeon rule changes to class. No need for you to be here." '''
return text
</drac2> -thumb {{image}}
