def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    str_length = len(haystack)
    substr_length = len(needle)

    if substr_length>str_length:
        return -1
    size = substr_length
    index = 0
    str_r = ''
    while size!=0:
        str_r +=haystack[index]
        index = index+1
        size = size-1
    if str_r ==needle:
        return 0
    first_index =0
    for i in range(index,str_length):
        str_r = str_r[1:]+haystack[i]
        first_index +=1
        if str_r==needle:
            return first_index
    return -1

haystack = "hellodfjkvdvdvdndvnlfssgvvsa"
needle = "ssgtyr"
print(strStr(haystack, needle))



