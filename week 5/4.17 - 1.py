def turn_clockwise(x):
    if x == "N":
        return "E"
    elif x == "E":
        return "S"
    elif x == "S":
        return "W"
    elif x == "W":
        return "N"
    else:
        return "None"

x = input("compass point: ")
print(turn_clockwise(x))