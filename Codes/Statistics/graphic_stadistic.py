import sys
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *
import tkFileDialog
import matplotlib.pyplot as plt
import numpy as np
import os
import itertools #To join all elements of a list, look https://docs.python.org/2/library/itertools.html
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from sklearn import preprocessing
from scipy.constants import Boltzmann as boltzmann #Importing Boltzmann's constant as boltzmann

def choose():
  rar = os.getcwd().split("/") # Going to the
  bash = "/"+rar[1] #first directory of your
  os.chdir(bash) #computer
  root = Tk()
  m = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a .txt file')
  root.destroy()
  return m  

def prepair(t):   
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
  return snowblind, varien, mirai, timein, timeout
  
def fit(to, be):
    """
    Hello!
    This function makes the best fit for the data by the way of polinomical funtions
    While the integer is bigger, the precision of the fit would be better, but it takes a lot of processing, so be careful!
    """
    return np.lib.polyval(np.lib.polyfit(to, be, 10), to)

def analysis(phase, twelve, day, may, gs): #phase = time  , twelve = data , day = string, may = subplot, gs = GridSpec
    """
    Hello!
    This funtion makes all the graphics about the stadistic loke the histogram, the simple plot and the gauss campane.
    """
    myst = 0
    a, b = sum(twelve)*1., len(twelve)*1.
    mean = a/b
    o = []
    for x in twelve:
	o.append((x-mean)**2)
    o = (sum(o)/(len(twelve)-1))**.5
    drey = []
    completement = {"good" : "SkyPipe Units (SPU)", "month" : "Power (W)"}
    for x in twelve: #This "for" is for the Gauss's Campane,  
	if x < 3*o: #If the data is smaller than 3 mean deviation
	    drey.append(x) #Join it to make the Gauss's Campane (Feel free to change the "3")
    drey = np.array(drey)
    moon = fit(phase, twelve)
    spacement = preprocessing.scale(drey) #Standardization, look this http://scikit-learn.org/stable/modules/preprocessing.html
    plt.subplot(gs[0,may])
    plt.plot(phase, twelve, "r-", label = "Line across the data")
    #If you want to show the points individually discomment the next comment
    #plt.plot(snowblind, varien, "g+", label = "Individual Data")
    plt.plot(phase, moon, "k-", label = "Fit")
    plt.legend(fontsize=10)
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
	
    return mean, o, completement[day]

  
def graphic(): 
  appears = varien*boltzmann*6e3
  f = plt.figure(figsize=(20,20))
  gs = plt.GridSpec(3, 2)
  mean1, o1, comp1 = analysis(snowblind, varien, "good", 0, gs)
  mean2, o2, comp2 = analysis(snowblind, appears, "month", 1, gs)
  burn = Tk()
  def another():
    burn.destroy()
  def andother():
    burn.destroy()
    sys.exit()
  burn.protocol('WM_DELETE_WINDOW', andother)
  burn.wm_title("Stadistic")
  canvas = FigureCanvasTkAgg(f, master = burn)
  toolbar = NavigationToolbar2TkAgg(canvas, burn)
  L1 = Label(burn, text="Your Mean is %s %s and your Mean Deviation is %s %s"%(str(mean1), str(comp1), str(o1), str(comp1)))
  L2 = Label(burn, text="Your Mean is %s %s and your Mean Deviation is %s %s"%(str(mean2), str(comp2), str(o2), str(comp2)))
  L3 = Label(burn, text="Your observation started in %s and finished in %s %s (UT) "%(timein, timeout, mirai[0]))
  B1 = Button(burn, text="Quit", bg="red", fg="white" ,command=andother)
  B2 = Button(burn, text="Another File", bg="blue", fg="white", command=another)
  L1.grid(columnspan=2)
  L2.grid(columnspan=2)
  L3.grid(columnspan=2)
  burn.grid_columnconfigure(1, weight=1)
  B1.grid(row=3, sticky=E)
  B2.grid(row=3, column=1, sticky=W)
  burn.grid_columnconfigure(0, weight=1)
  burn.grid_rowconfigure(4, weight=1)
  canvas.get_tk_widget().grid(row=4, columnspan=2, sticky=W)
  toolbar.grid(columnspan=2)
  burn.mainloop()
while True:    
  snowblind, varien, mirai, timein, timeout = prepair(choose()) #Here I use the return of choose() to run prepair()
  graphic()	  