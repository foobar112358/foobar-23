def answer(chunk, word):
    res = chunk
    q = [(chunk, len(chunk))]
    st = set([chunk])
    wl = len(word)
    while q:
        c, r = q.pop(0)
        p = c.rfind(word, 0, r)
        if p >= 0:
            q.append((c, p + wl - 1))
            c = c[:p] + c[p+wl:]
            if c not in st:
                q.append((c, len(c)))
                st.add(c)
        elif len(c) < len(res):
            res = c

    return res


if __name__=='__main__':
    cases = [
        (("lololololo", "lol"), "looo"),
        (("goodgooogoogfogoood", "goo"), "dogfood"),
        (("12341212123434341234", '1234'), ''),
        (("12341212123123434341234", '1234'), '12121233434'),
        (("1122121221222", "12"), "222"),
        (("aaababa", "aba"), "a"),
        ]

    # import timeit
    from os import sys, path
    sys.path.insert(1, path.abspath('../'))
    import test
    test.test(answer, cases)
    print test.bench(answer, cases)
