#THIS CODE WILL PLOT THE UNFILTERED VOLTAGE AND SOC VALUES STRAIGHT OUT OF EXPERIMENTAL DATA
#AS A BATTERY DISCHARGE MAY CONTAIN 1000S OF VALUES, IT IS A GOOD PRACTICE TO QUICKLY PLOT
#THE RESULTS TO FIND OUT ANY ANOMALIES, AND ALSO TO VALIDATE IF THE RECORDED VALUES COVERED THE
#ENTIRE DISCHARGE OF THE BATTERY. THIS SAVES A LOT OF TIME FOR THE NEXT STEPS THAT INVOLVES
#1. DATA PROCESSING 2. TRANSFORMATION 3. FILTERING 4. ML MODEL DEVELOPMENT

import matplotlib.pyplot as plt #matplotlib for plotting
import pandas as pd #pandas for data handling
import xlrd
import numpy as np
import seaborn as sns
from scipy.interpolate import make_interp_spline,BSpline

#importing the data files. Currently, this code imports a single xlsx file, but multiple files can be
#imported into multiple dataframes.

xls = pd.ExcelFile("../experimental data/Li-Ion-30mA_RAW.xlsx")
ExcelSheet = xls.parse(0) #as every excel file contains data in multiple sheets (for different temperatures)
#the sheets can easily be switched by providing the appropriate number.

#Next, the data from each sheet can be stored in variable/arrays

batt_capacity = ExcelSheet['capacity'] #remaining battery capacity after each discharge iteration
batt_soc = ExcelSheet['soc'] #remaining battery SOC after each discharge iteration
batt_voltage = ExcelSheet['scaled'] #battery voltage values per iteration
batt_time = ExcelSheet['time'] #time intervals recorded. In this experiment, recordings were taken at 15 sec.
print(batt_voltage) #printing few values to see if the data import worked or not.

#THE FOLLOWING CODE WILL PLOT THE IMPORTED FEATURE VALUES

# 1. UNFILTERED VOLTAGE CURVES
plt.close('all') #close any previously opened figures.
fig = plt.figure()
plt.xlim([0,35000])
plt.ylim([3.5,4.5])
plt.title ('Voltage discharge curves of XYZ mAh battery ')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (volts)')
plt.style.use('seaborn-muted')
plt.grid()
ax = fig.gca()
plt.plot(batt_time,batt_voltage, label='30mA load at 5C')

###################################################################################

#comment out the following if you only have one set of readings at one temperature
#similarly we can simultaneously read values at other temperatures to see a trend
ExcelSheet = xls.parse(1)
batt_capacity15C = ExcelSheet['capacity'] #remaining battery capacity after each discharge iteration
batt_soc15C = ExcelSheet['soc'] #remaining battery SOC after each discharge iteration
batt_voltage15C = ExcelSheet['scaled'] #battery voltage values per iteration
batt_time = ExcelSheet['time'] #time intervals recorded. In this experiment, recordings were taken at 15 sec.
plt.plot(batt_time,batt_voltage15C, label='30mA load at 15C')

#similarly we can simultaneously read values at other temperatures to see a trend
ExcelSheet = xls.parse(2)
batt_capacity25C = ExcelSheet['capacity'] #remaining battery capacity after each discharge iteration
batt_soc25C = ExcelSheet['soc'] #remaining battery SOC after each discharge iteration
batt_voltage25C = ExcelSheet['scaled'] #battery voltage values per iteration
batt_time = ExcelSheet['time'] #time intervals recorded. In this experiment, recordings were taken at 15 sec.
plt.plot(batt_time,batt_voltage25C, label='30mA load at 25C')

#similarly we can simultaneously read values at other temperatures to see a trend
ExcelSheet = xls.parse(3)
batt_capacity35C = ExcelSheet['capacity'] #remaining battery capacity after each discharge iteration
batt_soc35C = ExcelSheet['soc'] #remaining battery SOC after each discharge iteration
batt_voltage35C = ExcelSheet['scaled'] #battery voltage values per iteration
batt_time = ExcelSheet['time'] #time intervals recorded. In this experiment, recordings were taken at 15 sec.
plt.plot(batt_time,batt_voltage35C, label='30mA load at 35C')

ExcelSheet = xls.parse(4)
batt_capacity45C = ExcelSheet['capacity'] #remaining battery capacity after each discharge iteration
batt_soc45C = ExcelSheet['soc'] #remaining battery SOC after each discharge iteration
batt_voltage45C = ExcelSheet['scaled'] #battery voltage values per iteration
batt_time = ExcelSheet['time'] #time intervals recorded. In this experiment, recordings were taken at 15 sec.
plt.plot(batt_time,batt_voltage45C, label='30mA load at 45C')
#############################################################################################################

plt.legend()
plt.show() #calling show at the end so that all values appear on single figure. This is equivalent to hold function in
#MATLAB and other plotting applications.

#USE THIS code to convert the RAW voltage values into more presentable smooth splines.
#This requires BSPLINE library, which further requires conversion from Pandas to Numpy

x_np = batt_time[~np.isnan(batt_time)] #This converts pd dataframe to numpy array, by removing all NaN values
v_np = batt_voltage[~np.isnan(batt_voltage)] #convert voltage from pandas to numpy.
xnew = np.linspace(x_np.min(),x_np.max(),50) #creating new linspace for interpolation. The larger the value (50),
#the more resolution or samples will be present in the line.
spl = make_interp_spline(x_np,v_np,k=3) #creating interpolated spline from x(min) to x(max).
vnew = spl(xnew)

####################################################################################################
#Similarly, create individual splines for other voltage values at diff. temperature.
x_np15 = batt_time[~np.isnan(batt_time)] #This converts pd dataframe to numpy array, by removing all NaN values
v_np15 = batt_voltage15C[~np.isnan(batt_voltage15C)] #convert voltage from pandas to numpy.
xnew15 = np.linspace(x_np15.min(),x_np15.max(),50) #creating new linspace for interpolation. The larger the value (50),
#the more resolution or samples will be present in the line.
spl15 = make_interp_spline(x_np15,v_np15,k=3) #creating interpolated spline from x(min) to x(max).
vnew15 = spl15(xnew15)


x_np25 = batt_time[~np.isnan(batt_time)] #This converts pd dataframe to numpy array, by removing all NaN values
v_np25 = batt_voltage25C[~np.isnan(batt_voltage25C)] #convert voltage from pandas to numpy.
xnew25 = np.linspace(x_np25.min(),x_np25.max(),50) #creating new linspace for interpolation. The larger the value (50),
#the more resolution or samples will be present in the line.
spl25 = make_interp_spline(x_np25,v_np25,k=3) #creating interpolated spline from x(min) to x(max).
vnew25 = spl25(xnew25)

x_np35 = batt_time[~np.isnan(batt_time)] #This converts pd dataframe to numpy array, by removing all NaN values
v_np35 = batt_voltage35C[~np.isnan(batt_voltage35C)] #convert voltage from pandas to numpy.
xnew35 = np.linspace(x_np35.min(),x_np35.max(),50) #creating new linspace for interpolation. The larger the value (50),
#the more resolution or samples will be present in the line.
spl35 = make_interp_spline(x_np35,v_np35,k=3) #creating interpolated spline from x(min) to x(max).
vnew35 = spl35(xnew35)


x_np45 = batt_time[~np.isnan(batt_time)] #This converts pd dataframe to numpy array, by removing all NaN values
v_np45 = batt_voltage45C[~np.isnan(batt_voltage45C)] #convert voltage from pandas to numpy.
xnew45 = np.linspace(x_np45.min(),x_np45.max(),50) #creating new linspace for interpolation. The larger the value (50),
#the more resolution or samples will be present in the line.
spl45 = make_interp_spline(x_np45,v_np45,k=3) #creating interpolated spline from x(min) to x(max).
vnew45 = spl45(xnew45)

##############################################################################################
#now plotting the values
plt.style.use('seaborn-muted')
plt.grid()
ax = fig.gca()

plt.plot(xnew,vnew, label = 'Voltage discharge curves at 5C')
plt.plot(xnew15,vnew15, label = 'Voltage discharge curves at 15C')
plt.plot(xnew25,vnew25, label = 'Voltage discharge curves at 25C')
plt.plot(xnew35,vnew35, label = 'Voltage discharge curves at 35C')
plt.plot(xnew45,vnew45, label = 'Voltage discharge curves at 45C')
plt.title('Voltage Discharge curves for XYZ Battery')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (volts)')
plt.legend()
plt.show()

#Simple SoD curves over time. They are normally going to be linear graphs
#State of Discharge, normally maps how SOC values behaved over time.
#Although the values will be linear, but simultaneously observing multiple SOC values (for instance for different temperature values)
#can easily help to estimate how SOC varied.
fig2 = plt.figure()

plt.ylim([0, 100])
plt.xlim([0, 9000])
plt.style.use('seaborn-dark-palette')
plt.plot(batt_time,batt_soc,label='State of Discharge at 5C')
plt.plot(batt_time,batt_soc15C,label='State of Discharge at 15C')
plt.plot(batt_time,batt_soc25C,label='State of Discharge at 25C')
plt.plot(batt_time,batt_soc35C,label='State of Discharge at 35C')
plt.plot(batt_time,batt_soc45C,label='State of Discharge at 45C')

plt.title('SoD for XYZmAh Li-Po battery over time')
plt.xlabel('Time (seconds)')
plt.ylabel('State of Discharge over time (%)')
plt.grid()
plt.legend()
plt.show()
