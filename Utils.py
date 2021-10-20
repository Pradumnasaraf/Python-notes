def max_num(list):
    
    Big =list[0]
    for items in list:
        if Big <items:
            Big = items
    return Big
