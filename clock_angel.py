# created by Aladin Handoklo

def calculate_angle(time):
    #split the time string into hours and mins
    splitted_time = time.split(":")

    # converting hours and minutes to numbers
    hours = int(splitted_time[0])
    mins = int(splitted_time[1])

    #check illegability
    if hours > 23 or hours < 0 or mins < 0 or mins > 59:
        return "the time format is illegal"

    #make all hour numbers in range 12 to 23 in range of 0 to 11
    hours %= 12

    #calculate the angel of the hours and the mins
    hours_angel = hours * 30 + mins * (30/60)
    mins_angel = mins * 6

    #get the difference as the resulting angel
    angel = hours_angel - mins_angel if hours_angel > mins_angel else mins_angel - hours_angel

    if angel > 180:
        return 360 - angel
    return angel

if __name__ == '__main__':
    print(calculate_angle("13:17"))
