def scalar_mult(scalar, vector):
    for i in range(len(vector)):
        vector[i] = vector[i] * scalar
    print(vector)


scalar_mult(2, [2,4,5,6])