def selections(seq, n):
    """
    selections(seq, n) is a recursive generator where
    seq is an iterable object
    n is the sample size
    n = len(seq) is the max sample size
    returns a list of lists of unique sample size items
    """
    if n == 0:
        yield []
    else:
        for i in range(len(seq)):
            # recursion
            for ss in selections( seq, n - 1):
                yield [seq[i]] + ss


def get(n, iterable='01'):
    return ["".join(x) for x in list(selections(iterable, n))]