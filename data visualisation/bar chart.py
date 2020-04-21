# create the bar chart for the temp variation

# import matplotlib

import os
print(os.getcwd())
import matplotlib.pyplot as plt

# bar chart for diff cities tmp
x_cities=['new delhi','london','new york','dubai','germany']
y_temp=[75,63,58,69,98]
          
          
          
          
#plot the line plot
plt.title('TEMP VARIATION')
plt.xlabel('CITIES')
plt.ylabel('TEMPERATURE')

plt.bar(x_cities,y_temp)

plot.show()
