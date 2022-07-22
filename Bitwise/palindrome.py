
def isPal(string, l, r):
            if l >= r:
                return True
            if string[l] != str[r]:
                return False
            
            return isPal(string, l+1, r-1)
        

isPal("madamimadam")