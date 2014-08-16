"""
Author: Alejandro Cardenas-Avendano

email: alejandro.cardenasa@konradlorenz.edu.co
Website: https://github.com/alejandroc137
License: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""


from scipy.io import wavfile
import matplotlib.pyplot as plt

# read audio samples
input_data= wavfile.read("Yamaha.wav")
audio = input_data[1]
# plot the first 1024 samples
plt.plot(audio[0:100])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time (samples)")
# set the title
plt.title("Flute Sample")
# display the plot
plt.show()