multiline
!a import {{get_gvar("c3142345-8d1d-46cf-a351-118f2a19e4c2")}}
!embed <drac2>
cc="Sorcerous Recovery"
desc="You are a font of sorcerous power. Once per long rest, when you finish a short rest, you may recover all of your expended sorcery points."
character().create_cc_nx(cc,0,1,'long','hex',desc=desc,initial_value=1)
text=f''' -title "{name} is on their way." -f "Sorcery Points|{character().cc_str('Sorcery Points')}" -f "{cc}|{character().cc_str(cc)}" -f "{desc}" '''
return text
</drac2> -thumb {{image}}
