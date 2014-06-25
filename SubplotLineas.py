import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import math as m
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import scipy.misc as sc


a=input("Distancia a entre las cargas (Metros)")	
e=input("Valor de la carga (Coulombs)")
t=input("Numero de cargas por arista")	
nc=t**3								# Number of charges
j=np.zeros((nc,3))						# it shows the coordinates of each charge
m=np.zeros((nc,1))						# it indicates charge's sign
k=8.98*10**9
										
fig = plt.figure()
dd=(sc.factorial(t+2)/(sc.factorial(3)*sc.factorial(t-1)))-1	#This is the diferent distances possible between the charges,...
								#...combination with repetition: (n+r-1)!/r!(n-1)!
n=-1								#locating charges
for x in range (t):				
	for y in range (t):
    		for z in range (t):
			n+=1
			j[n,0],j[n,1],j[n,2],m[n]=x*a,y*a,z*a,(-((-1)**n)*e)	

if dd==3:
	ax1=fig.add_subplot(2,2,1, projection='3d')
	ax2=fig.add_subplot(2,2,2, projection='3d')
	ax3=fig.add_subplot(2,2,3, projection='3d')
if dd==9:
	ax1=fig.add_subplot(3,3,1, projection='3d')
	ax2=fig.add_subplot(3,3,2, projection='3d')
	ax3=fig.add_subplot(3,3,3, projection='3d')
	ax4=fig.add_subplot(3,3,4, projection='3d')
	ax5=fig.add_subplot(3,3,5, projection='3d')
	ax6=fig.add_subplot(3,3,6, projection='3d')
	ax7=fig.add_subplot(3,3,7, projection='3d')
	ax8=fig.add_subplot(3,3,8, projection='3d')
	ax9=fig.add_subplot(3,3,9, projection='3d')
							
c=sc.comb(nc,2)							#combinatorial function, n!/(n-2)!2!
f=np.zeros((c,1))						#Distances
i=-1									
for k in range (nc):										#k is the first dot and h is the second one
	for h in range (k+1,nc):										#combining the charges
		f[i,0]=(((j[k,0]-j[h,0])**2+(j[k,1]-j[h,1])**2+(j[k,2]-j[h,2])**2)**0.5)*(m[k]*m[h]) 	#Pythagorean Theorem		
		if (dd==3 or dd==9):
			if (abs(f[i,0])==a):			
				ax1.plot([j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]])	
			elif (abs(f[i,0])==a*2**(0.5)):			
				ax2.plot([j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]])
			elif (abs(f[i,0])==a*3**(0.5)):			
				ax3.plot([j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]])
		if (dd==9):
			if (abs(f[i,0])==2*a):			
				ax4.plot([j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]])
			elif (abs(f[i,0])==a*5**(0.5)):			
				ax5.plot([j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]])
			elif (abs(f[i,0])==a*6**(0.5)):			
				ax6.plot([j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]])
			elif (abs(f[i,0])==3*a):			
				ax7.plot([j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]])
			elif (abs(f[i,0])==2*a*2**(0.5)):			
				ax8.plot([j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]])
			elif (abs(f[i,0])==a*12**(0.5)):			
				ax9.plot([j[k,0],j[h,0]],[j[k,1],j[h,1]],[j[k,2],j[h,2]])		
		i+=1	

u=sum(1/f)
plt.show()
