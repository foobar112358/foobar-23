def answer(words):
    alphatable = init_alphatable()

    # init table values
    for i in xrange(50):
        last_prefix = ""
        last_char = ''
        for word in words:
            if len(word) <= i:
                continue
            char = word[i]
            prefix = word[:i]
            if last_char and prefix == last_prefix and last_char != char:
                alphatable[char][last_char] = 1
                alphatable[last_char][char] = -1
            last_char = char
            last_prefix = prefix

    # print_alphatable(alphatable)

    while 1:
        c = 0
        for char, reltable in alphatable.iteritems():
            for compared_char, relation in reltable.iteritems():
                if not relation:
                    continue
                for inredir_char, indir_relation in alphatable[compared_char].iteritems():
                    if relation == indir_relation:
                        if not alphatable[char][inredir_char]:
                            c += 1
                            alphatable[char][inredir_char] = relation
                            alphatable[inredir_char][char] = -relation
        # print '#' , c
        if not c: break

    # print_alphatable(alphatable)
    chars = [(char, len([i for i in reltable.values() if i]), len([i for i in reltable.values() if i > 0])) for char, reltable in alphatable.iteritems()]
    # print chars
    sortedchars = sorted([(c[0], c[2]) for c in chars if c[1]], cmp=lambda a,b: a[1]-b[1])
    # print sortedchars
    return ''.join(map(lambda a: a[0], sortedchars))


def init_alphatable():
    alphabets_tpl = dict(zip(map(chr, range(ord('a'), ord('z') + 1)), [0] * 26))
    alphatable = {}
    for i in xrange(ord('a'), ord('z') + 1):
        alphabets = dict(alphabets_tpl.items())
        del(alphabets[chr(i)])
        alphatable[chr(i)] = alphabets
    return alphatable


def print_alphatable(table):
    print ' ', ' ',
    for i in range(ord('a'), ord('z') + 1):
        colc = chr(i)
        print colc,
    print ''

    for i in range(ord('a'), ord('z') + 1):
        rowc = chr(i)
        print rowc, ' ',
        for j in range(ord('a'), ord('z') + 1):
            colc = chr(j)
            r = table[rowc].get(colc, 0)
            if r:
                print '>' if table[rowc].get(colc, 0) > 0 else '<',
            elif rowc == colc:
                print '\\',
            else:
                print ' ',

        print ''


if __name__=='__main__':
    cases = [
        [[["z", "yx", "yz"]], 'xzy'],
        [[["y", "z", "xy"]], "yzx"],
        [[["ba", "ab", "cb"]], 'bac'],
        [[["z", 'aa', 'ac', 'ab', 'ad', 'ae']], 'zacbde'],
        [[["z", 'e', 'ae', 'ad', 'ac', 'ab', 'aa']], 'zedcba'],
        [[['z', 'z', 'y', 'v', 'w', 't', 'u', 'r', 's', 'p', 'q', 'n', 'o', 'l', 'm', 'j', 'k', 'h', 'i', 'f', 'g', 'd', 'e', 'b', 'c', 'a']], 'zyvwturspqnolmjkhifgdebca']
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
