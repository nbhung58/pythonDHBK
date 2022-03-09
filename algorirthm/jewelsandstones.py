
def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """       
    list_jewels = list(jewels.strip())    
    list_stones = list(stones.strip())
    b = 0
    for i in list_jewels:
        for j in list_stones:
            if i == j:
                b+=1
    print(b)


jewels = input("Input Jewels: ")
stones = input("Input Stones: ")
numJewelsInStones(jewels, stones)