
import matplotlib.pyplot as plt
# load the file
f=open('salesdata2.csv','r')
salesfile=f.readlines()
sale_list=[]
s_list=[] 
c_list=[]

for records in salesfile:
   sale,cost=records.split(sep=',')
   s_list.append(int(sale))
   c_list.append(int(cost))
   
 # create the list of the list
sale_list.append(s_list)
sale_list.append(c_list)
   
   
#plot the scater plot
plt.subplot(2,2,1)
plt.title('sale vs cost')
plt.xlabel('sale')
plt.ylabel('cost')
plt.scatter(s_list,c_list)


#plot the boxplot
plt.subplot(2,2,2)
plt.title('BOX PLOT OF SALES')
plt.ylabel("USD")
plt.boxplot(sale_list)

#plot the line plot
x_days=[1,2,3,4,5,6,]
y_price1=[9,8.6,5.6,9.9,5.6,6.3]

plt.subplot(2,2,3)
plt.title('stock movement')
plt.xlabel('weekdays')
plt.ylabel('prices in USD')

plt.plot(x_days,y_price1,label='stock 1')
plt.legend(loc=2,fontsize=12)

#plot for the histogram
plt.subplot(2,2,4)
plt.title("histogram of sales")
plt.ylabel("USD")
plt.hist(s_list,bins=5,rwidth=0.9)

#tightlayout so that the fig dont overlap
plt.tight_layout()
plt.savefig('images/01subplot.png')

plt.show()

   
   