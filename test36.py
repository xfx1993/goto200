def magicalString(n):
    """
    :type n: int
    :rtype: int
    """
    if n<=3:
        return 1
    s='122'
    count= 1
    len = 3
    count_index =1
    num_index =2

    while True:
        next_count =int(s[count_index+1])
        if s[num_index]=='2':
            s = s+'1'*next_count
            count +=next_count
        else:
            s = s+'2'*next_count
        len =len+next_count
        if len>=n:
            break
        count_index+=1
        num_index +=next_count

    if len==n:
        return count
    elif len>n and s[-1]=='1':
        return count-1
    else:
        return count

print(magicalString(8))


