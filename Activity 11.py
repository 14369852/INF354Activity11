import matplotlib.pyplot as mpl
import numpy as np
import pandas as pnd

# 1.import information
tips = pnd.read_csv("./tips.csv")
print("1. Read success. ")
print(tips)
print ("===============================================================================")

# 2. Add new calculated column
print("2. Add calculated column. Success")
tips["tips_percent"] = tips["total_bill"]/ tips["tip"]
print(tips)
print ("===============================================================================")

#3. Subset of data
# dinnerInfo = [float,float, str, str,str,str, int]
print("3. Subset: Lunch info")
lunchInfo = tips.loc[tips["time"] == "Lunch"]
print(lunchInfo)
print ("===============================================================================")

#4 Correlation coefficient
print("4. Correlation coefficient b/w total bills and tips:")
cor = tips["total_bill"].corr(tips["tip"])
print (cor)
print ("===============================================================================") 

#5 Visualization
thurInfo = tips.loc[tips["day"]== "Thur"]
friInfo = tips.loc[tips["day"]== "Fri"]
satInfo = tips.loc[tips["day"]== "Sat"]
sunInfo = tips.loc[tips["day"]== "Sun"]

#1st plot
mpl.bar("Thursday", np.mean(thurInfo["tips_percent"]))
mpl.bar("Friday", np.mean(friInfo["tips_percent"]))
mpl.bar("Saturday", np.mean(satInfo["tips_percent"]))
mpl.bar("Sunday", np.mean(sunInfo["tips_percent"]))

mpl.xlabel("Days")
mpl.ylabel("Tips %")

mpl.title("5. Average tips percentage perday")

# mpl.legend()
mpl.show()

# 2nd plot
mpl.scatter(thurInfo["tips_percent"],thurInfo["size"], label= "Thursday")
mpl.scatter(friInfo["tips_percent"],friInfo["size"], label= "Friday")
mpl.scatter(satInfo["tips_percent"],satInfo["size"], label= "Saturday")
mpl.scatter(sunInfo["tips_percent"],sunInfo["size"], label= "Sunday")

mpl.xlabel("tips percentage")
mpl.ylabel("Size")

mpl.title("5. Tips per day per size")

mpl.legend()
mpl.show()