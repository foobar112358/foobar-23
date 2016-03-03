def answer(intervals):
    intervals = intervals[:]
    times = [intervals.pop(0)]

    for s, e in intervals:
        pos_s, pos_e = find_range(times, s, e)

        if pos_s >= len(times):
            times.append([s, e])
            continue

        if pos_e < pos_s:
            t = [s, e]
        else:
            t = [min(times[pos_s][0], s), max(times[pos_e][1], e)]
        a = times[:pos_s]
        a.append(t)
        a.extend(times[pos_e + 1:])
        times = a

    return sum([t[1] - t[0] for t in times])


def find_range(times, start, end):
    s = len(times)
    for i in xrange(len(times)):
        if start <= times[i][1]:
            s = i
            break
    e = s - 1
    for i in xrange(s, len(times)):
        if end >= times[i][0]:
            e = i
        else:
            break

    return s, e

if __name__ == '__main__':
    cases = [
        ( [ [[1, 3], [3, 6]] ], 5),
        [ [ [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]] ], 16],
        [ [ [[1, 2], [1, 2], [1, 2], [1, 2]] ], 1],
        [ [ [[1, 2], [5, 6], [3, 4]], ], 3],
        [ [ [[1, 2], [2, 3], [3, 4]], ], 3],
        [ [ [[5, 10], [1, 2], [2, 3], [3, 4]], ], 8],
        [ [ [[5, 7], [4, 5], [2, 4], ]], 5],
    ]

    import test
    test.test(answer, cases)
