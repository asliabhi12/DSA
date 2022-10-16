import re


def nonrepeatingCharacter(s):
        #code here
        mydict = {}
        for i in range(len(s)):
            if s[i] in mydict:
                mydict[s[i]]+=1
            else:
                mydict[s[i]] = 0
   
        

        for i in mydict:
            if mydict[i] == 0:
                return i

        return "$"
            

     

print(nonrepeatingCharacter("hhhjdfgjkjgfkdjkj"))