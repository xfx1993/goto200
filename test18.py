def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    index = 0
    length_t = len(t)
    length_s = len(s)

    for i in range(length_t):
        if t[i]==s[index]:
            index = index+1
        if index==length_s:
            return True
    return False

