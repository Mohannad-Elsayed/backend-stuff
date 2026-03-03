import sys, heapq
from collections import Counter

class TopK:
    __slots__ = ("k", "big", "small", "db", "ds", "sb")
    def __init__(self, k=0):
        self.k = k
        self.big = []
        self.small = []
        self.db = Counter()
        self.ds = Counter()
        self.sb = 0
    def _prune_big(self):
        while self.big and self.db[self.big[0]]:
            v = heapq.heappop(self.big)
            self.db[v] -= 1
    def _prune_small(self):
        while self.small and self.ds[-self.small[0]]:
            v = -heapq.heappop(self.small)
            self.ds[v] -= 1
    def _fix(self):
        self._prune_big()
        self._prune_small()
        while len(self.big) > self.k:
            self._prune_big()
            if not self.big:
                break
            v = heapq.heappop(self.big)
            self.sb -= v
            heapq.heappush(self.small, -v)
            self._prune_big()
        while len(self.big) < self.k:
            self._prune_small()
            if not self.small:
                break
            
            v = -heapq.heappop(self.small)
            heapq.heappush(self.big, v)
            self.sb += v
            self._prune_small()
        self._prune_big()
        self._prune_small()
        while self.big and self.small:
            self._prune_big()
            self._prune_small()
            if not self.big or not self.small:
                break
            if self.big[0] >= -self.small[0]:
                break
            a = heapq.heappop(self.big)
            b = -heapq.heappop(self.small)
            self.sb += b - a
            heapq.heappush(self.big, b)
            heapq.heappush(self.small, -a)
    def set_k(self, k):
        self.k = k
        self._fix()
    def add(self, x):
        heapq.heappush(self.big, x)
        self.sb += x
        self._fix()
    def sumk(self):
        self._fix()
        return self.sb if len(self.big) == self.k else None

INF = 10**30
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [[] for _ in range(n+2)]
    for _ in range(n):
        x, y = map(int, input().split())
        a[y + 1].append(x)
    tk = TopK(0)
    res = 0
    B = [-INF] * (n+2)
    for k in range(n+1, 0, -1):
        for x in a[k]:tk.add(x)
        tk.set_k(k)
        sk = tk.sumk()
        if sk is not None:
            if sk > res:
                res = sk
        tk.set_k(k - 1)
        skB = tk.sumk()
        if skB is not None:
            B[k] = skB
    pre = [-INF] * (n+2)
    cur = -INF
    for k in range(1, n+2):
        if B[k] > cur:
            cur = B[k]
        pre[k] = cur
    out = []
    for _ in range(m):
        x, y = map(int, input().split())
        c = y + 1
        ans = res
        if pre[c] > -INF//2:
            v = x + pre[c]
            if v > ans:
                ans = v
        print(ans,end=' ')
    print()
