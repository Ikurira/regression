import mysql.connector
import numpy as np
from scipy import stats
import datetime

def performRegression(asset):

    conn = mysql.connector.connect(
    option_files="my.cnf")

    cur = conn.cursor()

    startSlice = 0  #Variable for start point in slicing time series
    endSlice = 59   #Variable for end point in slicing time series
    yVariable = 0   #Variable for selecting 'Y' in regression analysis
    xVariable = 0   #Variable for selecting 'X' in regression analysis

    size = 400      #Variable for determinig size of time series
    signal=[]       #Variable to collect residuals
    while True:
        try:
            time = datetime.datetime.now()
            day = time.day
                                                                    
            if endSlice == size:                                        #Once entire time series has been analysed, check for Standard Deviation
                print ('Currently analysing Standard Deviations on', asset[yVariable], '/', asset[xVariable])
                
                sigma = np.std(signal)                                  #Standard Deviation of mean reverting residual
                standardDeviation = np.around((sigma), decimals=2)      #Standard Deviation to 2 decimal places
                                                            
                if sigma > 2:                                           #If the Standard Deviation is larger than 2, notify user and insert into database
                    print(' *** =====> Current Standard Deviation for ', (asset[yVariable]), '/', (asset[xVariable]), 'is', standardDeviation, '<===== *** ')
                    
                    sql = "insert into matches (Date, type, front, back)values(%s, %s, %s, %s)" #insert result into matches table
                    values = (day, sigma, asset[yVariable], asset[xVariable])
                    cur.execute(sql, values)
                    conn.commit()

                signal=[]    


                xVariable += 1
                startSlice = 0                                          #Reset variable for start point in slicing time series
                endSlice = 59                                           #Reset variable for end point in slicing time series
                if xVariable == len(asset):                             #Once all X Variables have been regressed, start a new Y Variable
                    yVariable += 1
                    xVariable = 0

            sql = "SELECT close FROM " + asset[yVariable]               #Execute query
            query = cur.execute(sql) 
            output = cur.fetchall()
            outputArray = np.array(output)                              #Turn list into an array 
            flatY = outputArray.flatten()                               #Flatten from 2d shape to 1d for analysis
            Y = flatY[-size:]
            Y = Y[startSlice:endSlice]                                  #Create a 60 data point time series
            
            sql = "SELECT close FROM " + asset[xVariable]
            query = cur.execute(sql)
            output = cur.fetchall()
            outputArray = np.array(output)                              #Turn list into an array 
            flatX = outputArray.flatten()                               #Flatten from 2d shape to 1d for analysis
            X = flatX[-size:]
            X = X[startSlice:endSlice]                                  #Create a 60 data point time series

                                                                        #perform Linear Regression
            model = slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
            yhat = X * model.slope + intercept                          #calculate predicted Y
            residual = yhat - yVariable                                 #create residual variable
            signal.append(residual[-1])                                 #mean reverting residual

            startSlice += 1
            endSlice += 1
        except Exception as e:
            print (e)
            break
