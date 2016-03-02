def answer2(chunk, word):
    while 1:
        # pos = chunk.rfind(word)
        h, _, t = chunk.rpartition(word)
        if not h:
            break
        chunk = h + t

    if chunk.startswith(word):
        chunk = chunk.replace(word, '')

    # while 1:
    #     segs = chunk.rsplit(word)
    #     if len(segs) < 2:
    #         break
    #     chunk = ''.join(segs)

    return chunk

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

def answer2(chunk, word):
    res = chunk
    # q = [(chunk, 0)]
    q = {chunk: 0}
    while 1:
        hasNew = True
        for c, s in q.iteritems():
            if s >= 0:
                p = c.find(word, s)
                if p >= 0:
                    q[c] = p + 1
                    c = c[:s] + c[s:].replace(word, )
        c, s = q.pop(0)
        # print c, s
        p = c.find(word, s)
        if p >= 0:
            q.append((c, p + 1))
            c = c[:s] + c[s:].replace(word, '', 1)
            # print '-- append ', (c, 0)
            q.append((c, 0))
        elif len(c) <= len(res):
            # print '-- result ', c
            res = c
        # else:
            # print '-- skip'

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
