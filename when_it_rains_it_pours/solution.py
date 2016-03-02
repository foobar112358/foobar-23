def answer(heights):
    total_water = 0
    queue = []

    p = find_peak_in(heights, 0, len(heights) - 1)
    queue.append((0, p, 0))
    queue.append((p, len(heights) - 1, 1))

    while queue:
        l, r, d = queue.pop(0)
        p = find_peak_in(heights, l + d, r + d - 1)
        if p is None:
            continue

        total_water += get_water_in(heights, p, l if d else r)
        if d:
            if p != r:
                queue.append((p, r, 1))
        else:
            if l != p:
                queue.append((l, p, 0))

    return total_water

def get_water_in(heights, s, e):
    if s > e:
        s, e = e, s
    h = min(heights[s], heights[e])
    return h * (e - s - 1) - sum(heights[s + 1:e]) if (e - s > 1) else 0

def find_peak_in(heights, s, e):
    m = 0
    res = None
    for i in xrange(s, e + 1):
        if heights[i] > m:
            m = heights[i]
            res = i
    return res


if __name__=='__main__':
    cases = [
        ([1, 4, 2, 5, 1, 2, 3], 5),
        ([1, 2, 3, 2, 1], 0),
        ([2], 0),
        ([1, 2], 0),
        ([3, 2], 0),
        ([3, 2, 1], 0),
        ([1, 2, 3], 0),
        ([1, 4, 2, 3], 1), #left peak
        ([4, 2, 3], 1), #left peak
        ([3, 1, 4], 2), #right peak
        ([4, 2, 5, 3, 2, 1], 2), #right peak
        ([1, 4, 4, 2, 3, 3, 1], 1), #left flat peak
        ([4, 4, 2, 5, 5, 3, 3, 2, 2, 1], 2), #right flat peak
        ([4, 2, 4, 2, 4, 2, 4, 2, 2, 1], 6), #lots flat peak
        ([1, 4, 1, 3, 2, 3, 4, 4, 5, 7, 3, 4, 5, 6, 2, 3], 14) # complicate
        ]

    for c in cases:
        r = answer(c[0])
        if r == c[1]:
            print '=='
        else:
            print "%s=>%s %s %s" % (c[0], c[1], '==' if r == c[1] else '!=', r)
