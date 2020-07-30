def findClosedNumbers(num):
    """
    :type num: int
    :rtype: List[int]
    """
    bin_num  = bin(num)

    bin_num_list = list(bin_num)
    min_num=0
    max_num=0
    map_zero = dict()
    for i in range(2,len(bin_num_list)):
        if bin_num_list[i]=='0':
            map_zero[i]=0

    if not map_zero:
        return [int(bin_num+'0',2),-1]
    if len(map_zero)==1 and len(bin_num_list)-1 in map_zero:
        bin_num_list[-1]='1'
        bin_num_list[-2]='0'
        return [int(str(bin_num_list),2),-1]
    if len(map_zero)!=1 and len(bin_num_list)-1 in map_zero:
        bin_num_list[-1] = '1'
        bin_num_list[-2] = '0'
        min_num = int(str(bin_num_list),2)
        bin_num_list[-1] = '0'
        bin_num_list[-2] = '1'
        next_i = 0
        for key,value in map_zero.items():
            if key>next_i and key<len(bin_num_list)-1:
                next_i = key




    return [max_num,min_num]

print(findClosedNumbers(2))


