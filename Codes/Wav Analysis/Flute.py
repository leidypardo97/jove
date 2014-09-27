from scipy.io.wavfile import read
import matplotlib.pyplot as plt

#Audio 1 read
input_data1 =read("lbursts1.wav")
audio1 = input_data1[1]

#Plot data
plt.plot (audio1[0:1024],'r')


plt.ylabel("Amplitude")
plt.xlabel("Time (Samples)")

plt.title("Flute")

plt.show()
