
import matplotlib.pyplot as plt
# load the file
f=open('salesdata2.csv','r')
salesfile=f.readlines()


s_list=[] 
c_list=[]

for records in salesfile:
   sale,cost=records.split(sep=',')
   s_list.append(int(sale))
   c_list.append(int(cost))
   


   
   
#plot the scater plot


plt.title('sale vs cost')
plt.xlabel('sale')
plt.ylabel('cost')
plt.scatter(s_list,c_list)
