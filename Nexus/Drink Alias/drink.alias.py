embed <drac2>
ch=character()
dd="Waterskin"
ff="Thirst"
desc3="Holds enough liquid for five drink rations."
desc7="Adventure, travel, and combat are thirsty work. Keep a waterskin close by to avoid dehydration. If your Thirst reaches 5 or 6 gain +1 Exhaustion level, this level of Exhaustion can only be cleared by lowering your Thirst level below 5"
ch.create_cc_nx(dd, 0, 5, None, "bubble", desc=desc3, initial_value=5)
ch.create_cc_nx(ff, 0, 6, None, 'hex', 0, desc=desc7, initial_value=0)
a=argparse(&ARGS&)
n=a.last('n', 1, int)
value=ch.get_cc(dd)
thirst=ch.get_cc(ff)
refill=f""" -f "To refill your Waterskin use `!refill water`" """
if value>=abs(n) and thirst>=abs(n):
    ch.mod_cc(dd, -abs(n))
    ch.mod_cc(ff, -abs(n))
    text=f''' -title "{name} drinks what they can!" -f "{dd}|{ch.cc_str(dd)} (-{abs(n)})" -f "{ff}|{ch.cc_str(ff)} (-{abs(n)})" '''
else:
    ch.mod_cc(dd, -min(value, thirst))
    ch.mod_cc(ff, -min(value, thirst))
    text=f''' -title "{name} drinks what they can!" -f "{dd}|{ch.cc_str(dd)} (-{min(value, thirst)})" -f "{ff}|{ch.cc_str(ff)} (-{min(value, thirst)})" '''
return text+refill
</drac2> -thumb {{image}}
