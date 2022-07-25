import math


def stocksBuySell(prices):
    maxProfit = 0
    minSoFar = prices[0]
    for price in range(0,len(prices)-1):
        minSoFar = min(minSoFar, prices[price])
        profit = prices[price] - minSoFar
        maxProfit = max(maxProfit, profit) 


    return profit

s = stocksBuySell([7,1,5,3,6,4])
print(s)



def maxProfit(prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit

m = maxProfit([7,1,5,3,6,4])

print(m)
