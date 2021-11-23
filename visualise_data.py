import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import mysql.connector

def visualiseOutput(): 

    cur = conn.cursor()

    startSlice = 0  #Variable for start point in slicing time series
    endSlice = 59   #Variable for end point in slicing time series
    
    size = 400
    signal=[]
    while True:
        try:
           
            sql = "SELECT close FROM " + front
            query = cur.execute(sql) 
            output = cur.fetchall()
            outputArray = np.array(output)                              #Turn list into an array 
            flatY = outputArray.flatten()                               #Flatten from 2d shape to 1d for analysis
            Y = flatY[-size:]
            Y = Y[startSlice:endSlice]                                  #Create a 60 data point time series

            sql = "SELECT close FROM " + back
            query = cur.execute(sql)
            output = cur.fetchall()
            outputArray = np.array(output)                              #Turn list into an array 
            flatX = outputArray.flatten()                               #Flatten from 2d shape to 1d for analysis
            X = flatX[-size:]
            X = X[startSlice:endSlice]                                  #Create a 60 data point time series
            
            model = slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
            yhat = X * model.slope + intercept
            residual = yhat - Y
            signal.append(residual[-1])

            startSlice += 1
            endSlice += 1
        except Exception as e:
            print (e)
            break
        
    plt.plot(signal)
    plt.grid(b=True, which='major', color='b', linestyle='-')
    plt.grid(b=True, which='minor', color='r', linestyle='--')
    plt.minorticks_on()

    plt.show()

if __name__ == "__main__":
    conn = mysql.connector.connect(
    option_files="my.cnf")

    print('\n ** To visualise the residual data, enter the Y variable and X variable when prompted.** \n \n ** From MySql these are referenced under columns "Front" and "Back" respectively.**')
    print('\n Please enter variables below: \n')

    while True:
        print ('\n')
        front = input('Y = : ')
        back = input('X = : ')
        visualiseOutput()

    