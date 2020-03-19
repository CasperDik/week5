def scalar_mult(scalar, vector):
    for i in range(len(vector)):
        vector[i] = vector[i] * scalar
    print(vector)


scalar_mult(7, [3,0,5,11,2])