#d(n) = sum of numbers less than n which divide evenly into n
#d(a) = b and d(b) = a: b and a  are amicable numbers

#evaluate the sum of all amicable numbes under 10,000

amicable_list = []

def amicable(x):
    sumlist = []
    for i in range (1, int(x/2) + 1):
        if x%i == 0:
            sumlist.append(i)
    return sum(sumlist)

for x in range (1, 10000):
    num = amicable(x)
    if amicable(num) == x:
        #amicable_list.append(x)
        if num != x:
            amicable_list.append(x)

print(amicable_list)
print(sum(amicable_list))
        
