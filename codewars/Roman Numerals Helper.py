class RomanNumerals:
      
    @staticmethod
    def to_roman(val):
        roman = {
            0:'',
            1:'I',
            2:'II',
            3:'III',
            4:'IV',
            5:'V',
            6:'VI',
            7:'VII',
            8:'VIII',
            9:'IX',
            10:'X',
            20:'XX',
            30:'XXX',
            40:'XL',
            50:'L',
            60:'LX',
            70:'LXX',
            80:'LXXX',
            90:'XC',
            100:'C',
            200:'CC',
            300:'CCC',
            400:'CD',
            500:'D',
            600:'DC',
            700:'DCC',
            800:'DCCC',
            900:'CM',
            1000:'M',
            2000:'MM',
            3000:'MMM'
        }
        #convert number to digits
        charArr = list(str(val))
        for i in range(0, len(charArr)):
            power = len(charArr)-i-1
            charArr[i] = int(charArr[i])*pow(10,power)
            charArr[i] = roman[charArr[i]]
        sum=''
        for i in range(0, len(charArr)):
            sum+=charArr[i]
        return sum
    @staticmethod
    def from_roman(roman_num):
        roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        def isPositive(arr: list, index: int)->bool:
            try:
                if arr[index] < arr[index+1]:
                    return False
                else:
                    return True
            except:
                return True
        charArr = list(roman_num)
        #convert to array of numbers    
        for i in range(0, len(charArr)):
            charArr[i] = roman[charArr[i]]
        for i in range(0, len(charArr)):
            if isPositive(charArr,i)==False:
                charArr[i] = -charArr[i]
        sum=0
        for i in range(0, len(charArr)):
            sum+=charArr[i]
        return sum
    
    print(from_roman('MDCLXVI'))

