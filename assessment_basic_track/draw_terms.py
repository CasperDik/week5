def draw_terms():
    import random
    import time
    n = # count items in the list
    for i in range(n):
        read = open("terms.txt").read()
        read = read[0:]
        list = read.split()
        random_word = random.choice(list)

        print(random_word)
        time.sleep(60)              #wait 60 seconds before looping again

draw_terms()