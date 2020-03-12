def day_name(dayname):
    if dayname == "sunday":
        return 0
    elif dayname == "monday":
        return 1
    elif dayname == "tuesday":
        return 2
    elif dayname == "wednesday":
        return 3
    elif dayname == "thursday":
        return 4
    elif dayname == "friday":
        return 5
    elif dayname == "saterday":
        return 6
    else:
        return "none"

def day_name1(daynumber):
    if daynumber == 0:
        return "sunday"
    elif daynumber == 1:
        return "monday"
    elif daynumber == 2:
        return "tuesday"
    elif daynumber == 3:
        return "wednesday"
    elif daynumber == 4:
        return "thursday"
    elif daynumber == 5:
        return "friday"
    elif daynumber == 6:
        return "saterday"
    else:
        return "none"

def returnday(leaveday, n):
    back = day_name(leaveday) + (n % 7)
    return day_name1(back)


print(returnday("sunday", 7))