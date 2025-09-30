a = int(input())
ans = 0
if (a <= 50):
    ans = a*1500
elif (a <= 100):
    ans += (a-50)*2000 + 50*1500
else:
    ans += (a-100)*3000 + 50*1500 + 50*2000
print(ans)