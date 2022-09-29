def atoi(string):
        if not string:
            print("string doesn't exist")
            return -1
            
        
        out = 0
        negative= False
        

        if string[0] == '-':
            negative = True
            string = string[1:]
            
        else:
            out = ord(string[0]) - ord("0")
            


        for i in range(1, len(string)):
            if string[i].isnumeric():
                out = out * 10 + (ord(string[i])-ord("0"))
                

        if not negative:
            return out
        else:
            return -out


string = "-123"
print(atoi(string))
# if not negative and out >= 2147483647:
                #     return 2147483647
                # if negative and out >= 2147483647:
                #     return -2147483647
                # else:
                #     break