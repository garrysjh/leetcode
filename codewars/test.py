def spiralize(size):
    # fill empty array
    spiral = [[None for y in range(size)] for x in range(size)]
    while(size!=0):
        #fill top
        for i in range(0, size):
            spiral[0][i] = 0
        #fill right
        for i in range(0, size):
            spiral[i][-1]=0
        #fill bottom
        for i in range(0, size):
            spiral[-1][i]=0
        #fill left
        for i in range(-1, -(size)+1,-1):
            spiral[i][0]=0
        size-=1
    return spiral

print(spiralize(5))