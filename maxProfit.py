from typing import List




def maxProfit(prices: List[int]):
       """
        :type prices: List[int]
        :rtype: int
       """
       ### check for the lowest number 
       timeTobuy = 0 

       timeTosell = 1

       max_profit = 0 

       while timeTosell < len(prices):

           if prices[timeTobuy] < prices[timeTosell]:
               max_profit = max(prices[timeTosell] - prices[timeTobuy],max_profit)
           else:
               timeTobuy = timeTosell
           timeTosell += 1 

       return max_profit        



if __name__ == "__main__":

	prices = [7,1,5,3,6,4]
	print(maxProfit(prices))
