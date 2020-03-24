def createlist(n):
    terms = list()
    myfile = open("terms.txt", "a+")

    for i in range(n):   #inputs
        if terms in myfile:
            print("This word has already been added to the list")
        else:
            x = input("Please write here the bingo terms: ")
            terms.append(x)

    for i in terms:                     #terms to file
        myfile.write(i)
        myfile.write("\n")


n = int(input("how many bingo terms do you want to add to the list: "))
createlist(n)


