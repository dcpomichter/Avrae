<drac2>
cc='Nexus Inspiration'
c=character()
return f'adv -f "Nexus Inspiration|If you have inspiration, you can expend it when you make an attack roll, saving throw, or ability check. Spending your inspiration gives you advantage on that roll." {c.mod_cc(cc,-1)} -f "{cc}|{c.cc_str(cc)} (-1)"' if c.cc_exists(cc) and c.get_cc(cc)>0 else f'-f "{cc}"|"Not Available" '
</drac2>
