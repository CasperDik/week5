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

print(day_name("saturday"))