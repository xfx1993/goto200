def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    ac = 0
    stack = []

    for i in range(len(digits)-1,-1,-1):
        if i == len(digits)-1:
            num = digits[i]+ac+1
        else:
            num = digits[i]+ac
        if num==10:
            stack.append(0)
            ac = 1
        else:
            stack.append(num)
            ac = 0
    if ac==1:
        stack.append(1)
    stack.reverse()
    return stack

digits = [9,9,9,9,9]

print(plusOne(digits))

