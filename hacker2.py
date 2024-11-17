'''Mark and Jane are very happy after having their first child. Their son loves toys, 
so Mark wants to buy some. There are a number of different toys lying in front of him, 
tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize 
the number of toys he buys with this money. Given a list of toy prices and an amount to spend, 
determine the maximum number of gifts he can buy.
Note Each toy can be purchased only once.
Example
The budget is 7  units of currency. He can buy items that cost [1,2,3] for 6 , or [3,4]for 7 units. 
The maximum is 3  items.
Function Description
Complete the function maximumToys in the editor below.
maximumToys has the following parameter(s):
int prices[n]: the toy prices
int k: Mark's budget
Returns
int: the maximum number of toys
Input Format
The first line contains two integers,  and , the number of priced toys and the amount Mark has to spend.
The next line contains  space-separated integers '''

# sort prices, from lowest to highest, each time keeping track of the total runnin price and stop when the max budget
#is reached
n=7 
k=50
prices=[1,12,5, 111, 200, 1000, 10]

def  maximumToys(prices,k):
    prices.sort()
    tot_spent=0
    toys=0
    for price in prices:
        if tot_spent+price<=k:
            tot_spent+=price
            toys+=1
        else:
            break #don't add more toys because budget is reached
    return toys
print(maximumToys(prices,k))