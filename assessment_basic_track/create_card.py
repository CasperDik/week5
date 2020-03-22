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
        card.append(random_word)           # create list with 25 terms
        list_3.remove(random_word)

    bingo_card = numpy.array(card)
    bingo_card = bingo_card.reshape([5,5])      # reshape list in 5x5 grid
    print(bingo_card)

    #has to be interactive card?

create_bingo_card()