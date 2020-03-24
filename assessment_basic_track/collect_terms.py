#bingo program LC
#made by Casper Dik

def createlist():
    terms = list()
    myfile = open("terms.txt", "a+")
    x = 0
    print("Hello! First we need to create a bingocard. \n" "Write below the bingo term you want to add. \n" "If you have added all your words, press enter.")
    while x != "":
        if terms in myfile:
            print("This word has already been added to the list")
        else:
            x = input("Please write here the bingo terms you want to add: ")
            terms.append(x)

    for i in terms:                     #terms to file
        myfile.write(i)
        myfile.write("\n")


createlist()


