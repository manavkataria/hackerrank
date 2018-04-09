#!/usr/bin/env python2

# Generate All Subsets in
# 1. Recursive Inverse Lexicographical Order
# 2. Recursive Lexicographical Order
# 3. Iterative using binary strings; Arbitrary Order
# 4. Iterative using binary strings; Inverse Lexicographical Order

def make_subset_from_bitstring(num, s):
    result = ''
    binstr = '{num:{fill}{width}b}'.format(num=num, fill='0', width=len(s))
    # binstr = bin(num)[2:]  # Weaker Alternative

    for i, c in enumerate(s):
        # bitchar = binstr[-i]  # Arbitrary Order
        bitchar = binstr[i]  # Inverse Lexicographical Order
        if bitchar == '1':
            result += c

    return result

def subsets_iterative(s):
    n = len(s)

    result = list()
    for i in range(2**n):
        subset = make_subset_from_bitstring(i, s)
        result.append(subset)

    return result

def subsets(s, left):
    results = []
    print 'State: s(%s), left(%s)' % (s, left)

    if len(left) == 0:
        print 'Subset Leaf:', s
        return [s]

    results.extend(subsets(s, left[1:]))
    results.extend(subsets(s + left[0], left[1:]))

    return results


def subsets_result_reference_in_state(s, left, results):
    # print 'State: s(%s), left(%s), result(%s)' % (s, left, results)

    if len(left) == 0:
        # print 'Subset Leaf:', s
        results += [s]
        return

    subsets_result_reference_in_state(s, left[1:], results)
    subsets_result_reference_in_state(s + left[0], left[1:], results)


def generate_all_subsets(s):
    results = list()
    # subsets1('', s, results)
    # results = subsets('', s)        # Output in Inverse Lexicographical Order
    # results = subsets('', s[::-1])  # Output in Lexicographical Order
    results = subsets_iterative(s)

    return results


print generate_all_subsets('abc')
