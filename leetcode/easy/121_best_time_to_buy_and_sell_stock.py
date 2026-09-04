# You’re given an array prices where prices[i] is the stock price on day i.

# Choose one day to buy and a later day to sell. Return the maximum profit you can
#  make. If no profit is possible, return 0.


# def buy_and_sell(prices):
#     #going to store value as [0] and index as [1]
#     highest_day = lowest_day = prices[0]

#     for index, today in enumerate(prices):
#         #check highest day
#         if today > highest_day:
#             highest_day = today

#         #chekc lowest day
#         if today < lowest_day:
#             lowest_day = today

#     return highest_day - lowest_day

def buy_and_sell(prices):
    #going to store value as [0] and index as [1]
    lowest_day = prices[0]
    max_profit = 0

    for index, today in enumerate(prices):
        profit_if_sold_today = today - lowest_day

        if profit_if_sold_today > max_profit:
            max_profit = profit_if_sold_today

        #check highest day
        if today < lowest_day:
            lowest_day = today

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(buy_and_sell(prices))