import numpy as np
import math

def returnsin(x):           #this function return the sin of the one paramater: x
    return(math.sin(x)) 

def returncos(x):           #this function return the cos of the one paramater: x
    return(math.cos(x)) 


def tabulate(min, max, entries, lines):     #min, max define the min and max of x as it tabulates
                                            #entries defines the increment value that x increases by as it moves towards the max
                                            #lines defines the number of lines to print of the created sequence

    valuearray = np.linspace(min, max, num=entries)
    print("x                     sin(x)                cos(x)")
        
    for x in range(0, lines):
        i = valuearray[x]
        formati = (format(i,".14f"))
        formatsini = (format(math.sin(i),".14f"))
        formatcosi = (format(math.cos(i),".14f"))
        print(formati, "    ", formatsini, "    ", formatcosi)

def firstten(min, max, entries):            #does the same print out as tabulate function, 
                                            #but the number of lines is automatically ten, the user cannot choose a different number
    for x in range(0,1):
        tabulate(min, max, entries, 10)


def main():
    
    tabulate(0, (2*math.pi), 1000, 1000)
    firstten(0, (2*math.pi), 1000)

if __name__=="__main__":
    main()