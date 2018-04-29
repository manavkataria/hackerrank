#!/usr/bin/env python2

def isMatchRecurse(t, p, prev):
    print '\nT:%s \nP:%s \nprev=%s' % (t, p, prev)

    # Base
    if len(t) == 0 and len(p) == 0:
        return True

    # Transition
    flag = False

    if p[0] != '*':
        if t[0] == p[0]:
            prev = p[0]
            print 'Both Consumed'
            try:
                flag = flag or isMatchRecurse(t[1:], p[1:], prev)
            except IndexError:
                flag = False
        elif p[0] == '.':
            print 'Both Consumed'
            try:
                flag = flag or isMatchRecurse(t[1:], p[1:], prev)
            except IndexError:
                flag = False
        elif len(p) > 2 and p[1] == '*':
            prev = p[0]
            print 'P Consumed'
            flag = flag or isMatchRecurse(t, p[1:], prev)
        else:
            flag = False
    else: # p[0] = '*'
        print 'p[0]', p[0]
        try:
            print 'T[0]', t[0]
        except IndexError as e:
            print 'IndexError', e
        if len(t) == 0 and p[0] == '*':
            try:
                print 'P Consumed'
                flag = flag or isMatchRecurse(t, p[1:], prev)
            except IndexError:
                flag = False
        elif t[0] == prev:
            try:
                print 'T Consumed'
                flag = flag or isMatchRecurse(t[1:], p, prev=t[0])
            except IndexError:
                flag = False
        else:
            try:
                print 'P Consumed'
                flag = flag or isMatchRecurse(t, p[1:], prev)
            except IndexError:
                flag = False
    return flag

def isMatchRecurseFactored(t, i, p, j, prev):
    # Guard
    if i > len(t) or j > len(t):
        return False

    t = t[i:]
    p = p[j:]
    # import ipdb; ipdb.set_trace()
    print '\nT:%s \nP:%s \nprev=%s' % (t, p, prev)

    # Base
    if len(t) == 0 and len(p) == 0:
        return True

    # Transition
    flag = False

    if p[0] != '*':
        if t[0] == p[0]:
            prev = p[0]
            print 'Both Consumed'
            flag = flag or isMatchRecurseFactored(t, i+1, p, j+1, prev)
        elif p[0] == '.':
            print 'Both Consumed'
            flag = flag or isMatchRecurseFactored(t, i+1, p, j+1, prev)
        elif len(p) > 2 and p[1] == '*':
            prev = p[0]
            print 'P Consumed'
            flag = flag or isMatchRecurseFactored(t, i, p, j+1, prev)
        else:
            flag = False
    else: # p[0] = '*'
        if len(t) == 0 and p[0] == '*':
            print 'P Consumed'
            flag = flag or isMatchRecurseFactored(t, i, p, j+1, prev)
        elif t[0] == prev:
            print 'T Consumed'
            flag = flag or isMatchRecurseFactored(t, i+1, p, j, prev)
        else:
            print 'P Consumed p:%s, t:%s' % (p, t)
            flag = flag or isMatchRecurseFactored(t, i, p, j+1, prev)
    return flag


def isMatch(strText, strPattern):
    t = strText
    p = strPattern
    prev = None

    # return isMatchRecurse(t, p, prev)
    i = j = 0
    return isMatchRecurseFactored(t, i, p, j, prev)

def main():
    t = 'abbc'
    p = '*.b*c*'

    res = isMatch(t, p)
    print '\nResult:', res

if __name__ == '__main__':
    main()
