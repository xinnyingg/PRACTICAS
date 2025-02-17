def suma_equilibrada(lista):
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

    for i in range(len(lista)):
        if sum(lista[:i]) == sum(lista[i+1:]):
            return 1
    return -1

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())