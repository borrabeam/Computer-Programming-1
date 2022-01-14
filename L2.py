# Level 2

def num_even_digits(n):
    """Return the total number of even digits in n

    >>> num_even_digits(223345)
    3

    >>> num_even_digits(973315)
    0

    >>> num_even_digits(88660022)
    8

    >>> num_even_digits(12345670)
    4

    """
    n_string = str(n)
    llist1 = []
    for i in n_string:
        llist1.append(i)

    sum_digits = 0
    for i in llist1:
        if int(i) % 2 == 0:
            sum_digits += 1
    return sum_digits

def possible_rectangle(size1, size2, size3, size4):
    """Return True if size1, size2, size3, and size4 could form a rectangle (when two pair of sizes are equal)

    >>> possible_rectangle(10, 20, 20, 10)
    True

    >>> possible_rectangle(10, 30, 20, 10)
    False

    >>> possible_rectangle(10, 10, 10, 10)
    True

    >>> possible_rectangle(10, 10, 20, 10)
    False

    """
    
    if size1 + size2 == size3 + size4:
        return True
    else:
        return False


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose = True)



