#import glob
#import os
import wave
import contextlib
import scipy
from pylab import*
#from getpass import getuser
import numpy as np
import math
from scipy.io import wavfile
from scipy.signal import hann
from scipy.fftpack import rfft
import matplotlib.pyplot as plt
from Tkinter import Tk
from tkFileDialog import askopenfilename

#Graphic Mode
Tk().withdraw()
fname = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print "File Selected: "+fname


#fname="/home/edwmapa/jove/Sample Data/"+files[var]
#File Duration frames/rate
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    print "File length: %f Sec."%duration


def graphOne(whichFile):
	#wavfile.read() returns rate and data in numpy array
	input_data=wavfile.read(whichFile)
	sampFreq, snd = input_data

	snd = snd / (2.**15)
	print "This is the shape of the sound (sample points, chanels sound):"
	print(snd.shape)

	#If the sound has more than one channel, only load first channel
	if len(snd.shape)!=1:
	    snd=snd[:,0]

	#Arange of ms
	samplePoints=snd.shape[0]
	timeArray = arange(0,float(snd.shape[0]), 1)
	timeArray = timeArray / sampFreq

	maxV=(np.amax(snd))+.05  #Max Value of snd
	minV=(np.amin(snd))-.05
	#yDuration
	yduration = np.array(duration)
	yduration = np.repeat(yduration,2)

	plt.figure(figsize=(20,10))
	plt.plot(timeArray,snd,'b',label="Signal")
	plt.plot(yduration,np.linspace(minV,maxV, 2),"r--",label="Limit") #Limit line
	plt.ylim(-maxV,maxV)
	plt.legend()
	plt.title("File: "+fname)
	plt.ylabel('Amplitude',size=30)
	plt.xlabel('Time (sec.)',size=30)
	plt.show()

	##############################################################################
	plt.figure(figsize=(20,10))
	plt.hist(snd, bins=200)
	xlabel('Amplitude',size=30)
	ylabel('Times Repeated',size=30)
	plt.show()

def graphTwo(whichFile):
	input_data1 =wavfile.read(whichFile)
	audio1 = input_data1[1]

	#Sampling
	samp=2048

	#Here we check the sound shape. We cant work with the sound if th sound has more than one channel.
	if len(audio1.shape)!=1:
	    audio1=audio1[:,0]
	    
	#Hanning window
	window=hann(samp)
	audio1 = audio1[0:samp] * window

	#Fast Fourier Transform fft
	mags= abs(rfft(audio1))

	#dB values
	mags= 20 * scipy.log10(mags)
	#To 0 dB, set max mags to zero
	mags -=max(mags)

	#plot
	plt.figure(figsize=(20,10))
	plt.plot(mags, label="Graph")
	ylabel("Magnitude $(dB)$", size =30)
	xlabel("Frequency Bin", size=30)
	plt.legend()
	plt.title("Flute Spectrum", size=30)
	plt.show()


optRead=input("Choose a graph: 1() or 2()")
if optRead<0 or optRead>2 :
    raise ValueError("No valid argument")

if (optRead==1):
	graphOne(fname)
elif(optRead==2):
	graphTwo(fname)