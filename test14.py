def findClosest(words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    pre_word_index = -1
    min_dis = 1000001

    for i in range(len(words)):
        if words[i]==word1 or words[i]==word2:
            if pre_word_index==-1:
                pre_word_index=i
            elif words[pre_word_index]==words[i]:
                pre_word_index = i
            elif words[pre_word_index]!=words[i]:
                min_dis = min_dis if i-pre_word_index>=min_dis else i-pre_word_index
                pre_word_index = i

    return min_dis


words = ["I","am","a","student","from","a","university","IG","a","city"]
word1 = "a"
word2 = "I"

print(findClosest(words,word1,word2))


