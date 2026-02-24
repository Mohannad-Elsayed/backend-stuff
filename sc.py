n, a, b = map(int, list(input().split()))
ans = 0
for i in range(n):
    for j in range(n):
        x, y, cnt, f = i, j, 20, 0
        for _ in range(cnt):
            t = a*y + b*x
            f |= t % n == 0
            y = t
            x = y
        ans += f == 0

print(ans)