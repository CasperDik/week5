def createlist(n):
    terms = list()
    for i in range(n):                  #inputs
        x = input("Please write here the bingo terms: ")
        terms.append(x)
    myfile= open("terms.txt", "a+")
    for i in terms:                     #terms to file
        myfile.write(i)
        myfile.write("\n")
    # Check if a term hasn't been added before
    # Register how often a term has been added to indicate how relevant a term is

n = int(input("how many bingo terms do you want to add to the list: "))
createlist(n)


