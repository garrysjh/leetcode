def format_duration(seconds):
    #get number values in list
    # seconds
    # seconds/60 = min
    # seconds/60*60 = hour
    # seconds/60*60*24 = day
    # seconds/60*60*24*365 = year
    if seconds==0:
        return 'now'
    def toMinutes(seconds: int)->int:
        return int(seconds/60)
    def toHours(seconds:int)->int:
        return int(seconds/(60*60))
    def toDays(seconds:int)->int:
        return int(seconds/(60*60*24))
    def toYears(seconds:int)->int:
        return int(seconds/(60*60*24*365))
    timePlace=['year','day','hour','minute','second']
    time=[]
    time.append(toYears(seconds))
    time.append(toDays(seconds-toYears(seconds)*60*60*24*365))
    time.append(toHours(seconds-toDays(seconds)*60*60*24))
    time.append(toMinutes(seconds-toHours(seconds)*60*60))
    time.append(seconds-toMinutes(seconds)*60)
    result=[]
    for i in range(0, len(time)):
        if time[i]!=0:
            if time[i]==1:
                result.append(str(time[i]) + ' ' + timePlace[i])
            else:
                result.append(str(time[i]) + ' ' + timePlace[i] + 's')
    for i in range(0, len(result)-2):
        result[i] = result[i]+', '
    if len(result)>1:
        result[-2] = result[-2] + ' and '
    return ''.join(result)



    


TEST_CASE=3600
print(format_duration(TEST_CASE))
    