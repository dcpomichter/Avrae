embed <drac2>
gun=character().cc_exists("&1&".title())
ammo=character().cc_exists("&1& Ammo".title())
if gun and ammo:
  gun=character().get_cc("&1&".title())
  ammo=character().get_cc("&1& Ammo".title())
  full=character().get_cc_max("&1&".title())-gun
  if full==0:
      text=f''' -title "{name} tries to Reload" -f "Don't be silly| Your gun is fully loaded" -f "{"&1&".title()}|{character().cc_str("&1&".title())}"'''
  else:
    if "&2&".lower()=='breech':
      if ammo>=1:
        character().mod_cc("&1&".title(), +1)
        character().mod_cc("&1& Ammo".title(), -1)
        text=f''' -title "{name} Reloads their {"&1&".title()}" -f "{"&1&".title()}|{character().cc_str("&1&".title())+f' (+1)'}" -f "{"&1&".title()} Ammo| {character().cc_str("&1& Ammo".title())+f' (-1)'}" -f "Breech| With an Action or Bonus Action (player choice) a single bullet or charge can be loaded into the weapon."'''
      else:
        text=f''' -title "{name} tries to Reload" -f "Don't be silly| You don't have anymore Ammo" -f "{"&1& Ammo".title()}|{character().cc_str("&1& Ammo".title())}"'''
    elif ammo>full:
      character().mod_cc("&1&".title(), +full)
      character().mod_cc("&1& Ammo".title(), -full)
      text=f''' -title "{name} Reloads their {"&1&".title()}" -f "{"&1&".title()}|{character().cc_str("&1&".title())+f' (+{full})'}" -f "{"&1&".title()} Ammo| {character().cc_str("&1& Ammo".title())+f' (-{full})'}"'''
    else:
      character().mod_cc("&1&".title(), +ammo)
      character().mod_cc("&1& Ammo".title(), -ammo)
      text=f''' -title "{name} Reloads their {"&1&".title()}"  -f "Careful!| You are Out of Reloads" -f "{"&1&".title()}|{character().cc_str("&1&".title())+f' (+{ammo})'}" -f "{"&1&".title()} Ammo| {character().cc_str("&1& Ammo".title())+f' (-{ammo})'}"'''
elif gun and not ammo:
  text=f''' -title "{name} tries to Reload" -f "Don't be silly| You don't have any extra Ammo setup" -f "{"&1&".title()}|{character().cc_str("&1&".title())}" -f "{"&1& Ammo".title()}| **No Counter**"'''
elif ammo and not gun:
  text=f''' -title "{name} tries to Reload" -f "Don't be silly| You don't have a gun loaded" -f "{"&1&".title()}| **No Counter**" -f "{"&1& Ammo".title()}| {character().cc_str("&1& Ammo".title())}"'''
else:
  text=f''' -title "{name} tries to Reload" -f "Don't be silly| You don't have a gun or ammo" -f "{"&1&".title()}| **No Counter**" -f "{"&1& Ammo".title()}| **No Counter**"'''
return text
</drac2> -thumb "https://media.discordapp.net/attachments/879551881557454859/1149808743844937879/1255911904326.png?width=767&height=479"
