embed <drac2>
ch, n, arg=character(), "\n", &ARGS&
parsedargs=argparse(arg)
cc="Experience"
desc="When a character reaches the appropriate threshold they can Spend experience to level up."
ch.create_cc_nx(cc, 0, reset=None, reset_to=0, desc=desc, initial_value=0)
lvl=ch.levels.total_level
levelup=parsedargs.get('levelup')
currentVal=ch.get_cc(cc)
out=f''' -title "{name} has Experienced the Wilds" -f "Current Level:| {lvl}" '''
totals = [
        int(x.strip()) for x in (
            (svar := get_svar("xptotals"))
            or ch.get_cvar(
                "xptotals",
                "0,10,20,30,40,50,60,70,80,90"
            )).split(",")
    ]
if svar:
    ch.set_cvar('xptotals', svar)
if arg:
    if arg[0].strip('-+').isdigit():
        value=int(arg[0].strip('-+'))
        ch.mod_cc(cc, +value)
        out+=f''' -f "{cc}|{ch.cc_str(cc)} (+{value})" '''
    newVal=ch.get_cc(cc)
    if newVal>=totals[lvl] and not levelup:
        out+=f'-f "{name} has learned enough to Level Up to {lvl+1}|Be sure to run `{ctx.prefix}{ctx.alias} levelup`, then update your sheet before gaining more experience" '
    elif not levelup:
        out+=f' -f "Next Level: {lvl+1}| {totals[lvl]} exp (*{totals[lvl]-currentVal} remaining*)" '
    if levelup:
        if newVal>=totals[lvl]:
            ch.mod_cc(cc, -totals[lvl])
            out+=f''' -f "{name} spends their Experience to level up to {lvl+1}!|Be sure to update your sheet to reflect your new Level" -f "{cc}|{ch.cc_str(cc)} (-{totals[lvl]})" '''
        else:
            out+=f''' -f "You do not have the Experience to level up just yet." -f "Next Level: {lvl+1}| {totals[lvl]} exp (*{totals[lvl]-currentVal} remaining*)" '''
else:
    out+=f'''  -f "{cc}|{ch.cc_str(cc)}" -f "Next Level: {lvl+1}| {totals[lvl]} exp (*{totals[lvl]-currentVal} remaining*)" '''
    if currentVal>=totals[lvl]:
        out+=f'-f "{name} has learned enough to Level Up to {lvl+1}|Be sure to run `{ctx.prefix}{ctx.alias} levelup`, then update your sheet before gaining more experience" '
return out
</drac2> -footer "{{ctx.prefix}}{{ctx.alias}} [args]| created by @dcpomichter" -thumb {{image}} -color {{color}}
