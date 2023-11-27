n, k = map(int, input().split())

vals = []
for i in range(n):
    f, b = map(int, input().split())
    vals.append((i + 1, f * 4 + b))
    

print(" ".join(map(str, sorted(map(lambda x: x[0], sorted(vals, key=lambda x: x[1], reverse=True)[:k])))))