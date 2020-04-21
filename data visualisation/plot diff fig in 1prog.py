
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
plt.figure(1)
plt.title('sale vs cost')
plt.xlabel('sale')
plt.ylabel('cost')
plt.scatter(s_list,c_list)
plt.savefig('images/scatter.png')


#plot the boxplot
plt.figure(2)
plt.title('BOX PLOT OF SALES')
plt.ylabel("USD")
plt.boxplot(sale_list)
plt.savefig('images/21box.png')
