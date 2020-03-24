#bingo program
#made by Casper Dik

def createlist(n):
    terms = list()
    for i in range(n):                  #inputs
        x = input("Please write here the bingo terms: ")
        terms.append(x)
    myfile= open("terms.txt", "a+")
    for i in terms:                     #terms to file
        myfile.write(i)
        myfile.write("\n")

def create_bingo_card():
    import random
    import numpy

    read = open("terms.txt").read()
    read = read[0:]
    list = read.split()
    list_3 = list.copy()
    card = []

    for i in range(25):
        random_word = random.choice(list_3)
        card.append(random_word)  # create list with 25 terms
        list_3.remove(random_word)

    bingo_card = numpy.array(card)
    bingo_card = bingo_card.reshape([5, 5])  # reshape list in 5x5 grid
    print("Welcome to bingo! This is your bingo card \n", bingo_card)
    numpy.savetxt("bingo_card.txt", numpy.array(bingo_card), fmt="%s")

def generate_bingo_cards():
    new_card = "no"
    create_bingo_card()
    new_card = input("Do you want to generate a new bingo card: ")
    while (new_card == "yes"):
        create_bingo_card()
        new_card = input("Do you want to generate a new bingo card: ")

def check_terms():
    import random
    import time
    import numpy

    t = 2  # pause time
    x = 0  # dummy to break loop
    read = open("terms.txt").read()
    read = read[0:]
    list = read.split()
    list_2 = list.copy()
    n = len(list_2)

    bingocard = open("bingo_card.txt").read()
    bingocard2 = bingocard.split()

    for i in range(n):
        print("This is round number", (i + 1))
        time.sleep(t)
        random_word = random.choice(list_2)
        print("The drawn word is: ", random_word)
        time.sleep(t)
        list_2.remove(random_word)
        if random_word in bingocard2:
            print("YES!", random_word, "is on your bingocard!!")
            time.sleep(t)
            bingocard2[bingocard2.index(random_word)] = "X"
            bc = numpy.array(bingocard2)
            bc = bc.reshape([5, 5])
            print("This is your current bingocard: \n", bc)
            for i in range(5):              # test for bingo on rows
                j = 0
                if bc[i, j] == bc[i, j + 1] == bc[i, j + 2] == bc[i, j + 3] == bc[i, j + 4] == "X":
                    x = 1
            for j in range(5):
                i = 0                       # test for bingo on columns
                if bc[i, j] == bc[i + 1, j] == bc[i + 2, j] == bc[i + 3, j] == bc[i + 4, j] == "X":
                    x = 1
            j = 0
            i = 0                           # test for diagonal bingo
            if bc[i, j] == bc[i + 1, j + 1] == bc[i + 2, j + 2] == bc[i + 3, j + 3] == bc[i + 4, j + 4] == "X":
                x = 1
                                        # test for diagonal bingo
            j = 4
            if bc[i, j] == bc[i + 1, j - 1] == bc[i + 2, j - 2] == bc[i + 3, j - 3] == bc[i + 4, j - 4] == "X":
                x = 1
        if x == 1:
            print("You have bingo!!! Shout BINGO and claim your price!")
            break
        else:
            print("Unfortunate,", random_word, "is not on your bingocard.")
        time.sleep(t)  # wait x seconds before looping again


def play_bingo():
    n = int(input("how many bingo terms do you want to add to the list: "))
    createlist(n)
    generate_bingo_cards()
    check_terms()


play_bingo()

#to do
#improve storing terms to list --> not ask for number but break loop in another way
#Check if a term hasn't been added before
#(extra) Register how often a term has been added to indicate how relevant a term is
#layout array?
