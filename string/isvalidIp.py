def isValid(s):
    #code here
    counter = 0
    for i in range(len(s)):
        if s[i] == '.':
            counter+=1

    print(counter)
    if counter != 3:
        return 0

    st = set()

    for i in range(256):
        st.add(str(i))

    print(st)

    a = s.split('.')
   
    for i in range(len(a)):
        if a[i] not in st:
            return 0
    return 1

print(isValid("1.2.3.4"))    


 # temp = ""

    # for i in range(len(s)):
    #     if s[i] != '.':
    #         temp = temp+s[i]
        
    #     else:
    #         if temp in st:
    #             counter+=1
    #         temp=""

    # if temp in st:
    #         counter += 1

    # if counter == 4:
    #     return 1
    # else:
    #     return 0