def alphabetcounter(s):
    s = s.lower().replace("","")
    letter_counts = {}
    for letter in s:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    if letter_counts[" "] > 0:
        del letter_counts[" "]
    letter_items = list(letter_counts.items())
    letter_items.sort()
    for letter, count in letter_items:
        print(letter, "\t", count)

alphabetcounter("ThiS is String with Upper and lower case Letters")