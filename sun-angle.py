import datetime
def sun_angle(time):
    #replace this for solution
    basetime = datetime.datetime.strptime("06:00","%H:%M")
    endtime = datetime.datetime.strptime("18:00","%H:%M")
    intime = datetime.datetime.strptime(time,"%H:%M")
    r = (endtime-basetime).seconds
    lag = (intime - basetime).seconds
    if basetime <= intime <= endtime: 
        return (180*lag)/r
    else:
        return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")