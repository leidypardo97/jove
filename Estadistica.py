#Hacer un notebook de python que reciba datos, los archivos de texto planos, calcule promedio, desviación estándar,
#haga un histograma de frecuencias y ajuste la mejor curva de datos.

#http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#http://stackoverflow.com/questions/10393176/is-there-a-way-to-read-a-txt-file-and-store-each-line-to-memory
import matplotlib.pyplot as plt
import numpy as np #Importing tools
import matplotlib.mlab as mlab
font = {'family' : 'serif',
        'color'  : 'darkgreen', #Selecting class of text to be plotted
        'weight' : 'normal',
        'size'   : 20,
        }
#----------------------------------# This enclosed part makes a .txt file to probe the code 
forth= open("probes.txt", "w")     #It's just simulating the receiving of data from the radio telescope
forth.write("0 12 ")
forth.write("1 24 ")
forth.write("2 36 ")
forth.close()
#----------------------------------#

will, save=[],[] #Making two empty lists
with open('probes.txt', 'r') as fitsio:                             #Specifying that part as fitsio to make things easier
    seb= fitsio.readlines() #Counting lines                         #Here you put the name of your .txt file. I can put a raw_input, 
    for line in seb: #This for goes in range(fitsio.readlines())    #but like is only a probe I didn't.   
        drunk= line.split() #This part adds a "comma" for each space          
     
drunk=[int(x) for x in drunk] #Making integers all components of drunk

for gauss in range(0, len(drunk), 2):
        will.append(drunk[gauss])      #Separating drunk into two lists, one of time and one of Amperes
for milk in range(1, len(drunk), 2):
    save.append(drunk[milk])    

prom=(sum(save))/(len(save)) #Calculating the mean

hollow=[] #Making an empty list
for dawn in range(len(save)): #I think that this doesn't need explanation
    hollow.append((((save[dawn])-prom)**2)) #We are appending the summatory to find the mean deviation
    
hollow=sum(hollow) #And we sum all the components
hollow= hollow/(len(save)-1) #And next we divide it by n-1 where n is the len of the list "save"
hollow=hollow**0.5 #Finally, we do a square root

fig = plt.figure() #Plotting a base
ax = fig.add_subplot(111) #Setting the axes
ax.set_title("Data Itvara", fontdict=font) #Title
ax.text(0.01, 0.9, "When you close a window the next graphic", fontdict=font , #Saying a instruction in a yellow box
        bbox={"facecolor":"yellow", "alpha":1, "pad":10})
ax.text(0.01, 0.81, "will appear", fontdict=font ,  #The same instruction
        bbox={'facecolor':'yellow', "alpha":1, "pad":10})
ax.text(0.1, 0.7, "$Average=$ "+"$"+str(prom)+"$"+" $A$", fontdict=font) #Plotting the average
ax.text(0.1, 0.6, "$Mean$ "+"$Deviation=$ "+"$"+str(hollow)+"$"+" $A$", fontdict=font) #Plotting the mean deviation
plt.show() #Showing

pegboard=[x for x in save] #pegboard=save
podcast=[] #New list
boombox=1 #Counter
for hero in range(len(pegboard)): 
    switch=pegboard[0]
    pegboard.pop(0)
    for your in pegboard:
        if switch==your:
            boombox=boombox+1
            
        else:
            break
    podcast.append(switch)
    podcast.append(boombox)
            
switch=[]
boombox=[]
for swung in range(0, len(podcast), 2):
    switch.append(podcast[swung])
    
for swung in range(1, len(podcast), 2):
    boombox.append(podcast[swung])
    
fig = plt.figure() #Plotting a base
ax = fig.add_subplot(111) #Setting the axes
ax.set_title("Frequency Histogram", fontdict=font) #Putting a title
me= prom + hollow  * np.random.randn(10000) #I don't understand this part as well as I wanted #I needed some help in this part
n, bins, patches= plt.hist(me, 50, normed=1, facecolor="yellow", alpha=0.5) #Plotting 50 bars, "me", in yellow and dark (alpha=1)
meqw = mlab.normpdf(bins, prom, hollow) #Adjusting the best curve data
plt.plot(bins, meqw, 'g--') #When we put normed=1 we allow to add other plots
plt.subplots_adjust(left=0.15) #Tweak spacing to prevent clipping of ylabel
plt.show() #Showing the plot #I taked a lot of things from http://matplotlib.org/examples/statistics/histogram_demo_features.html


plt.plot(will, save) #Just plotting a function with time and Amperes
plt.title("Itvara", fontdict=font) #Title
plt.xlabel("Time (s)", fontdict=font) #Naming labels
plt.ylabel("Intensity (A)", fontdict=font)
plt.show() #Showing
