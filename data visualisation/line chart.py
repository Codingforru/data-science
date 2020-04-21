#plotting the basics using matplotlib
#import pyplot of matplotlib
import matplotlib.pyplot as plt

x_days=[1,2,3,4,5,6,]
y_price1=[9,8.6,5.6,9.9,5.6,6.3]
y_price2=[12,10,9.6,4.9,6.8,7.6]



#plot the line plot
plt.title('stock movement')
plt.xlabel('weekdays')
plt.ylabel('prices in USD')

plt.plot(x_days,y_price1,label='stock 1')
plt.plot(x_days,y_price2,label='stock 2')

#create the legends
plt.legend(loc=2,fontsize=12)
plot.show()



