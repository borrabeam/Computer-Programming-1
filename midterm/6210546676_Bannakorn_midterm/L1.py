# Level 1


def char_index_list(s, c):
    """
    >>> char_index_list("ababababa", 'a')
    [0, 2, 4, 6, 8]
    >>> char_index_list("aabaabaaccab", 'b')
    [2, 5, 11]
    >>> char_index_list("aabaabaaccab", 'c')
    [8, 9]
    >>> char_index_list("asdfghjkl", 'g')
    [4]
    >>> char_index_list("asdfghjkl", 'z')
    []
    >>> char_index_list("asdfghjklfff", 'f')
    [3, 9, 10, 11]
    """

    # your code goes here
    llist = []
    llist2 = []
    a = [str(i) for i in str(s)]

    for i in range(len(a)):
       llist.append(a[i])
    
    for i in range(len(a)):    
        if c == str(a[i]):
            llist2.append(i)
        else:
            pass
    print(llist2)

