embed <drac2>
fighter=character().levels.get('Fighter')
if fighter>=1:
    text=f''' -title "{name} wants to know more about Fighting." -f "Fighter Level|{fighter}" -f "This alias will utilize subcommands to implement certain fighter abilities that have been altered by the Darker Dungeon PDF ruleset. Most actions are the same and can be utilized as normal with the `!a` command. Those that have been altered can be found below with their new command." -f "Subcommands|`wind` - Will execute the Second Wind ability including increased die amounts per Fighter Level.\n\n`rally` - Will execute the Battle Master Maneuver, Rally with the increased dice size and number. Supports `-t` in combat." '''
else:
    text=f''' -title "{name} thinks they know about Fighting." -f "Fighter Level|0" -f "You are not a Fighter. This alias and its subcommands will do you no good." '''
return text
</drac2> -thumb {{image}}
