# def string_interleave(s1, s2)


def selective_sum(n, k):

    """
    >>> selective_sum(3018, 2) 
    11

    >>> selective_sum(593796, 3)
    25
    >>> selective_sum(12345, 10) 
    15
    """
    llist = []
    summ = 0
    a = [int(i) for i in str(n)]

    for i in range(len(a)):
       llist.append(a[i])
    
    for j in range(k):
        summ += max(llist)
        llist.remove(max(llist))
        if not llist:
            break
    print(summ)

   
    
    # llist.remove(max(llist))
    


