import re
text='select Roll_no from named_recog where Roll_no=="102"'
pattern=re.compile(r'[a-zA-Z]{6}\s[a-zA-z_*0-9]+\s[a-zA-z]{4}\s[a-zA-Z0-9_]+')
matches=pattern.findall(text)
#print(matches)

pattern=re.compile(r'[a-zA-Z]{6}\s[a-zA-z_*0-9]+\s[a-zA-z]{4}\s[a-zA-Z0-9_]+')

pattern3=re.compile(r'[a-zA-Z0-9"=_]+')
matches=pattern3.findall(text)
print(matches)

#assert text==matches[0]



