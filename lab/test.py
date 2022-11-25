def non_decrease_subseqs(s):
    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:],prev)
        else:
            a = subseq_helper(s[1:],s[0])
            b = subseq_helper(s[1:],prev)
            return insert_into_all(s[0], a) + b
    return subseq_helper(s, 0)
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order.

seqs = non_decrease_subseqs([1, 3, 2])
sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
non_decrease_subseqs([])
    [[]]
seqs2 = non_decrease_subseqs([1, 1, 2])
sorted(seqs2)
    [[], [1], [1], [1, 1], [1, 1, 2], [1, 2], [1, 2], [2]]
    """
    a = subseq_helper([3, 2],1)
        a = subseq_helper([2],3)=[[2],[]]
            return subseq_helper([],3)=[[]]
            a = subseq_helper([],2)=[[]]
            b = subseq_helper([],3)=[[]]
            return insert_into_all(2, a) + b=[[2],[]]
        b = subseq_helper([2],1)
            a = subseq_helper([],2)=[[]]
            b = subseq_helper([],1)=[[]]
            return insert_into_all(2, a) + b
        return insert_into_all(3, a) + b
    b = subseq_helper([3, 2],0)
    return insert_into_all(1, a) + b