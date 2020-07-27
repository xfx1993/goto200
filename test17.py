def suggestedProducts(products, searchWord):
    """
    :type products: List[str]
    :type searchWord: str
    :rtype: List[List[str]]
    """
    pro_length = len(products)
    searchWord_size = len(searchWord)
    result = []

    def dfs(products,searchWord,index):
        if index ==searchWord_size:
            return
        cur_products =[]
        cur_sw = searchWord[:index+1]
        if not products:
            result.append([])
        else:
            for p in products:
                if p.startswith(cur_sw):
                    cur_products.append(p)
            if not cur_products:
                result.append([])
            elif len(cur_products)<=3:
                result.append(cur_products)
            else:
                result.append(cur_products[:3])
        dfs(cur_products, searchWord, index+1)



    dfs(products,searchWord,0)
    return result


products = ["havana"]
searchWord = "tatiana"


print(suggestedProducts(products, searchWord))

