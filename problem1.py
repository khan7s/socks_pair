def pile():

    n = int(input("Enter the no. of socks in pile: "))

    a = []
    for i in range(0,n):
        a.append(int(input()))
    a.sort()
#checking the pairs of socks with same colors
    count = 0
    for i in range(n+1):
        try:
            if a[i]==a[i+1]:
                a.pop(i)
                a.pop(i+1)
                count+=1

        except:
            pass
    print(count)
pile()
