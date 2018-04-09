#!/usr/bin/env python2
# Problem: String Reverse with Multiple Paranthesis


def reverse_paranthesis_strings(instr):
    useStack = False
    stack = list()
    queue = list()

    for c in instr:
        print '\nDebug: c:', c
        if c == '(':
            useStack = useStack ^ True  # XOR to flip-flop
            print 'UseStack:', useStack

        if useStack:
            # Special Param Handling
            if c == '(':
                c = ')'
            elif c == ')':
                c = '('
            stack.append(c)
        else:
            queue.append(c)

        if (c == '(' and useStack == True) or (c == ')' and useStack == False):
            useStack = useStack ^ True  # XOR to flip-flop
            print 'UseStack:', useStack

        print 'Stack:', stack
        print 'Queue:', queue

    outstr = ''.join(queue)
    outstr += ''.join(stack[::-1])

    return outstr


def main():

    test_params = [
        # ('(abcde)', '(edcba)'),
        ('(abc(de))', '((de)cba)'),
        # ('(abc(de(fg)))', '(((gf)de)cba)'),
        ]

    for instr, outstr in test_params:
        result = reverse_paranthesis_strings(instr)
        print '%s -> %s; Found: %s' % (instr, outstr, result)
        assert result == outstr

if __name__ == '__main__':
    main()
