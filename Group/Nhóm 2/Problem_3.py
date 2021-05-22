n, m = [int(x) for x in input().split()]
a = list(map(int, input().split()))
a.sort(reverse=True)

low = 0
high = max(a)

while (low < high):
    mid = (low + high + 1) // 2
    s = 0
    for i in range(n):
        s = s + max(0, a[i] - mid)
    if s < m:
        high = mid - 1
    else:
        low = mid

print(low)