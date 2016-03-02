def answer(str):
    op_stack = []
    result = ''
    for i in str:
        #print i, op_stack,
        if i=='*' or i =='+':
            if op_stack and op_stack[-1] < i:
                #print 'dump all',
                while op_stack and op_stack[-1] < i:
                    result += op_stack.pop()

            op_stack.append(i)

        else:
            result += i

        #print ' op_stack:', op_stack, ' result:', result

    while op_stack:
        result += op_stack.pop()

    return result


if __name__=='__main__':
    cases = [
        ('2+3*2', '232*+'),
        ('2*4*3+9*3+5', '243**93*5++'),
        ('2*4*3+5+9*3+5', '243**593*5+++'),
        ('3+5*4+2+3+4*5*7*9+2', '354*234579***2+++++')
        ]

    for i in ["%s=>%s %s %s" % (c[0], c[1], '==' if answer(c[0]) == c[1] else '!=', answer(c[0]), ) for c in cases]:
        print i
