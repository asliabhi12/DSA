import re

s = "A man, a plan, a canal: Panama"

#s= ''.join(e for e in s if e.isalnum()).lower()
print(s)

s = re.sub('[^A-Za-z0-9]+', '', s)
print(s)
res = (s[::-1].lower())

print(res == s)



