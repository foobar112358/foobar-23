def answer(x):
    s = set()
    for i in x:
        j = list(i.replace(',', '').replace('.', ''))
        j.reverse()
        j = ''.join(j)
        s.add(min(i, j))

    print s
    return len(s)

if __name__=='__main__':
    cases = [
        (["foo", "bar", "oof", "bar"], 2),
        (["x", "y", "xy", "yy", "", "yx"], 5),
        ]

    for i in ["%s=>%s %s %s" % (c[0], c[1], '==' if answer(c[0]) == c[1] else '!=', answer(c[0]), ) for c in cases]:
        print i
