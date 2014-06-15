from decimal import *
#print "If You Find any Bug, Please Tell me What is"
n=Decimal(raw_input("Insert your number and press Enter> "))
m=int(raw_input("To make an integer a binarie write 0, to make a binary an integer write 1 and press Enter > "))

j=[]
a=[]
i=[]
r=[]
p=[]
keep=n
n=int(Decimal(n))
if m==0:
    while n>0:
        t=n%2
        j.append(t)
        n=n/2
    for x in range(len(j)):
        i.append(j[x]*(10**x))
    mov=keep%1
    if mov !=0:
        bow=(len(str(mov)))-2
        mov=int(mov*10**bow)
        mov=mov*(10**(-len(str(mov))))
        while mov!=1.0:
            mov=mov-int(mov)
            mov=mov*2
            if mov>=1.0:
                r.append(1)
            if mov<1.0:
                r.append(0)
        r=[str(x) for x in r]
        print keep, "Is", str(sum(i))+"."+"".join(r), "in Binaries"
    else:
        print keep, "Is", str(sum(i)), "in Binaries"
        
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
    lost=[]
    healer=[]
    mov=keep%1
    if mov!=0:
        for x in str(mov):
            lost.append(x)
        for x in xrange(2):
            lost.pop(0)
        pure="".join(lost)
        for x in range(len(pure)):
            healer.append(int(pure[x])*(2**(-(x+1))))
    print n, "Is", sum(p)+sum(healer), "in Decimals"    
