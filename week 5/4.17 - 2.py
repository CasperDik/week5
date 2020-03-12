def day_name(daynumber):
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

print(day_name(3))