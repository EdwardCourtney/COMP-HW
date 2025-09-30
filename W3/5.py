m, n = map(int, input().split())
ans = m//n
if (m%n != 0):
    ans += 1
print (ans)