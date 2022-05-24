import numpy as np
import matplotlib.pyplot as plt
from pygments import highlight
from scipy import optimize

def convertTime(x): #def function to help convert time to decimal
    for a in x:
        colonindex = x.find(':')
        hours = x[0:colonindex]
        seconds = x[colonindex+1 :]
        hoursmins = (float(hours)+(float(seconds)/60.0))
        adddayfloat = ((float(hoursmins))/24.0)
    return float(adddayfloat)


#Defining a function to describe the Intra- and Inter- day variations of the tide
def findIntraInterVariation():

    #First we want to bring in the data set from the file that was given to us. It has the tidal
    #measurements in Santa Cruz in January and February of 2022.
    testArray = np.loadtxt('tideinfo.csv', dtype = "str")
    sig = 0.25
    y_err = np.full(82, sig)
   
    #Create some arrays to split up the information from the data set.   
    #We break it into 3 different arrays: days, time, and tide reading
    dayArray = np.array([])
    
    timeArray = np.array([])

    tideArray = np.array([])

    #Create a for loop to iterate through the data and put the data into their
    #corresponding arrays that we created.
    for i in testArray:
        dayArray = np.append(dayArray, int(i[0]), axis=None)
        timeArray = np.append(timeArray, i[1], axis=None)
        tideArray = np.append(tideArray, float(i[2]), axis=None)

    for day in dayArray:
        dayfloat = float(day)
        perdayConvert = np.array([convertTime(xi) for xi in timeArray])

    c = np.array(list(zip(perdayConvert,dayArray))) 
    # c is a combined array to add day count to (hours + min) which has already been converted

    finaltime = np.array([(x[0] + x[1]) for x in c])
    # finaltime is the final array that has all the times (84 times) in decimal form the format of 1 day/24 hours = 1.
    # print("finaltime : ", finaltime)

    #Create a couple more arrays: highTide[] readings and lowTide[] readings
    highTide = np.array([])
    lowTide = np.array([])

    #To get the data into their proper arrays, we splice through the tideArray readings. So
    #for the low tide readings we have to start at index 1 and take every other value. 
    
    #For the high tide readings, we start at index 0 and then take every other value because
    #we know that that data corresponds with the high tide.
    
    #We also wanted to get rid of the doubling of data in the day array, so we removed the
    #duplicates from the dayArray and created the singleDayArray[]
    lowTide = tideArray[1::2]

    highTide = tideArray[0::2]

    singleDayArray = dayArray[0::2]

    # print(np.var(lowTide), np.var(highTide))
    
    plt.figure(figsize=[21,15])

    # plt.plot(highTide, '-o', label="High Tide")
    # plt.plot(tideArray, '-o', label="All Tide")
    
    plt.plot(finaltime, tideArray, label = "All Tide") #this is the plotting of the (decimal converted day/hour/min times) vs (all tide data)

    #  plot the amplitude data graph
    # plt.plot(dayArray, np.fabs(tideArray - np.mean(tideArray)))

    plt.title("Tidal Readings from Santa Cruz (January - February)")
    
    plt.xlabel("Time in Decimal form (1 day/24 hours = 1.0")
    
    plt.ylabel("Tide Height")
    
    plt.xticks(range(0,42))

    
    #Styling the size of the text in the figure
    plt.rc('axes', labelsize = 24)
    
    plt.rc('xtick', labelsize = 10)
    
    plt.rc('ytick', labelsize = 10)
    
    plt.rc('legend', fontsize = 14)
    
    plt.rc('figure', titlesize = 24)
    
    legend = plt.legend(fancybox = True, framealpha = 1, shadow = True, borderpad = 1)
    
    #This is a for loop so that we can annotate each of our data points with the correct
    #tidal reading.

    # for i in range(len(singleDayArray)):
        
    #     plt.annotate(lowTide[i], xy=(singleDayArray[i], lowTide[i]), textcoords = "offset points", xytext = (-20,-10), ha = 'center')
        
    #     plt.annotate(highTide[i], xy=(singleDayArray[i], highTide[i]), textcoords = "offset points", xytext = (-20,-10), ha = 'center')


    for i in range(len(finaltime)):
        
        plt.annotate(tideArray[i], xy=(finaltime[i], tideArray[i]), textcoords = "offset points", xytext = (-20,-10), ha = 'center')      

    #define function we can use to model data
    def f_line(x, a, b, c, d):
        return a*np.sin(b*x +c) + d


    #perform a fit


    params, params_cov = optimize.curve_fit(f_line,finaltime,tideArray,sigma=y_err,p0=[2.7,15.,5.,4.])

    
    #p0 is initial guess of the parameters
    #you can guess initial parameters based on the graph - looking to see guess about frequency, amplitude, etc
    #will compute how close is the model to the data
    #minimize the squared deviation in the points in the model

    a_fit = params[0]
    b_fit = params[1]
    c_fit = params[2]
    d_fit = params[3]

    print(a_fit,b_fit,c_fit,d_fit)
    y_fit = a_fit * np.sin(b_fit * singleDayArray + c_fit) + d_fit

    # plt.errorbar(singleDayArray,highTide,yerr=y_err,fmt='o', label ='data')
    # plt.plot(singleDayArray,y_fit,label='fit')
    # plt.xlabel('x')
    # plt.ylabel('y')


    plt.show()

    
#Call the function to perform the operation and create the graph
findIntraInterVariation()

