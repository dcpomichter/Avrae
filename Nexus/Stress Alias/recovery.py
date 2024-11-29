embed <drac2>
cc="Stress"
desc1="Stress is a measure of pressure on a character's mental state, representing a build-up of negative emotions such as anger, fear, frustration, and irritation. Too much Stress is bad for your mental health and, if not treated carefully, can lead to detrimental Afflictions-or even death.\n\nCharacters can suffer up to 40 points of Stress before they reach breaking point. To prevent this, they'll need to find ways to relax and recover during downtime."
low=int(character().get_cc_min(cc))
character().edit_cc(cc, low+10, 40, "long", None, low+10, desc=desc1)
character().set_cc(cc, character().get_cc_min(cc))
text=f''' -title "{name} recovers from their Mental Breakdown" -f "{cc}| {character().cc_str(cc)}" -f "A month after a character has removed all Afflictions, they recover their senses and can be active again. Each time a character recovers from a breakdown, their minimum Stress increases by 10." '''
return text
</drac2>
