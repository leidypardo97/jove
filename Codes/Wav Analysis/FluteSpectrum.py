import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft

import matplotlib.pyplot as plt


#Audio 1 read
input_data1 =read("lbursts1.wav")
audio1 = input_data1[1]

#Hanning window 
window=hann(1024)
audio1 = audio1[0:1024] * window

#Fast Fourier Transform fft
mags= abs(rfft(audio1))

#dB values
mags= 20 * scipy.log10(mags)
#To 0 dB, set max mags to zero
mags -=max(mags)

#plot
plt.plot(mags)
plt.ylabel("Magnitude (db)")
plt.xlabel("Frequency Bin")

plt.title("Flute Spectrum")

plt.show()