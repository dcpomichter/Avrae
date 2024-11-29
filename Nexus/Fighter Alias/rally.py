embed <drac2>
fighter=character().levels.get('Fighter')
a=argparse(&ARGS&)
target=a.last('t')
if fighter>=1:
    subclass=get("subclass", "")
    if "Battle Master" in subclass:
        superiority=character().get_cc('Superiority Dice')
        dice=2 if fighter<=6 else 3 if fighter<=9 else 4 if fighter<=14 else 5 if fighter<=17 else 6
        size=8 if fighter<=9 else 10 if fighter<=17 else 12
        heal=vroll(f'{dice}d{size}+{fighter}')
        if superiority>=1:
            if combat():
                if combat().get_combatant(target):
                    cmbt=combat().get_combatant(target)
                    cmbt.set_temp_hp(max(cmbt.temp_hp, heal.total))
                    character().mod_cc('Superiority Dice', -1)
                    text=f''' -title "{name} rallies their ally!" -f "{cmbt.name}|{cmbt.hp_str()}" -f "Superiority Dice| {character().cc_str('Superiority Dice')} (-1)" -f "Effect|On your turn, you can use a bonus action and expend one superiority die to bolster the resolve of one of your companions. When you do so, choose a friendly creature who can see or hear you. That creature gains temporary hit points equal to {dice}d{size} + your Fighter Level."'''
                else:
                    character().mod_cc('Superiority Dice', -1)
                    text=f''' -title "{name} rallies their ally!" -f "{target} Temp HP| +{heal.total} THP" -f "Superiority Dice| {character().cc_str('Superiority Dice')} (-1)" -f "Effect|On your turn, you can use a bonus action and expend one superiority die to bolster the resolve of one of your companions. When you do so, choose a friendly creature who can see or hear you. That creature gains temporary hit points equal to {dice}d{size} + your Fighter Level." '''
            else:
                character().mod_cc('Superiority Dice', -1)
                text=f''' -title "{name} rallies their ally!" -f "{target} Temp HP| +{heal.total} THP" -f "Superiority Dice| {character().cc_str('Superiority Dice')} (-1)" -f "Effect|On your turn, you can use a bonus action and expend one superiority die to bolster the resolve of one of your companions. When you do so, choose a friendly creature who can see or hear you. That creature gains temporary hit points equal to {dice}d{size} + your Fighter Level." '''
        else:
            text=f''' -title "{name} tries to use their Rally" -f "Superiority Dice|{character().cc_str('Superiority Dice')}" '''
    else:
        text=f''' -title "{name} needs to learn a lesson or two." -f "You are not a Battle Master| Only Battle Masters can use Battle Maneuvers"'''
else:
    text=f''' -title "{name} needs to learn a lesson or two." -f "You are not a Fighter| Only Fighters can become Battle Masters"'''
return text
</drac2> -thumb {{image}}
