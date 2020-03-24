#bingo program LC
#made by Casper Dik

def check_terms():
        import random
        import time
        import numpy

        t = 2                             #pause time
        x=0                                 #dummy to break loop
        read = open("terms.txt").read()
        read = read[0:]
        list = read.split()
        list_2 = list.copy()
        n = len(list_2)

        bingocard = open("bingo_card.txt").read()
        bingocard2 = bingocard.split()

        for i in range(n):
            print("This is round number", (i+1))
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
                for i in range(5):                      #test for bingo on rows
                    j=0
                    if bc[i, j] == bc[i, j + 1] == bc[i, j + 2] == bc[i, j + 3] == bc[i, j + 4] == "X":
                        x=1
                for j in range(5):
                    i=0                                #test for bingo colums
                    if bc[i, j] == bc[i+1, j] == bc[i+2, j] == bc[i+3, j] == bc[i+4, j] == "X":
                        x=1
                j=0
                i=0                             #test for diagonal bingo
                if bc[i, j] == bc[i+1, j+1] == bc[i+2, j+2] == bc[i+3, j+3] == bc[i+4, j+4] == "X":
                        x=1
                                                # test for diagonal bingo
                j=4
                if bc[i, j] == bc[i+1, j-1] == bc[i+2, j-2] == bc[i+3, j-3] == bc[i+4, j-4] == "X":
                    x=1
            if x == 1:
                print("You have bingo!!! Shout BINGO and claim your price!")
                break
            else:
                print("Unfortunate,", random_word , "is not on your bingocard.")
            time.sleep(t)  # wait x seconds before looping again

check_terms()