import sys
k=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

mean=int(raw_input("From Normal Date to Julian Date type 0, from Julian Date to Normal Date write 1 > "))

if mean==0:
    y=int(raw_input("insert the year with all the digits > "))
    m=int(raw_input("insert month > "))
    if m>12:
        print "A year only has 12 months"
        sys.exit()
    d=int(raw_input("insert day > "))
    J=367*y-((7*(y+(m+9)/12))/4)-((3*((y+(m-9)/7)/100+1))/4)+275*m/9+d+1721029
    print "The Julian Date for the noon of", k[m-1], d,",", y, "is ",J

if mean==1:
    Q=int(raw_input("Write your Julian Date Here > "))
    z=Q+68569
    a=4*z/146097
    s=z-((146097*a)+3)/4
    u=(4000*(s+1))/1461001
    r=s-(1461*u)/4+31
    f=80*r/2447
    d=r-(2447*f)/80
    g=f/11
    m=f+2-(12*g)
    y=100*(a-49)+u+g
    print "The Corresponding Date for", Q," is:", k[m-1], d,", ", y
