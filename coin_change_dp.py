#!/usr/bin/env python2
# Problem: Coin Change
# Dynamic Programming:

# NOTE: This is not a greedy problem
# Consider

inf = float('inf')

amount = 76
denominations = [1, 5, 10, 25]

class CoinChange(object):

    def __init__(self, amount, denominations):
        self.amount = amount
        self.denominations = denominations

    def reset_cache(self):
        self.cache = [inf] * self.amount  # NOTE: Important to Initialize Cache
        self.cache[0] = 0

    def find_min_path(self, residual_amount):
        self.reset_cache()

        minlen = self.find_min_len_of_path(residual_amount)
        path = self.find_path()
        print 'Path:', path
        return minlen

    def find_path(self):
        i = self.amount-1
        stack = list()

        while (i>0):
            min_val = inf
            best_d = inf

            for d in self.denominations:
                val = self.cache[i - d]
                if val < min_val:
                    min_val = val
                    best_d = d
            i = i - best_d
            stack.append(best_d)

        return stack[::-1]

    def find_min_len_of_path(self, residual_amount):
        if residual_amount < 0:
            return inf

        if self.cache[residual_amount] == inf:
            if residual_amount in self.denominations:
                self.cache[residual_amount] = 1
            else:
                min_len = inf
                for d in self.denominations:
                    path_len = self.find_min_len_of_path(residual_amount - d) + 1
                    if path_len < min_len:
                        min_len = path_len
                self.cache[residual_amount] = min_len

        return self.cache[residual_amount]

    # def find_min_len_of_path_iter(self, residual_amount):
    #     if residual_amount < 0:
    #         return inf
    #
    #     if self.cache[residual_amount] == inf:
    #         if residual_amount in self.denominations:
    #             self.cache[residual_amount] = 1
    #         else:
    #             min_len = inf
    #             for d in self.denominations:
    #                 path_len = self.find_min_len_of_path(residual_amount - d) + 1
    #                 if path_len < min_len:
    #                     min_len = path_len
    #             self.cache[residual_amount] = min_len
    #
    #     return self.cache[residual_amount]


def main():
    cc = CoinChange(amount+1, denominations)
    cc.find_min_path(amount)
    # for i in range(amount+1):
    #     print 'Amount: %d -> Coins: %0.0f' % (i, cc.find_min_path(i))

if __name__ == '__main__':
    main()
