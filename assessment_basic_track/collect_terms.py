def createlist(n):
    terms = list()
    for i in range(n):                  #inputs
        x = input("Please write here the bingo terms: ")
        terms.append(x)
    print(terms)
    myfile= open("terms.txt", "a+")
    for i in terms:                     #terms to file
        myfile.write(i)
        myfile.write("\n")

n = int(input("how many bingo terms do you want to add to the list: "))
createlist(n)

