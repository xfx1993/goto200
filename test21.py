def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    length= len(prices)
    head = 1
    tail = 0
    cur_price = 0
    max_price = 0
    while True:
        if head ==length:
            break
        if prices[head]>prices[tail]:
            cur_price = prices[head]-prices[tail]
            if cur_price>max_price:
                max_price = cur_price
        else:
            tail =head
        head = head+1

    return max_price


prices=[7,1,4,3,9]
print(maxProfit(prices))