numlist = []

for x in range(1,1000):
    num = x**x
    numlist.append(num)

finalnum = str(sum(numlist))

ans = finalnum[-10:]
print(ans)

