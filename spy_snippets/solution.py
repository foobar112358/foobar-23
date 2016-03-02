# encoding: utf8

def answer(document, searchTerms):
    doc = document.split(' ')
    res = []

    for t in searchTerms:
       p = find_next_word(doc, 0, t)
       res.append(p)
    res.sort()

    t = doc[res[0]]
    tmp = res[:]
    while True:
        p = find_next_word(doc, tmp[0] + 1, doc[tmp[0]])
        if not p: break

        tmp[0] = p
        tmp.sort()
        if res[-1] - res[0] > tmp[-1] - tmp[0]:
            res = tmp[:]

    return ' '.join(doc[res[0]: res[-1]+1])

def find_next_word(document, pos, word):
    for i in xrange(pos, len(document)):
        if document[i] == word:
            return i
    return None

if __name__=='__main__':
    cases = [
        (("many google employees can program", ["google", "program"]), "google employees can program"),
        (["a b c d a",  ["a", "c", "d"]], "c d a"),
        (["world there hello hello where world", ["hello", "world"]], "world there hello"),
        (["world there hello world hello where hello", ["hello", "world"]], "hello world"),
        (["world there world hello where hello world", ["hello", "world"]], "world hello"),
        (("many google employees google can program", ["google", "program"]), "google can program"),
        (("many google employees can program google", ["google", "program"]), "program google"),
        (("many google employees can program google some", ["google", "program", "some"]), "program google some"),
        (("many google employees can program google a some", ["google", "program", "some"]), "program google a some"),
        (("many google employees can program google xx xx a some program google", ["google", "program", "some"]), "some program google"),
        ]

    for c in cases:
        r = answer(*c[0])
        if r == c[1]:
            print '=='
        else:
            print "%s=>%s %s %s" % (c[0], c[1], '==' if r == c[1] else '!=', r)
