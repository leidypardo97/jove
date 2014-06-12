n=int(raw_input("Insert your number > "))
m=int(raw_input("To make an integer a binarie write 0, to make a binary an integer write 1 > "))

j=[]
a=[]
i=[]
p=[]

if m==0:
    while n>0:
        t=n%2
        j.append(t)
        n=n/2
    for x in range(len(j)):
        i.append(j[x]*(10**x))
    print sum(i)   

if m==1:
    for x in range(len(str(n))):
        k=n/(10**x)
        a.append(k)
    
    a.reverse()
    for x in range(len(a)):
        a[x]=(a[x]/10.0)
    a=[int(((x-int(x))+0.01)*10) for x in a]
    a.reverse()
    count=0
    for x in range(len(a)):
        p.append(a[x]*(2**count))
        count=count+1
    print sum(p)    
