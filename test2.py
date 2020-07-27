def convertToTitle( n):
    """
    :type n: int
    :rtype: str
    """
    list =''
    a =26
    while n//a>26:
        a = a*26

    while n>26:
        n1 = n//a
        if n%a ==0 or n%a ==26:
            n1=n1-1
            if n1 ==0:
                n1=26
            n = n-a

        if n1!=0:
            list+=(chr(64+n1))
        else:
            continue
        if n%a!=0:
            n=n%a
        a=a//26

    list+=(chr(64+n))

    return list

print(convertToTitle(10000))
