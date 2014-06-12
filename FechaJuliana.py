import sys
k=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

y=int(raw_input("insert the year with all the digits > "))
m=int(raw_input("insert month > "))
if m>12:
    print "A year only has 12 months, fool"
    sys.exit()
d=int(raw_input("insert day > "))

J=367*y-((7*(y+(m+9)/12))/4)-((3*((y+(m-9)/7)/100+1))/4)+275*m/9+d+1721029

print "The Julian Date for the noon of", k[m-1], d,",", y, "is ",J
