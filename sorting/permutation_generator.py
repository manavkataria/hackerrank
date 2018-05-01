#!/usr/bin/env python2

def permutation_generator(input):
    """ Approach:
        Loop right to left
            find inversion index pairs (i-1, i)
                if found: swap (arr[i-1], X)
                    where X = smallest value in arr[i:] > arr[i-1]
                reverse (inplace) arr[i:]
                return array
    """

    for i in range(len(input)-1, 0, -1):
        if input[i-1] < input[i]:
            # find index of smallest value greater than input[i-1] in input[i:]
            # NOTE: Alternatively: Loop (starting from right) to find the idx, val
            filtered = [(j,x) for (j,x) in enumerate(input[i:]) if x > input[i-1]]
            idx, val = min(filtered, key=lambda (j, x): x)

            input[i-1], input[i+idx] = input[i+idx], input[i-1]  # Swap
            input[i:] = input[i:][::-1]  # Reverse Inplace

            return input

    return None


# Test Cases:
input_list = [[1,2,3],
              [1,3,2],
              [3,2,1],
              ['a','c','b']
              ]
expected_list = [[1,3,2],
                 [2,1,3],
                 None,
                 ['b','a','c']
                 ]

# Important Test Cases
for input, expected in zip(input_list, expected_list):
    output = permutation_generator(input)
    assert output == expected, '%s != %s' %(output, expected)

# Full Permutation Test
input = ['a','b','c']
while (input is not None):
    print input
    input = permutation_generator(input)
