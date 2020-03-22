def draw_terms():
    import random
    import time

    read = open("terms.txt").read()
    read = read[0:]
    list = read.split()
    n = len(list)

    for i in range(n):
        random_word = random.choice(list)
        print(random_word)
        time.sleep(60)              #wait 60 seconds before looping again

draw_terms()