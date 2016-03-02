def answer2(food, grid):
    INIT, DOWN, RIGHT = 0, 1, 2
    path = [[0, 0, food, 0]]
    N = len(grid[0])
    NM = N - 1
    result = 200

    def _left_at_least(step):
        return NM * 2 - step + 1

    c = 0
    while 1:
        c += 1
        #print "===", path
        while path:
            x, y, f, d = path.pop()
            if d < RIGHT:
                break
        #print x, y, f, d, '->',
        d += 1
        if d == RIGHT:
            #print 'RIGHT',
            if x >= NM:
                #print 'WALL'
                continue
            #try go right
            #print "CHK", [x+1, y, grid[x+1][y]],
            f -= grid[x + 1][y]
            _left_required = _left_at_least(len(path) + 2)
            #print 'REQUIRE', _left_required, 'LEFT', f
            if not _left_required: # last step
                #print 'RES',
                if not f:
                    return 0
                if f < result:
                    result = f
                    #print 'UPD', result, '=>', f
                #else:
                    #print ''
                # if not result: # best
                #     return 0
            elif f < _left_required:
                #print 'EATEN'
                continue
            else:
                path.append((x, y, f + grid[x+1][y], d))
                path.append((x + 1, y, f, INIT))
                #print 'NEXT', [x+1, y]
                continue

        elif d == DOWN:
            #print 'DOWN',
            # try go down
            if y >= NM:
                path.append((x, y, f, d))
                #print 'WALL, REDIR'
                continue
            #print "CHK", [x, y+1, grid[x][y+1]],
            f -= grid[x][y+1]
            _left_required = _left_at_least(len(path) + 2)
            #print 'REQUIRE', _left_required, 'LEFT', f
            if not _left_required:
                # #print 'RES',
                if not f:
                    return 0
                if f < result:
                    # #print 'UPD', result, '=>', f
                    result = f
                #else:
                    #print ''
            elif f < _left_required:
                # #print 'EATEN', 'REDIR', 'NEXT', [x, y, f + grid[x][y+1], d]
                path.append((x, y, f + grid[x][y+1], d))
                continue
            else:
                # #print 'NEXT', [x, y + 1]
                path.append((x, y, f + grid[x][y+1], d))
                path.append((x, y + 1, f, INIT))
                continue
        else: # finish
            #print '### FIN ###'
            break

    print c
    return result

def answer(food, grid):
    N = len(grid)
    result = [[set() for j in xrange(N)] for i in xrange(N)]
    result[0][0].add(0)
    for i in xrange(N):
        for j in xrange(N):
            inext = grid[i+1][j] if i + 1 < N else 0xFFFFFFFF
            jnext = grid[i][j+1] if j + 1 < N else 0xFFFFFFFF
            for x in result[i][j]:
                if x + inext <= food:
                    result[i + 1][j].add(x + inext)
                if x + jnext <= food:
                    result[i][j + 1].add(x+jnext)
    return food - max(result[-1][-1]) if result[-1][-1] else -1

if __name__ == "__main__":
    cases = [
        ([7, [[0, 2, 5], [1, 1, 3], [2, 1, 1]]], 0),
        ([12, [[0, 2, 5], [1, 1, 3], [2, 1, 1]]], 1),
        ([118, [[0, 2, 2], [2, 8, 1], [5, 8, 1]]], 99)
        ]

    import random
    N = random.randrange(6, 8)
    matrix = []
    for i in xrange(N):
        l = []
        for j in xrange(N):
            l.append(random.randint(1, 9))
        matrix.append(l)
    matrix[0][0] = 0
    food = random.randint(20, 200)
    cases.append([[food, matrix], answer2(food, matrix)])

    import test
    test.test(answer, cases)
    # print test.bench(answer, cases)
