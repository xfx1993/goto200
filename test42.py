def findAndReplacePattern(words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """
    def str2numlist(s):
        index = 1
        map_dict=dict()
        num_list =''
        for ch in s:
            if ch not in map_dict:
                map_dict[ch]=index
                num_list+=str(index)
                index =index+1
            else:
                num_list+=str(map_dict[ch])
        return num_list

    pattern_num = str2numlist(pattern)

    result = []

    for w in words:
        if str2numlist(w)==pattern_num:
            result.append(w)

    return result

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"

print(findAndReplacePattern(words,pattern))


