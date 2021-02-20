def vectorReverse(vector):
    if len(vector) == 1:
        return vector[0]
    return vector[len(vector)-1] + vectorReverse(vector[:len(vector)-1])