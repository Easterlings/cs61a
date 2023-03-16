def two_list(vals, counts):
    other = Link.empty
    for i in range(len(vals)):
        for j in range(counts[len(vals)-i-1]):
            other = Link(vals[len(vals)-i-1],other)
    return other
    """
    Returns a linked list according to the two lists that were passed in. Assume
    vals and counts are the same size. Elements in vals represent the value, and the
    corresponding element in counts represents the number of this value desired in the
    final linked list. Assume all elements in counts are greater than 0. Assume both
    lists have at least one element.

a = [1, 3, 2]
b = [1, 1, 1]
c = two_list(a, b)
c
    Link(1, Link(3, Link(2)))
a = [1, 3, 2]
b = [2, 2, 1]
c = two_list(a, b)
c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """
    "*** YOUR CODE HERE ***"