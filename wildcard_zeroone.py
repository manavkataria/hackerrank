#!/usr/bin/python

WILDCARD = '?'

def wildcard(string, i):

    if i > len(string):
        return []

    if i == len(string):
        return [string]

    if string[i] != WILDCARD:
        return wildcard(string, i+1)
    else:
        s = string[:i] + '0' + string[i+1:]
        zero_result = wildcard(s, i+1)
        s = string[:i] + '1' + string[i+1:]
        one_result = wildcard(s, i+1)

        return zero_result + one_result

def find_all_possibilities(s):
    result = wildcard(s, 0)
    return result

result = find_all_possibilities('1??0')

print('\n'.join(result))
