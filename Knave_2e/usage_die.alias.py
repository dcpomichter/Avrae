embed <drac2>
ch, n, args=character(), "\n", &ARGS&
cc=f"{'&1&'.title()} Die"
desc= f"Instead of tracking each individual item, take a die - this is your usage die. Roll it whenever you use that item: if you roll a 1 or 2, the die gets one size smaller. {n}{n}Usage Die: d12 → d10 → d8 → d6 → d4 → 0"
ch.create_cc_nx(cc, 0, 6, None, 'square', 3, desc=desc, initial_value=3)
dice=[0, 4, 6, 8, 10, 12, 20][character().get_cc(cc)]
ammo=vroll(0) if dice==0 else vroll(f'1d{dice}')
text=f''' -title "Roll for Usage!" -footer "`{ctx.prefix}{ctx.alias} [item]` was written by @dcpomichter" -color {color} -thumb {image}'''
if ammo.total>=3:
    text +=f'''-f "{cc}|{ammo+' (**Stable**)'}"'''
elif ammo.total==0:
    text +=f''' -f "{cc}| You are out of {'&1&'}"'''
else:
    character().mod_cc(cc,-1)
    remain=character().get_cc(cc)
    if remain>=1:
        text +=f'''-f "{cc}|{ammo+' (**Expended**)'}" -f "{cc} Counter|{character().get_cc(cc)+' (-1)'}"'''
    else:
        text +=f'''-f "{cc}|{ammo+' (**Expended**)'}" -f "{cc} Counter|{character().get_cc(cc)+' (-1)'}" -f "Your Stack is Empty"'''
return text
</drac2>
