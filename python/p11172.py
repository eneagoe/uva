def relational_operator(a, b):
    if a == b:
        return '='
    elif a > b:
        return '>'
    else:
        return '<'

out = []
t = int(input())

for _ in range(t):
    a, b = input().split()
    out.append(relational_operator(int(a), int(b)))

for r in out:
    print(r)
