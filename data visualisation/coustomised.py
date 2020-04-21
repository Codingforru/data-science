

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
plt.subplot(2,3,1)
plt.title('sale vs cost')
plt.xlabel('sale')
plt.ylabel('cost')


# for coustmisations
plt.scatter(s_list,c_list,
             marker='*',
             s=40,c='g')


#plot the boxplot
plt.subplot(2,3,2)
plt.title('BOX PLOT OF SALES')
plt.ylabel("USD")
plt.boxplot(sale_list,
            patch_artist=True,
            boxprops=dict(facecolor='g',color='r',linewidth=2),
            whiskerprops=dict(color='r',linewidth=2),
            medianprops=dict(color='w',linewidth=1),
            capprops=dict(color='r',linewidth=2),
            flierprops=dict(markerfacecolor='r',marker='.',markersize=7))



            

#plot the line plot
x_days=[1,2,3,4,5,6,]
y_price1=[9,8.6,5.6,9.9,5.6,6.3]

plt.subplot(2,3,3)
plt.title('stock movement')
plt.xlabel('weekdays')
plt.ylabel('prices in USD')

plt.plot(x_days,y_price1,label='stock 1',color='g',marker='o',
         markersize='5',linewidth='2',linestyle='--')
plt.legend(loc=2,fontsize=8)

#plot for the histogram
plt.subplot(2,3,4)
plt.title("histogram of sales")
plt.ylabel("USD")
plt.hist(s_list,bins=5,rwidth=0.9,color='c')


#plot for bar chart
plt.subplot(2,3,5)
x_cities=['new delhi','london','new york','dubai','germany']
y_temp=[75,63,58,69,98]
          
         
#charts label
plt.title('TEMP VARIATION')
plt.xlabel('CITIES')
plt.ylabel('TEMPERATURE')
plt.xticks(rotation='45')

plt.bar(x_cities,y_temp,color=['r','g','c','y','m'])


#tightlayout so that the fig dont overlap
plt.tight_layout()
plt.savefig('images/01customplot.png')

plt.show()

   
   