from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np


# read audio samples
input_data= wavfile.read('grilloa.wav')
audio = input_data[1]
l=len(audio)
audio_l=np.vstack(audio[0:l,0])
#audio_r=np.vstack(audio[0:l,1])


#Delete interference. #To improve: look up in the book, clean EMI for all records.
alw=np.vstack((audio_l[0:320630],audio_l[395840:589891]))			 #Audio Left channel without interference
count=np.vstack(np.arange(len(alw)))
alwc=np.hstack((count,alw))							# The first column indicates the time
										# To improve, converte them into seconds

n=0
for x in range (len(alwc)):							# Find out the number of maximum over the threshold
	if (alwc[x,1]>8500 and alwc[x-1,1]<alwc[x,1]>alwc[x+1,1]):
		n+=1	
e=0
det=np.zeros((n,32))								# Determine which maximum have spike shape
for x in range (len(alwc)):
	if (alwc[x,1]>8500 and alwc[x-1,1]<alwc[x,1]>alwc[x+1,1]):		
		det[e]=np.hstack((0,alwc[x,0],alwc[x:x+30,1]))
		e+=1

for x in range (n):
	for y in range (2,32):
		if (det[x,y]<-5000):
			det[x,0]=1

aus=np.zeros((9,220))								#Save data around the spike 
cansada=0									# To improve: the 9 only works in this record
for x in range (n):			
	if(det[x,0]==1):
		aus[cansada]=np.hstack((alwc[det[x,1]-110:det[x,1]+110,1]))
		cansada+=1

aus_plot=aus.transpose()
							
ax1= plt.subplot(1,1,1)
ax1.plot(aus_plot)
plt.grid()
plt.show()
