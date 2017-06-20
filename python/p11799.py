out = []
t = int(input())

for _ in range(t):
    out.append(max(int(i) for i in input().split()))

for idx, m in enumerate(out):
    print("Case %d: %d" % (idx + 1, m))
