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
        self.denominations = denominations
        self.cache = [inf] * amount  # NOTE: Important to Initialize Cache

    def find_min_path(self, residual_amount):
        if residual_amount < 0:
            return inf

        # print 'Res:', residual_amount
        # import ipdb; ipdb.set_trace()
        if self.cache[residual_amount] == inf:
            if residual_amount in self.denominations:
                self.cache[residual_amount] = 1
            else:
                min_len = inf
                for d in self.denominations:
                    path_len = self.find_min_path(residual_amount - d) + 1
                    if path_len < min_len:
                        min_len = path_len
                self.cache[residual_amount] = min_len

        return self.cache[residual_amount]

def main():
    cc = CoinChange(amount+1, denominations)
    for i in range(amount+1):
        print 'Amount: %d -> Coins: %0.0f' % (i, cc.find_min_path(i))

if __name__ == '__main__':
    main()
