from __future__ import division

def answer(minions):
    minions = [[minions[i][0], float(minions[i][1]) / minions[i][2], i] for i in xrange(len(minions))]
    minions.sort(lambda a,b : 1 if a[0] * b[1] >= b[0] * a[1] else -1)
    return [m[2] for m in minions]


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
