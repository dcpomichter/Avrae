embed <drac2>
cc="Stress"
desc1="Stress is a measure of pressure on a character's mental state, representing a build-up of negative emotions such as anger, fear, frustration, and irritation. Too much Stress is bad for your mental health and, if not treated carefully, can lead to detrimental Afflictions-or even death.\n\nCharacters can suffer up to 40 points of Stress before they reach breaking point. To prevent this, they'll need to find ways to relax and recover during downtime."
character().create_cc_nx(cc, 0, 40, "long", None, 0, desc=desc1, initial_value=0)
current=character().get_cc(cc)
a=argparse(&ARGS&)
DC=a.last('dc', 10, int)
adv=a.adv(boolwise=True)
qq=vroll(character().saves.get('wis').d20(adv))
task=['check', 'heal']
degree=['minor', 'moderate', 'major', 'monstrous', 'majestic']
text=f''' -title "{name} checks their Stress levels" -f "{cc}|{character().cc_str(cc)}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} checks their Stress levels" -f "{cc}|{character().cc_str(cc)}" '''
if "&1&".lower() in degree:
  if "&1&".lower()==degree[0]:
    character().mod_cc(cc, +1)
    current=character().get_cc(cc)
    text=f''' -title "{name} is Stressed out!" -f "{cc}|{character().cc_str(cc)+' (+1)'}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} is Stressed out!" -f "{cc}|{character().cc_str(cc)+' (+1)'}" '''
  elif "&1&".lower()==degree[1]:
    stressed=vroll('1d4')
    character().mod_cc(cc, +stressed.total)
    current=character().get_cc(cc)
    text=f''' -title "{name} is Stressed out!" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} is Stressed out!" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" '''
  elif "&1&".lower()==degree[2]:
    stressed=vroll('1d6')
    character().mod_cc(cc, +stressed.total)
    current=character().get_cc(cc)
    text=f''' -title "{name} is Stressed out!" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} is Stressed out!" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" '''
  else:
    stressed=vroll('1d6+4')
    character().mod_cc(cc, +stressed.total)
    current=character().get_cc(cc)
    text=f''' -title "{name} is Stressed out!" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} is Stressed out!" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" '''
elif "&1&".lower() in task:
  if "&1&".lower()==task[0] and "&2&".lower() in degree:
    if "&2&".lower()==degree[0]:
      if qq.total < DC:
        character().mod_cc(cc, +1)
        current=character().get_cc(cc)
        text=f''' -title "{name} is Stressed out!" -f "DC|{DC}" -f "Minor Stress Check|{qq}' **Failure**'" -f "{cc}|{character().cc_str(cc)+' (+1)'}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} is Stressed out!" -f "DC|{DC}" -f "Stress Check|{qq}' **Failure**'" -f "{cc}|{character().cc_str(cc)+' (+1)'}" '''
      else:
        text=f''' -title "{name} keeps their cool." -f "DC|{DC}" -f "Minor Stress Check|{qq}' **Success**'" -f "{cc}|{character().cc_str(cc)}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} keeps their cool." -f "DC|{DC}" -f "Minor Stress Check|{qq}' **Success**'" -f "{cc}|{character().cc_str(cc)}" '''
    elif "&2&".lower()==degree[1]:
      stressed=vroll('1d4')
      if qq.total < DC:
        character().mod_cc(cc, +stressed.total)
        current=character().get_cc(cc)
        text=f''' -title "{name} is Stressed out!" -f "DC|{DC}" -f "Moderate Stress Check|{qq}' **Failure**'" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} is Stressed out!" -f "DC|{DC}" -f "Moderate Stress Check|{qq}' **Failure**'" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" '''
      else:
        text=f''' -title "{name} keeps their cool." -f "DC|{DC}" -f "Moderate Stress Check|{qq}' **Success**'" -f "{cc}|{character().cc_str(cc)}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} keeps their cool." -f "DC|{DC}" -f "Moderate Stress Check|{qq}' **Success**'" -f "{cc}|{character().cc_str(cc)}" '''
    elif "&2&".lower()==degree[2]:
      stressed=vroll('1d6')
      if qq.total < DC:
        character().mod_cc(cc, +stressed.total)
        current=character().get_cc(cc)
        text=f''' -title "{name} is Stressed out!" -f "DC|{DC}" -f "Major Stress Check|{qq}' **Failure**'" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} is Stressed out!" -f "DC|{DC}" -f "Major Stress Check|{qq}' **Failure**'" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" '''
      else:
        text=f''' -title "{name} keeps their cool." -f "DC|{DC}" -f "Major Stress Check|{qq}' **Success**'" -f "{cc}|{character().cc_str(cc)}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} keeps their cool." -f "DC|{DC}" -f "Major Stress Check|{qq}' **Success**'" -f "{cc}|{character().cc_str(cc)}" '''
    else:
      stressed=vroll('1d6+4')
      if qq.total < DC:
        character().mod_cc(cc, +stressed.total)
        current=character().get_cc(cc)
        text=f''' -title "{name} is Stressed out!" -f "DC|{DC}" -f "Monstrous Stress Check|{qq}' **Failure**'" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} is Stressed out!" -f "DC|{DC}" -f "Monstrous Stress Check|{qq}' **Failure**'" -f "{cc}|{character().cc_str(cc)+f' (+{stressed})'}" '''
      else:
        text=f''' -title "{name} keeps their cool." -f "DC|{DC}" -f "Monstrous Stress Check|{qq}' **Success**'" -f "{cc}|{character().cc_str(cc)}" -f "Breaking Point|When a character gains 40 points of Stress, they hit breaking point. In this state, your character is reckless, dangerous, and extremely vulnerable.\n\nIf you are hit by a damaging attack while at breaking point, your character suffers a fatal heart attack. You fall to 0 hit points, fail any remaining death saving throws, and die immediately." ''' if current==40 else f''' -title "{name} keeps their cool." -f "DC|{DC}" -f "Monstrous Stress Check|{qq}' **Success**'" -f "{cc}|{character().cc_str(cc)}" '''
  elif "&1&".lower()==task[1] and "&2&".lower() in degree:
    if "&2&".lower()==degree[0]:
      character().mod_cc(cc, -1)
      text=f''' -title "{name} relaxes a bit." -f "{cc}|{character().cc_str(cc)+' (-1)'}" '''
    elif "&2&".lower()==degree[1]:
      stressed=vroll('1d4')
      character().mod_cc(cc, -stressed.total)
      text=f''' -title "{name} is more relaxed." -f "{cc}|{character().cc_str(cc)+f' (-{stressed})'}" '''
    elif "&2&".lower()==degree[2]:
      stressed=vroll('1d6')
      character().mod_cc(cc, -stressed.total)
      text=f''' -title "{name} is very relaxed." -f "{cc}|{character().cc_str(cc)+f' (-{stressed})'}" '''
    else:
      stressed=vroll('1d6+4')
      character().mod_cc(cc, -stressed.total)
      text=f''' -title "{name} is extremely relaxed!" -f "{cc}|{character().cc_str(cc)+f' (-{stressed})'}" '''
  else:
    text=f''' -title "{name} is trying to adjust their Stress Levels" -f "Don't Forget|`check` requires a secondary argument of `minor`, `moderate`, `major`, or `monstrous` to determine how much is adjusted.\n\n`heal` requires a secondary argument of `minor`, `moderate`, `major`, or `majestic` to determine how much is adjusted." '''
return text
</drac2> -thumb {{image}}
