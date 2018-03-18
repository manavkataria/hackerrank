#!/usr/bin/env python2

arr = [100, 4, 2, 1, 8, 3, 101, 99, 98, 96, 102, 103]

def main():

    table = set(arr)
    maxlen = 0

    while len(table) > 0:
        key = table.pop()

        # scan left and delete
        leftlen = 0
        rightlen = 0

        backup_key = key

        while 1:
            key -= 1
            if key not in table:
                break
            table.discard(key)
            leftlen += 1

        key = backup_key
        while 1:
            key += 1
            if key not in table:
                break
            table.discard(key)
            rightlen += 1

        maxlen = max(maxlen, leftlen+rightlen+1)

    print maxlen







if __name__ == '__main__':
    main()
