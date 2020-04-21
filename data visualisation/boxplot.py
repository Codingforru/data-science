import os
print(os.getcwd())


import matplotlib.pyplot as plt

f=open('salesdata.csv','r')
salesfile=f.readlines()
sales_list=[]
for records in salesfile:
    sales_list.append(int(records))
    


#plot the line plot
plt.title('BOX PLOT OF SALES')

plt.boxplot(sales_list)

plot.show()