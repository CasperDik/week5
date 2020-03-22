def create_bingo_card():
    import random
    import numpy

    read = open("terms.txt").read()
    read = read[0:]
    list = read.split()
    card = []

    for i in range(25):
        random_word = random.choice(list)
        card.append(random_word)           # create list with 25 terms
    #make sure that they are UNIQUE terms

    bingo_card = numpy.array(card)
    bingo_card = bingo_card.reshape([5,5])      # reshape list in 5x5 grid
    print(bingo_card)

    #has to be interactive card?

create_bingo_card()