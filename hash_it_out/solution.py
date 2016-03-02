def answer(digest):
    message = [0] * (len(digest) + 1)
    for i in xrange(len(digest)):
        t = message[i - 1] ^ digest[i]
        # print t, (t % 2), (t if t % 2 else (t + 128)%256)
        message[i] = (t + 128)%256 if t % 2 else t

    return message[:-1]

def hash(message):
    message = message[:]
    message.append(0)
    digest = []
    for i in xrange(len(message) - 1):
        digest.append(((129 * message[i]) ^ message[i-1]) % 256)

    return digest

if __name__=='__main__':
    cases = [
        ([[0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
        ([[0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]],
          [0, 1,   4,   9, 16, 25,  36,  49,  64, 81, 100, 121, 144, 169, 196, 225]),
        ([[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]],
          [143, 1, 12, 0, 139, 1, 8, 0, 135, 1, 4, 0, 131, 1, 0, 0]),
        ([[129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
        ]

    import test
    import random
    for i in xrange(10):
        c = ([], [])
        for j in xrange(50):
            c[1].append(random.randint(0, 255))

        c[0].append(hash(c[1]))
        cases.append(c)

    # print hash([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    # print range(15, -1, -1)
    # print hash(range(15, -1, -1))
    # print hash([0, 1,   4,   9, 16, 25,  36,  49,  64, 81, 100, 121, 144, 169, 196, 225])

    test.test(answer, cases, 1, 1)
    # print test.bench(answer, cases)
