def trappingWater(height):
        #Code here
        
        #preprocessing
        n = len(height)
        left = []
        maxi = height[0]
        for i in range(n):
            maxi = max(maxi, height[i])
            left.append(maxi)
        print(left)


        right = []
       
        
        
        maxi = height[n-1]
        for i in range(n-1,-1,-1):
            maxi = max(maxi, height[i])
            right.insert(0, maxi)
        print(right)
        new = []
        res = 0
        for i in range(n):
            res =  res + (min(left[i], right[i]) - height[i])
            

        return res