def multiplyStrings(s1,s2):
        # code here
        # return the product string
        
        sign = -1
        s1out = 0
        s2out = 0
        if s1.isnumeric():
            for i in range(len(s1)):
                s1out = s1out * 10 + (ord(s1[i]) - ord("0"))

                
        else:
            for i in range(1,len(s1)):
                s1out = s1out * 10 + (ord(s1[i]) - ord("0"))
            s1out*= sign


        if s2.isnumeric():
            for i in range(len(s2)):
                s2out = s2out * 10 + (ord(s2[i]) - ord("0"))
                
        else:
            for i in range(1,len(s2)):
                s2out = s2out * 10 + (ord(s2[i]) - ord("0"))
            s2out*= sign
      

        return s1out * s2out

        

        
            
s1 = "33"
s2 = "2"

print(multiplyStrings(s1, s2))