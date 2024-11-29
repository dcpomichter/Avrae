embed <drac2>
cc="Nexus Inspiration"
ni_max=load_json(get_svar('ni','{}')).get('max',3)
c=character()
c.create_cc_nx(cc,maxVal=ni_max,minVal=0,reset_to=0,dispType='star')
c.mod_cc(cc,1)
arg="&*&"
explain=f""" Use the `ni` snippet in an `{ctx.prefix}attack`, `{ctx.prefix}check` or `{ctx.prefix}save` to your advantage, for instance `{ctx.prefix}save death ni`."""
return f'-title "{name} receives Nexus Inspiration!" -f "{cc}|{c.cc_str(cc)} (+1)" -desc "*{arg}*\n{explain}" ' if arg else f'-title "{name} receives Nexus Inspiration!" -f "{cc}|{c.cc_str(cc)} (+1)" -desc "{explain}"'
</drac2> -thumb {{image}}
