<drac2>
cc='Goron Fortitude'
c=character()
remove=c.mod_cc(cc,-1) if c.cc_exists(cc) and c.get_cc(cc)>0 else ''
if remove!='':
    text=f'''adv -f "{cc}|When you make a Constitution saving throw, you can do so with advantage. Once you use this feature, you must finish a short or long rest before you use it again." -f "{cc}|{c.cc_str(cc)} (-1)"'''
else:
    text=''
return text
</drac2>
