def answer(n):
    squares = [(i + 1) ** 2 for i in xrange(100)]
    def _find(x, s, e):
        # print s, e
        if (e - s) < 0:
            return s - 1
        mid = (e + s) / 2
        if x < squares[mid]:
            res = _find(x, s, mid - 1)
        elif x > squares[mid]:
            res = _find(x, mid + 1, e)
        else:
            res = mid
        return res

    result = []
    while n:
        # print '#', n
        index = _find(n, 0, 100)
        # print '-', index, squares[index]
        result.append(index)
        n -= squares[index]

    return len(result)

def validate():
    squares = [i * i for i in xrange(1, 101)]
    for i in squares:
        n = 0
        while 1:
            n += 1
            s = i * n
            if s > 10000:
                break
            solution = answer(s)
            if solution > n:
                print s, '=', n, '*', i, ' answer:', solution


if __name__=='__main__':
    cases = [
        ([24], 3),
        ([160], 2),
        ([9999], 4),
        ([10000], 1),
        ([1], 1),
        ([12], 3),
        ]

    import test
    test.test(answer, cases)
    validate()
    # print test.bench(answer, cases)
