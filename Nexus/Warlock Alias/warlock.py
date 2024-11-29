embed <drac2>
ch=character()
warlock=ch.levels.get('Warlock')
cc="Sacrificial Bargain"
desc= "Once per short rest, when you cast a warlock spell of 1st-level or higher, you may spend a number of hit die equal to your warlock spell level to cast the spell without expending a spell slot. If the spell can't be cast at a higher level, you may instead spend a number of hit die equal to the spell level."
if warlock>=1:
    ch.create_cc_nx(cc, 0, 1, 'short', 'star', 1, desc=desc, initial_value=1)
    text=f''' -title "So, you borrowed power from a Patron" -desc "A warlock rarely stumbles into power by accident—they seek it out, against all wisdom and at great personal cost. With intellect, warlocks decipher eldritch runes, pierce the mortal veil, and bargain with otherworldly powers.

**Spellcasting:** Your spellcasting ability for warlock spells is now Intelligence, not Charisma.

**Saving Throws:** You gain proficiency in Intelligence
saving throws, not Charisma.

**Features:** Warlock features that rely on your Charisma modifier (Agonizing Blast, Lifedrinker, etc) now use your Intelligence modifier where appropriate." -f "{cc}|{ch.cc_str(cc)}" -f "{desc}" -f "Subcommands| Use your subclass as a subcommand to import the new versions of attacks and abilitied altered by this change." -f "Supported Subcommands| `hexblade`
`celestial`
`fiend`"'''
else:
    text=f''' -title "You have no power here!" -f "Warlocks Only| This alias is for Warlocks to import their attacks. You are no Warlock. Begone!"'''
return text
</drac2> -thumb {{image}}
