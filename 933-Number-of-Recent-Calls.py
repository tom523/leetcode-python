# -*- coding: utf-8 -*-
import collections


class RecentCounter(object):

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)
        while self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)


r = RecentCounter()
print r.ping(1)
print r.ping(100)
print r.ping(3001)
print r.ping(3002)
print r.ping(3003)

