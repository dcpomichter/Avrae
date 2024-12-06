embed <drac2>
cc="Ammo Die"
desc= "Instead of tracking each individual shot, take a d12 - this is your Ammunition die. Roll it whenever you take a shot: if you roll a 1 or 2, the die gets one size smaller. If you're down to one piece of ammunition and you use it, that's it - it's all gone! Remove it from your inventory. Ammunition Die: d12 → d10 → d8 → d6 → d4 → 1"
character().create_cc_nx(cc, 0, 7, None, 'square', 6, desc=desc, initial_value=6)
dice=[0, 1, 4, 6, 8, 10, 12, 20][character().get_cc(cc)]
ammo=vroll(0) if dice==0 else vroll(f'1d{dice}')
if ammo.total>=3:
    text=f'''-f "Ammo Die|{ammo+' (**Recovered**)'}"'''
elif ammo.total==0:
    text=f'''miss -f "Ammo Die| You are out of Ammo"'''
else:
    character().mod_cc(cc,-1)
    remain=character().get_cc(cc)
    if remain>=2:
        text=f'''-f "Ammo Die|{ammo+' (**Expended**)'}" -f "{cc}|{character().get_cc(cc)+' (-1)'}"'''
    elif remain==1:
        text=f'''-f "Ammo Die|{ammo+' (**Expended**)'}" -f "{cc}|{character().get_cc(cc)+' (-1)'}" -f "You have 1 shot left, make it count"'''
    else:
        text=f'''-f "Ammo Die|{ammo+' (**Expended**)'}" -f "{cc}|{character().get_cc(cc)+' (-1)'}" -f "Your Ammo Stack is Empty"'''
return text
</drac2>
