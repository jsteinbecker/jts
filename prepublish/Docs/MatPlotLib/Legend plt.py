import matplotlib.pyplot as plt

"""
GENERATE LEGEND- FORMAT
##########################################
plt.legend.Legend(parent, handles, labels)
"""


plot = plt.figure(figsize=(10,6))

xaxis = ["Shift1","Shift2","Shift3"]
yaxis = [22,9,12]
yaxis2 = [12,8,2]

lab = ["EMP_1","EMP_2"]

bar = plt.bar(xaxis,yaxis,color='pink')
bar2 = plt.bar(xaxis,yaxis2,color='gold')

plt.legend(handles=(bar,bar2),labels=lab) # <-- LEGEND GENERATED HERE

plt.show()