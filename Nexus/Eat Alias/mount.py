embed <drac2>
ch=character()
CC="Ration Box"
mount=['horse', 'donkey', 'wolf', 'ox', 'camel', 'mule', 'mastiff', 'pony', 'mount']
EE="Hunger-Mount"
for x in mount:
    real=ch.cc_exists(f"""Hunger-{x.title()}""")
    if real:
        EE=f"""Hunger-{x.title()}"""
        break
desc2="Stores up to five basic food rations."
desc6="Few things burn through calories as fast as adventuring, so keep some snacks in your pocket. If your Hunger reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Hunger level below 5"
ch.create_cc_nx(CC, 0, 5, None, "bubble", desc=desc2, initial_value=5)
ch.create_cc_nx(EE, 0, 6, None, 'hex', 0, desc=desc6, initial_value=0)
a=argparse(&ARGS&)
n=a.last('n', 1, int)
value=ch.get_cc(CC)
hunger=ch.get_cc(EE)
refill=f""" -f "To refill your Ration Box use `!refill ration`" """
if value>=abs(n) and hunger>=abs(n):
    ch.mod_cc(CC, -abs(n))
    ch.mod_cc(EE, -abs(n))
    text=f''' -title "{name} feeds their mount what they can!" -f "{CC}|{ch.cc_str(CC)} (-{abs(n)})" -f "{EE}|{ch.cc_str(EE)} (-{abs(n)})" '''
else:
    ch.mod_cc(CC, -min(value, hunger))
    ch.mod_cc(EE, -min(value, hunger))
    text=f''' -title "{name} feeds their mount what what they can!" -f "{CC}|{ch.cc_str(CC)} (-{min(value, hunger)})" -f "{EE}|{ch.cc_str(EE)} (-{min(value, hunger)})" '''
return text+refill
</drac2> -thumb {{image}}
