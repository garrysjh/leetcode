#roman to integer, roman numerals are represnetde by seven different symbols IVXLCDM,  given roman numeral, convert it to integer
def romanChart(char: str) -> int:
    match char:
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L': 
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000

def roman(s: str):
    sum = 0
    arr = [*s]
    excepts = 0
    for element in arr:
        sum += romanChart(element)
    for element in range(0, len(arr)-1):
        if (arr[element] == 'I') & (arr[element+1] == 'V') | (arr[element] == 'I') & (arr[element+1] == 'X'):
            excepts += 2
        if (arr[element] == 'X') & (arr[element+1] == 'L') | (arr[element] == 'X') & (arr[element+1] == 'C'):
            excepts += 20
        if (arr[element] == 'C') & (arr[element+1] == 'D') | (arr[element] == 'C') & (arr[element+1] == 'M'):
            excepts += 200 
    return sum - excepts

s = "MCMXCIV"
print(roman(s))

    
