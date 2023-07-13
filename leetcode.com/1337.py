#K weakest rows in a matrix
# given an m x n matrix mat of 1's represneting soldiers and 0's represneting civs
# a row i is weaker than a row j if one of the following is true:
# num of soldiers is less than the number of soliders in row j
# both rows have the same number of soldiers and i < j

# take in matrix mat and k int

def weakMatrix(mat: list, k: int):
    #assign score to each row in the matrix
    #score = empty dictionary
    score = {}
    for row in range(0, len(mat),1):
        rowScore = 0
        for element in mat[row]:
            if element==1:
                rowScore += 1
        score[f'{row}'] = rowScore
    returnable = []
    for i in range(1,k+1):
        returnable.append(minKey(score))
        try:
            del score[minKey(score)]
        except KeyError:
            pass
    return returnable

def minKey(thisdict: dict):
    minList = list(thisdict.values())
    min = minList[0]
    minKey = list(thisdict.keys())
    returnable = minKey[0]
    for key, value in thisdict.items():
        if int(thisdict[key]) < min:
            returnable = key
            min = value
    return returnable


        
    
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3

print(weakMatrix(mat, k))

