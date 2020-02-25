n=int(input("Enter a number: "))
while True:
    n=n*3+1
    i=1
    sum=0
    while True:
        sum=sum+(n%(10**i)-n%(10**(i-1)))//10**(i-1)
        if n%(10**i)== n:
            break
        i=i+1
    n=sum
    if ((n%10-n%1)/1) == n:
        break
print(n)


