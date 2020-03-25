#bingo program LC
#made by Casper Dik

def createlist():
    myfile = open("terms.txt", "a+")
    x = 0
    while x != "":
        x = input("Please write here the bingo terms you want to add: ")
        read = open("terms.txt").read()
        read = read[0:]
        terms = read.split()
        if x in terms:
            print("This word has already been added to the list")
        else:
            myfile.write(x)
            myfile.write("\n")

def full_list():
    createlist()
    read = open("terms.txt").read()
    read = read[0:]
    list = read.split()
    y = len(list)
    o = 25 - y
    while o > 0:
        read = open("terms.txt").read()
        read = read[0:]
        list = read.split()
        y = len(list)
        o = 25 - y
        if o <= 0:
            break
        else:
            print("Oops, you have to at least add", o, "terms to play bingo")
            createlist()

full_list()


