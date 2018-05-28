#!/usr/bin/env python2

# Doordash: Delivery Scheduling
# Facebook: Calendar Problem

def getMergedIntervals(arr):
    """
    Steps:
    + Add elements to a calendar(default: 0) with <K:V> as <time: +1/-1 depending upon weather its a start time or end time> | O(N)
    + For each time in sorted(calendar.keys()) | O(N.logN) sorted
        + Merge while count > 0. Else its a new open interval now | O(N)
    """

    calendar = dict()
    for st, et in arr:
        calendar[st] = calendar.get(st, 0) + 1
        calendar[et] = calendar.get(et, 0) - 1

    sortedkeys = sorted(calendar.keys())

    overlap = 0
    st = None
    et = None
    intervals = []
    for t in sortedkeys:
        overlap += calendar[t]
        if overlap > 0:
            if st is None:
                st = t
            # else do nothing; continue growing this meeting

        if overlap == 0:
            et = t
            st = st if st else t  # Handle the case where st = et; 0 length meeting;
            intervals.append((st, et))
            st = None
            et = None

        if overlap < 0:
            raise Exception('Invalid Input!')

    return intervals
