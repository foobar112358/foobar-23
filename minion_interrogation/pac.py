def pac(m):
    q = [(m, 0)]

    lm = len(m)
    # yield m[:]
    while q:
        m, p = q.pop(0)
        print '----', m, p
        yield m
        for i in xrange(p + 1, lm):
            n = swap(m, p, i)
            q.append((n, p + 1))
            yield n


def swap(m, p1, p2):
    n = m[:]
    t = n[p1]
    n[p1] = n[p2]
    n[p2] = t
    return n


if __name__ == '__main__':
    c = 0
    for i in pac(range(3)):
        print i
        c += 1
    print c
