from __future__ import division

def answer2(minions):

    res = range(len(minions))
    res.sort(lambda a, b: s(minions[a], minions[b]))
    return res

def sortby(a, b):
    print a, b, a[0] * b[1], a[1] * b[0], 1 if a[0] * b[1] > b[0] * a[1] else -1
    return 1 if a[0] * b[1] >= b[0] * a[1] else -1

def answer(minions):
    minions = [[minions[i][0], float(minions[i][1]) / minions[i][2], i] for i in xrange(len(minions))]
    minions.sort(lambda a,b : 1 if a[0] * b[1] >= b[0] * a[1] else -1)
    return [m[2] for m in minions]

def answer2(minions):
    ''' Return the fastest expected minion interrogation order given a list
        of [time, prob_numerator, prob_denominator] minion info.
    '''
    num_minons = len(minions)

    # dividing the time by the probability of success gives the
    # individual expected interrogation time, so trying them
    # in order of this criterion will give the best overall time
    print minions
    sortkey = [t/(n/d) for t, n, d in minions]

    # timsort is stable, so we don't have to worry about having the
    # lexicographically first solution if we sort an ordered list
    return sorted(range(num_minons), key = sortkey.__getitem__)


def answer3(minions):
    minions = [[minions[i][0], float(minions[i][1]) / minions[i][2], i] for i in xrange(len(minions))]
    minions.sort(s)
    m = minions.pop(0)
    res = [m[2]]
    e = m[0]
    p = m[1]
    while minions:
        # cm = [0]
        cm = None
        ce = 1024000
        cp = [0, 1]
        for m in minions:
            te, tp = get_expect([e, p], m)
            if te < ce:
                cm = m
                ce = te
                cp = tp
        # print cm
        minions = [m for m in minions if m[2] != cm[2]]
        res.append(cm[2])
        e = ce
        p = tp
    return res

def answer4(minions):
    minions = [[minions[i][0], float(minions[i][1]) / minions[i][2], i] for i in xrange(len(minions))]
    res = [minions[0]]
    for i in xrange(1, len(minions)):
        m = minions[i]
        # candicate = []
        expect = 1024 * 50
        rescan = None
        for j in xrange(0, len(res) + 1):
            candicate = res[:]
            candicate.insert(j, m)
            # print candicate
            e, prob, _ = get_list_expect(candicate)
            # print e, expect
            if e < expect:
                # print "> ", e, expect
                rescan = candicate
                expect = e
        res = rescan[:]

    return [r[2] for r in res]

def get_list_expect(c):
    result = c[0]
    for i in xrange(1, len(c)):
        result = get_expect(result, c[i])

    return result


def memory(f):
    m = {}
    def _f(a, b):
        n = '%s_%s' % (a[2], b[2])
        r = m.get(n, None)
        if r is None:
            r = f(a, b)
            m[n] = r
        # print r
        return r
    return _f


@memory
def get_expect(a , b):
    print "."
    # if s(a, b) > 0:
    #     a, b = b, a
    exp = a[0] + b[0] - b[0] * float(a[1])
    prob = a[1] + b[1] - a[1] * float(b[1])
    return [exp, prob, "%s_%s" % (a[2], b[2])]


def s(a, b):
    return 1 if float(a[0]) * b[1] > float(b[0]) * a[1] else -1

if __name__=='__main__':
    cases = [
        ([[[5, 1, 5], [10, 1, 2]]], [1, 0]),
        ([[[5, 1, 5], [10, 1, 4]]], [0, 1]),
        ([[[5, 2, 3], [10, 1, 2]]], [0, 1]),
        ([[[20, 1, 2], [5, 1, 5], [10, 1, 2]]], [2, 1, 0]),
        ([[[20, 1, 2], [5, 1, 5], [10, 1, 4]]], [1, 0, 2]),
        ([[[1, 1023, 1024], [1, 1021, 1022], [1, 1020, 1021]]], [0, 1, 2]),
        ([[[1024, 1, 2], [1024, 1, 3], [1024, 1, 4]]], [0, 1, 2]),
        ([[[1024, 1, 2], [1024, 2, 3], [1024, 3, 4]]], [2, 1, 0]),
        ([[[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]], [2, 3, 0, 1]),
        ]

    import random
    # for i in xrange(10):
    #     n = random.randint(2, 50)
    #     case = [[], None]
    #     for j in xrange(n):
    #         d = random.randint(1, 1024)
    #         n = random.randrange(1, d)
    #         case[0].append([random.randint(1, 1024), n, d])
    #

    # import timeit
    # from os import sys, path
    # sys.path.insert(1, path.abspath('../'))
    import test
    test.test(answer, cases)
    # print test.bench(answer, cases)
