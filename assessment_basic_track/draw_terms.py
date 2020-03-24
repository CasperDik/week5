#bingo program LC
#made by Casper Dik

def draw_terms():
    import random
    import time

    read = open("terms.txt").read()
    read = read[0:]
    list = read.split()
    list_2 = list.copy()
    n = len(list_2)


    for i in range(n):
        random_word = random.choice(list_2)
        print(random_word)
        list_2.remove(random_word)
        time.sleep(0.2)              #wait 60 seconds before looping again

draw_terms()