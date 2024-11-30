embed <drac2>
ch=character()
ch.set_cvar("coinPouchName", "Pouch of Septims")
ch.set_cvar("coinRates", "{'s':1}")
ch.set_cvar("bagItemPrefixes", "{'s':':dvd:'}")
text=f''' -title "{name} Sets up their Pouch of Septims" -desc "{name} can now use `{ctx.prefix}coins` to track your coinage in Septims." '''
return text
</drac2>
