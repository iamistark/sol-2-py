def distributeCandies(candyType):
    max_types = len(set(candyType))  
    max_allowed = len(candyType) // 2  
    return min(max_types, max_allowed)  

#Driver code
candyType = [1, 1, 2, 2, 3, 3]
print(distributeCandies(candyType))

