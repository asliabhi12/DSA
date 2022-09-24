from re import M


def reverseWords(S):
        # code here 
        
        S = S.split('.')

        S= S[::-1]
        m = ""

        for i in range(len(S)):
            if i == len(S) -1:
                m+=S[i]
            else:
                m+=S[i] + "."

        return m

       
        

reverseWords('i.like.this.program.very.much')