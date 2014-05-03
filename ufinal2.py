import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math as m
dt=input("Numero de cargas")
j=np.zeros((dt,4))	# it show the coordinates of each charge, the last row indicates charge's sign
n=-1			# n will help us to identify the n charges (from 0 to n-1)
fig = plt.figure()	#Axes Definition and Graph start point
ax = Axes3D(fig)
for dot in range (dt):	#locating charges
	print dot
	x=input("x:")
	y=input("y:")
	z=input("z:")
	e=input("Qn:")
	n+=1
	j[n,0],j[n,1],j[n,2],j[n,3]=x,y,z,(e)	
        if (e<=0):			
		ax.scatter(x, y, z, color="#15cc55", s=2500, lw=1, alpha=0.7)	#negative charges
	else:					
		ax.scatter(x, y, z, colo r="#E50A15", s=1500, lw=1, alpha=0.7)	#positive charges

o=(m.factorial(dt))/(m.factorial(2)*m.factorial(dt-2))	#All the possible distances between the charges
d=np.zeros((o,1))
i=-1
for k in range (dt):
	for h in range (k+1,dt):				#combining the charges
		i+=1						#Pythagorean Theorem
		d[i]=(((j[k,0]-j[h,0])**2+(j[k,1]-j[h,1])**2+(j[k,2]-j[h,2])**2)**0.5)*(j[k,3]*j[h,3]) 
# print d, it shows the distance and the sign between all the cahrges, you can enabled to understand better
u=sum(1/d)
print u
ax.set_xlabel('$X$')
ax.set_ylabel('$Y$')
ax.set_zlabel('$Z$')
ax.set_title("$E_p$="+str(u)+"$k$", style="oblique")
#Plot a DotCube
plt.show()
