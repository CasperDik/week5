def add_vectors(a, b):
    if len(a) == len(b):
        for i in range(len(a)):
            a[i] += b[i]
        print(a)
    else:
        print("!Vectors have different lengths!")


add_vectors([1, 1, 4, 6], [1, 4, 5])