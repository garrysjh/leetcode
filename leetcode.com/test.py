def solution(text, ending):
    textArr = list(text)
    endingArr = list(ending)
    for i in range(1, len(text)):
        if textArr[i] != endingArr[i-1]:
            return False
    return True

print(solution('test','st'))