def snail(snail_map):
    result = []
    #get height
    # height = len(snail_map)
    # width = len(snail_map[0])
    #top row
    while len(snail_map)!=0:
        if len(snail_map)!=0:
            for i in range(0, len(snail_map[0])):
                result.append(snail_map[0].pop(0))
            snail_map.pop(0)
        #rightmost column
        for i in range(0, len(snail_map)):
            result.append(snail_map[i].pop(-1))
        #bottom row leftovers
        if len(snail_map)!=0:
            for i in range(0,len(snail_map[-1])):
                result.append(snail_map[len(snail_map)-1].pop(-1))
            snail_map.pop(-1)
        #leftmost column
        for i in range(len(snail_map)-1,-1,-1):
            result.append(snail_map[i].pop(0))
    return result

    #index (0,width-1) & (1, width-1)

print(snail([[1,2,3,6],
            [4,5,6,7],
            [7,8,9,8]]))