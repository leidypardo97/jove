work in the range of len(forever) #I had problems here, so I changed x to guilty
    eraw=forever.index(guilty) #Here we will find the first ocurrence of x
    ax.scatter(guilty[grace], guilty[hop], guilty[need]) #Plotting a point in (x, y, z)
    ax.text(guilty[grace], guilty[hop], guilty[need], useful[eraw], style="oblique") #Plotting text in the same coordenates to identificate each one

put=forever #I don't need to explain this
send=[] #An empty list
for selfish in range(27): #I was a little paranoid, so I didn't use x again 
    ill=put[grace] #ill is the first integrator of put
    put.pop(grace) #And we erase this first element in put
    for shine in put: #Another for that makes the below operation for each letter of the alphabet making all the combinatorials
        sun=((((shine[grace]-ill[grace])**2.0)+((shine[hop]-ill[hop])**2.0)+((shine[need]-ill[need])**2.0))**0.5)*(shine[3]*ill[3]) #This operation is the calculus of a vector with x,y,z components by Pythagoras
        send.append(sun) #When we do the operation of above we get a number that we send to the list made before

    
send=[x*2 for x in send] #The work is mutual so...
send=[1/x for x in send] #And the distance is dividing so...
ax.text(0, 0, 1.5, "$E_p$="+str(sum(send))+"$kQ^2$"+"$r^-$"+"$^1$", style="oblique") #Plotting the U in the plot

ana=2
mp.show() #Showing the plot
#print "Here you have the distribution of the charges"
#mp.show() #Showing the plot3D
#hey=raw_input("Do you want to remove some of them [y/n]")
#if hey==y:
#    return fig
