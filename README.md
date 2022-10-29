# Battery-Discharge-Plots
This repository provides python code and battery discharge dataset to easily plot and estimate the discharge patterns. 

 #CITATION
Ali, O., Ishak, M. K., Ooi, C. A., & Bhatti, M. K. L. (2022). Battery characterization for wireless sensor network applications to investigate the effect of load on surface temperatures. Royal Society open science, 9(2), 210870.

Abstract
This dataset reports the discharge profiles of 4 battery chemistries under IEEE 802.15.4 radio load profiles. The batteries were independently subjected to a five-step method to record the discharge characteristics. These discharge currents, their effect on battery capacity, and surface temperature may affect the overall battery lifetime, which was the major aim to discover. The following batteries were used in these experiements



Methods
The batteries were placed in a climate chamber to keep the temperatures constant. A data logging and buffering circuit was designed that recorded the battery voltages during the discharge cycles. Each battery was independently subjected to IEEE 802.15.4 based radio current profiles and therefore recorded accordingly. A total of 12 observations were made to record the discharge characterisitics of the batteries. In addition, 4 set of observations were made to record the effect of current on battery surface temperature. 

The battery relaxation time is important in identifying the optimum charge capacity of the battery. Therefore, the batteries were fully charged before being discharged at three separate SOC levels (corresponding to 90%, 50%, and 10%, respectively) after a 24-hour rest period. During this relaxation time, voltages were measured with a one-minute resolution and were compared to OCV measurements after 24 hours. The battery was considered quasi-stabilized at this stage. The OCV error between stabilized battery states can be computed from Equation below.

 

Usage Notes
The files are sorted, filtered and can be used as it is for future research work. It is important to consider that the discharge profiles may change with the increase or decrease in battery capacity, under ambient effects (such as temperature and humidity) and also with the relaxation period. Therefore, it is recommended to use this dataset to report only the battery chemistries as described above. In addition, it is very important to provide a minimum rest period of 4 hours to each battery, after a full charge cycle. 

The following folder and file structure is made available:

1. BATTERY DISCHARGE FILTERED DATA

Battery Discharge Characteristics (Contains individual battery discharge parameters for the above mentione battery capacities)
Battery Surface Temperatures (Contains ambient temperature, as well as readings from two PT100 sensors mounted on top of each battery)
Normalized Discharged characistics for plotting (Presents a template to selected weighted average-based normalized values for plots)
Relaxation Time Calculation (The OCV and relaxation time values are computed and the percentage error is calculated)

2. EXPERIMENTAL DATA

The experimental data contains actual battery discharge patterns recorded after laboratory experiments. Each excel file is presented in the format of 
"Battery Type_discharge current_status". For Instance, "Li-Ion-30mA_RAW" will report:
a. Battery type -> Lithium Ion
b. Discharge current -> 30mA
c. dataset filteration -> RAW (none) that means pre-processing and transformation is required.

Every excel file then further contains five sheets (5C, 15C, 25C, 35C, 45C) that contains battery discharge parameters recorded at different temperatures. 


3. CODE FILES

This data set provides a single code files that will help to quickly plot and visualize the dataset. The code files are written in Python and can be described as


voltage_curves.py ->  imports, splits and visualizes various battery discharge characteristics. This code is helpful in quickly visualizing the provided dataset. 
