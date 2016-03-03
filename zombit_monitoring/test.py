import timeit

def bench(answer, cases, number=10, repeat=10):
    def _t():
        for c in cases:
            answer(*c[0])

    res = timeit.Timer(_t).repeat(number=number, repeat=repeat)
    return min(res)

def test(answer, cases):
    for c in cases:
        r = answer(*c[0])
        print '>>>> %s' % c[0]
        print "==== %s" % c[1]
        print '\033[%sm%s\033[0m %s' % (92 if r == c[1] else 41, 'PASS' if r == c[1] else 'FAIL', r)
        print ""
