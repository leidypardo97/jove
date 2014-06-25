import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import math as m
import scipy.misc as sc


a=input("Distancia a entre las cargas (Metros)")		
e=input("Valor de la carga (Coulombs)")
t=input("Numero de cargas por arista")	
nc=t**3								# Number of charges
j=np.zeros((nc,3))						# it shows the coordinates of each charge
m=np.zeros((nc,1))						# it indicates charge's sign
k=8.98*10**9										


fig = plt.figure()

ax=fig.add_subplot(1,2,1, projection='3d')			#Plot a dot cube

ax.set_title("$Cristal cubico$",fontsize=20)
scatter1=lines.Line2D([0],[0],linestyle="none",marker='o',color="#15cc55")
scatter2=lines.Line2D([0],[0],linestyle="none",marker='o',color="#483d8b")
ax.legend([scatter1,scatter2],['Anion','Cation'],numpoints=1)


n=-1								#locating charges
for x in range (t):				
	for y in range (t):
    		for z in range (t):
			n+=1
			j[n,0],j[n,1],j[n,2],m[n]=x*a,y*a,z*a,(-((-1)**n)*e)	
            		if ((x+y+z)%2==0):			
				scatter1=ax.scatter(x*a, y*a, z*a, color="#15cc55", s=800, alpha=0.7) #negative charges, green
			else:					
				scatter2=ax.scatter(x*a, y*a, z*a, color="#483d8b", s=600, alpha=0.7) #positive charges, purple

ax=fig.add_subplot(1,2,2, projection='3d')			#Plot lines between dots 						
c=sc.comb(nc,2)							#combinatorial function, n!/(n-2)!2!
f=np.zeros((c,1))
i=-1												
for k in range (nc):						#k is the first dot and h is the second one
	for h in range (k+1,nc):									#combining the charges
		f[i,0]=(((j[k,0]-j[h,0])**2+(j[k,1]-j[h,1])**2+(j[k,2]-j[h,2])**2)**0.5)*(m[k]*m[h]) 	#Pythagorean Theorem
		ax.plot([j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]])				#Drawing lines between charges
		i+=1	

u=sum(1/f)							#Potential Energy, U=k*Q_1*Q_2/d	
ax.set_title("$E_p=$"+str(u)+"$k$",fontsize=20)	

#Plot
plt.show()
