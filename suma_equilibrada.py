def suma_equilibrada(f):
    """
    >>> suma_equilibrada([1, 1, 1, 1])
    1
>>> suma_equilibrada([10, 10, 7, 3, 30])
3
>>> suma_equilibrada([10, 20])
-1
>>> suma_equilibrada([-3, 5, -2])
2
>>> suma_equilibrada([0])
0
>>> suma_equilibrada([])
-1

    """

   # for i in range(len(lista)):
    #    if sum(lista[:i]) == sum(lista[i+1:]):
     #       return 1
    #return -1

    HalfSum=sum(f)/2
    sum1st=0
    pos=0
    for item in f:
        sum1st+=item
        if sum1st==HalfSum:
            return pos
        pos += 1
    return -1

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())




