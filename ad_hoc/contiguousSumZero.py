#!/usr/bin/env python2

# Problem Definition: https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/

import unittest

def sumZero(arr):
    sums = {}  # Running-sum: [idx] pairs
    sum = 0
    output = []

    for i, v in enumerate(arr):
        sum += v

        # Special Case: Add zero to sums so that output array can be formed
        if v == 0 and 0 not in sums:
            sums[0] = [i]

        # If zero sum found (collision of keys); Add to  range (start.idx, i) output
        for idx in sums.get(sum, []):
            output.append(arr[idx:i+1])  # range includes current index, hence sliced to i+1

        # Lastly, include current index as a potential start.idx for future computation
        sums[sum] = sums.get(sum, []) + [i+1]    # range starts from next index, hence i+1

    return output


tests = [
    [0, 0], # Med
    [0], # Trivial
    [1, 0, 2, 3, -5], # Hard
    [0, 1, 2, 3, 4, -10], # Hard
    [1, 2, 3], # Trivial
    [1, 2, 5, -7], # Med
    [0, 0, 1, -1], # Hard
]
expected = [
    [[0], [0, 0], [0]],
    [[0]],
    [[0], [0, 2, 3, -5], [2, 3, -5]],
    [[0], [0, 1, 2, 3, 4, -10], [1, 2, 3, 4, -10]],
    [],
    [[2, 5, -7]],
    [[0], [0, 0], [0], [0, 0, 1, -1], [0, 1, -1], [1, -1]]
]

class MyTest(unittest.TestCase):

    def _test_case(self, case):
        result = sumZero(tests[case])
        self.assertListEqual(result, expected[case])

    @unittest.skip('Running Indivial Tests in lieu of this to aid debugging')
    def test_everything(self):
        for i in range(len(tests)):
            self._test_case(i)

    def test_case_0(self):
        self._test_case(0)

    def test_case_1(self):
        self._test_case(1)

    def test_case_2(self):
        self._test_case(2)

    def test_case_3(self):
        self._test_case(3)

    def test_case_4(self):
        self._test_case(4)

    def test_case_5(self):
        self._test_case(5)

    def test_case_6(self):
        self._test_case(6)

if __name__ == '__main__':
    unittest.main()
