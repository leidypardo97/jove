import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math as m
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import scipy.misc as sc

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1,2,1, projection='3d') 	
ax.set_title("$Cristal cubico$",fontsize=20)
scatter1=lines.Line2D([0],[0],linestyle="none",marker='o',color="#ffff00")
scatter2=lines.Line2D([0],[0],linestyle="none",marker='o',color="#483d8b")
ax.legend([scatter1,scatter2],['Cation','Anion'],numpoints=1)

dt=input("Numero de cargas")
j=np.zeros((dt,4))	# it show the coordinates of each charge, the last row indicates charge's sign
n=-1			# n will help us to identify the n charges (from 0 to n-1)

for dot in range (dt):	#locating charges
	print dot
	x=input("x:")
	y=input("y:")
	z=input("z:")
	e=input("Qn:")
	n+=1
	j[n,0],j[n,1],j[n,2],j[n,3]=x,y,z,(e)	
        if (e<=0):			
		ax.scatter(x, y, z, color="#483d8b", s=2500, lw=1, alpha=0.7)	#negative charges, purple
	else:					
		ax.scatter(x, y, z, color="#ffff00", s=1500, lw=1, alpha=0.7)	#positive charges, yellow

o=(m.factorial(dt))/(m.factorial(dt-2)*m.factorial(2))	#All the possible distances between the charges (dt)!/(dt-2)!*2!
d=np.zeros((o,1))
i=-1
ax = fig.add_subplot(1,2,2, projection='3d')
for k in range (dt):
	for h in range (k+1,dt):				#combining the charges
		i+=1						#Pythagorean Theorem
		d[i]=(((j[k,0]-j[h,0])**2+(j[k,1]-j[h,1])**2+(j[k,2]-j[h,2])**2)**0.5)*(j[k,3]*j[h,3]) 
		p,s,t=[j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]]
		ax.plot(p,s,t)
		
u=sum(1/d)
ax.set_title("$E_p=$"+str(u)+"$k$",fontsize=20)	
plt.show()
