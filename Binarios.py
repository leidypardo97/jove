print "If You Find any Bug, Please Tell me What is :)"
n=int(raw_input("Insert your number > "))
time=raw_input("Does your number have decimal part? (y/n) > ")
if time=="y":
    mov=int(raw_input("Please Insert the Decimal Part without comma i.e. 101010.0101=0101 > "))
m=int(raw_input("To make an integer a binarie write 0, to make a binary an integer write 1 > "))

j=[]
a=[]
i=[]
r=[]
p=[]

if m==0:
    while n>0:
        t=n%2
        j.append(t)
        n=n/2
    for x in range(len(j)):
        i.append(j[x]*(10**x))
    
    mov=mov*(10**(-len(str(mov))))
    while mov!=1.0:
        mov=mov-int(mov)
        mov=mov*2
        if mov>=1.0:
            r.append(1)
        if mov<1.0:
            r.append(0)
    r=[str(x) for x in r]
    print int("".join(r))
    print str(sum(i))+"."+"".join(r)   

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
    
    lol=len(str(mov))
    aus=[]
    healer=[]
    for x in xrange(0, lol):
        rain=mov/(10**x)
        aus.append(rain)
   
    aus.reverse()
    for x in xrange(len(aus)):
        aus[x]=(aus[x]/10.0)
    aus=[int(((x-int(x))+0.01)*10) for x in aus]
    for x in range(len(aus)):
        healer.append(aus[x]*(2**(-(x+1))))
    print sum(p)+sum(healer)    
