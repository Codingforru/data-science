import os
print(os.getcwd())

import matplotlib.pyplot as plt

f=open('agedata.csv','r')
agefile=f.readlines()
age_list=[]
for records in agefile:
    age_list.append(int(records))

    
bins = [0,10,20,40,60,80,100]

#plot the line plot
plt.title('AGE HISTOGRAM')
plt.xlabel('GROUP')
plt.ylabel('AGE')

plt.hist(age_list,bins,histtype='bar',rwidth=0.7)


plot.show()

  



    