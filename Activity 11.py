import numpy as np
import matplotlib.pyplot as mpl
import pandas as pnd
# 1.import information
tips = pnd.read_csv("./tips.csv")

# 2. Add new calculated column
tips["tips_percent"] = tips["total_bill"]/ tips["tip"]*100

#3. Subset of data
# dinnerInfo = [float,float, str, str,str,str, int]
dinnerInfo = tips.loc[tips["time"] == "Lunch"]
thurInfo = tips.loc[tips["day"]== "Thur"]
friInfo = tips.loc[tips["day"]== "Fri"]
satInfo = tips.loc[tips["day"]== "Sat"]
sunInfo = tips.loc[tips["day"]== "Sun"]


#4 Correlation coefficient
tips.corrcoef(tips[:,2], tips[:,7])

#5 Visualization

mpl.plot(thurInfo["tips_percent"],thurInfo["size"], label= "Thursday")
mpl.plot(friInfo["tips_percent"],friInfo["size"], label= "Friday")
mpl.plot(satInfo["tips_percent"],satInfo["size"], label= "Saturday")
mpl.plot(sunInfo["tips_percent"],sunInfo["size"], label= "Sunday")

mpl.xlabel("size")
mpl.ylabel("Tips %")

mpl.title("tips percentage compared to amount of people per day")


mpl.legend()
mpl.show()