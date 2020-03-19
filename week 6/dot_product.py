def dot_product(vec1,vec2):
    if len(vec1) == len(vec2):
        x = 0
        for i in range(len(vec1)):
            x = x + (vec1[i] * vec2[i])
        print(x)
    else:
        print("!Vectors have different lengths!")


dot_product([1,2,1], [1,4,3])