#euler14-Longest Collatz Sequence
chainlist = []
lim = 999999
def collatz():
    #counter starts at 2 for start and end of chain)
    counter = 2
    for x in range(1,lim):
        while x != 1:
            if x % 2 == 0:
                x = x/2
                counter += 1
            if x % 2 != 0 and x != 1:
                x = 3*x + 1
                counter += 1
        chainlist.append(counter)
        counter = 2       
collatz()
maxpos = chainlist.index(max(chainlist)) + 1
print(maxpos)
