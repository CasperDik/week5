def draw_terms():
        import random
        import time
        import numpy

        read = open("terms.txt").read()
        read = read[0:]
        list = read.split()
        list_2 = list.copy()
        n = len(list_2)

        bingocard = open("bingo_card.txt").read()
        bingocard2 = bingocard.split()

        for i in range(n):
            print("This is round number", (i+1))
            time.sleep(2)
            random_word = random.choice(list_2)
            print("The drawn word is: ", random_word)
            time.sleep(2)
            list_2.remove(random_word)
            if random_word in bingocard2:
                print("YES!", random_word, "is on your bingocard!!")
                time.sleep(2)
                bingocard2[bingocard2.index(random_word)] = "X"
                bc = numpy.array(bingocard2)
                bc = bc.reshape([5, 5])
                print("This is your current bingocard: \n", bc)
            else:
                print("Unfortunate,", random_word , "is not on your bingocard")
            time.sleep(3)  # wait x seconds before looping again

draw_terms()