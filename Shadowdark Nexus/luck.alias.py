embed <drac2>
cc="Luck Token"
ni_max=load_json(get_svar('ni','{}')).get('max',1)
c=character()
arg="&*&"
explain=f""" Each player can only have one luck token at a time. You can cash in a luck token to reroll any roll you just made. You must use the new result.\n\nYou can also give your luck token to a companion"""
c.create_cc_nx(cc,maxVal=ni_max,minVal=0,desc=explain,reset_to=0,dispType="star")
c.mod_cc(cc,1)
return f'-title "{name} receives a Luck Token!" -f "{cc}|{c.cc_str(cc)} (+1)" -desc "*{arg}*\n\n{explain}" ' if arg else f'-title "{name} receives a Luck Token!" -f "{cc}|{c.cc_str(cc)} (+1)" -desc "{explain}"'
</drac2> -thumb {{image}} -footer "{{ctx.prefix}}{{ctx.alias}}| created by @dcpomichter"
