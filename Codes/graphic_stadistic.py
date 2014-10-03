import sys
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *
import tkFileDialog
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import os
import string
import itertools
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import glob
from sklearn import preprocessing
from scipy.constants import Boltzmann as boltzmann

    
def fit(to, be):
    """
    Hello!
    This function makes the best fit for the data by the way of polinomical funtions
    While the integer is bigger, the precision of the fit would be better, but it takes a lot of processing, so be careful!
    """
    return np.lib.polyval(np.lib.polyfit(to, be, 10), to)

def analysis(phase, twelve, day, may): #phase = time  , twelve = data , nine = string 
    """
    Hello!
    This funtion makes all the graphics about the stadistic loke the histogram, the simple plot and the gauss campane.
    """
    a, b = sum(twelve)*1., len(twelve)*1.
    mean = a/b
    o = []
    for x in twelve:
        o.append((x-mean)**2)
    o = (sum(o)/(len(twelve)-1))**.5
    drey = []
    for x in twelve:
        if x < 3*o:
            drey.append(x)
    drey = np.array(drey)
    completement = {"good" : "SkyPipe Units (SPU)", "month" : "Power (W)"}
    moon = fit(phase, twelve)
    spacement = preprocessing.scale(drey)
    
    plt.subplot(gs[0,may])
    plt.plot(phase, twelve, "r-", label = "Line across the data")
    #If you want to show the points individually discomment the next comment
    #plt.plot(snowblind, varien, "g+", label = "Individual Data")
    plt.plot(phase, moon, "k-", label = "Fit")
    plt.legend()
    plt.title(r"Relation Between Time ($\Delta t$) And "+completement[day] , fontsize=12) #r"SkyPipe Units ($SPU$)"
    plt.suptitle(mirai[0], fontsize=10)
    plt.ylabel(completement[day], fontsize=10)
    
    plt.subplot(gs[1,may])
    plt.title("Histogram", fontsize=10)
    plt.hist(twelve, bins=200, color="violet", histtype="bar", orientation="vertical")
    #Models of histogram: bar', 'barstacked','step','stepfilled','left','mid','right'.
    #Orientation of histogram: 'horizontal', 'vertical'
    plt.ylabel("Times Repeated", fontsize=10)
    
    plt.subplot(gs[2,may])
    plt.title("Gauss's Campane", fontsize=10)
    plt.hist(spacement, bins=200, color="violet", histtype="bar", orientation="vertical")
    #Models of histogram: bar', 'barstacked','step','stepfilled','left','mid','right'.
    #Orientation of histogram: 'horizontal', 'vertical'
    plt.ylabel("Times Repeated", fontsize=10)
    plt.xlabel(completement[day], fontsize=10)
        
    endgame = Tk()
    L1 = Label(endgame, text="Your Mean is %s %s and your Mean Deviation is %s %s"%(str(mean), str(completement[day]), str(o), str(completement[day])))
    L1.pack()
    L2 = Label(endgame, text="Your observation started in %s and finished in %s %s (UT) "%(timein, timeout, mirai[0]))
    L2.pack()
    B1 = Button(endgame, text="Next >", command=endgame.destroy)
    B1.pack()
    endgame.mainloop()

    
rar = os.getcwd().split("/")
bash = "/"+rar[1]
os.chdir(bash)
root = Tk()
t = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a .txt file')
root.destroy()
try:
    mirai, sekai, varien = np.loadtxt(t, dtype="string", unpack=True)
except:
  raise TypeError("Sorry, but I couldn't unpack the files. You hadn't selected a .txt file from SkyPipe. :(")
timein, timeout = sekai[0], sekai[-1]
sekai , varien = np.array([x.replace(",", ".") for x in sekai]) , np.array([x.replace(",", ".") for x in varien], dtype="float")
sekai = np.array([x.replace(":", ",") for x in sekai])
droptek = []
for x in sekai:
    droptek.append(x.split(","))
droptek = list(itertools.chain(*droptek))
droptek = [float(x) for x in droptek]
snowblind = []
for x in xrange(0, len(droptek), 3):
    snowblind.append(droptek[x]*3600+droptek[x+1]*60+droptek[x+2])
snowblind = np.array(snowblind, dtype="float")
snowblind = np.array([x-snowblind[0] for x in snowblind])

appears = varien*boltzmann*6e3
f = plt.figure(figsize=(20,20))
gs = plt.GridSpec(3, 2)
analysis(snowblind, varien, "good", 0)
analysis(snowblind, appears, "month", 1)

burn = Tk()
burn.wm_title("Stadistic")
canvas = FigureCanvasTkAgg(f, master = burn)
toolbar = NavigationToolbar2TkAgg(canvas, burn)
toolbar.pack()
canvas.get_tk_widget().pack(side=LEFT)
burn.mainloop()

