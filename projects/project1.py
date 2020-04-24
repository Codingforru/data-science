# importing some used modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

#read the data 
bikes =pd.read_csv('hour.csv')
bikes_prep=bikes.copy()

# prelim  and feature selection
c=list(bikes_prep.columns)
bikes_prep=bikes_prep.drop(["index","date","casual","registered"],axis=1) \
    #0=for row,1= columns
    
bikes_prep.isnull().sum()

#simple visualisation of data using hist
bikes_prep.hist(rwidth=0.9)
plt.tight_layout()

#data visualisation
#visualise the continuous features vs demand
plt.figure('figure 2')

plt.subplot(2,2,1)
plt.title('temp vs demand')
plt.scatter(bikes_prep['temp'],bikes_prep['demand'],s=2,c='g')
    
plt.subplot(2,2,2)
plt.title('atemp vs demand')
plt.scatter(bikes_prep['atemp'],bikes_prep['demand'],s=2,c='g')

plt.subplot(2,2,3)
plt.title('humidity vs demand')
plt.scatter(bikes_prep['humidity'],bikes_prep['demand'],s=2,c='r')

plt.subplot(2,2,4)
plt.title('windspeed vs demand')
plt.scatter(bikes_prep['windspeed'],bikes_prep['demand'],s=2,c='m')

plt.tight_layout()

# visualise the categorical variable
# visualise the categorical vs demand
plt.figure('fig 03')
colors=['g','r','b','m']
plt.subplot(3,3,1)
plt.title('season vs demand')
cat_list=bikes_prep['season'].unique()
cat_avg=bikes_prep.groupby('season').mean()['demand']
plt.bar(cat_list,cat_avg, color=colors)

plt.subplot(3,3,2)
plt.title('year vs demand')
cat_list=bikes_prep['year'].unique()
cat_avg=bikes_prep.groupby('year').mean()['demand']
plt.bar(cat_list,cat_avg, color=colors)

plt.subplot(3,3,3)
plt.title('month vs demand')
cat_list=bikes_prep['month'].unique()
cat_avg=bikes_prep.groupby('month').mean()['demand']
plt.bar(cat_list,cat_avg, color=colors)

plt.subplot(3,3,4)
plt.title('hour vs demand')
cat_list=bikes_prep['hour'].unique()
cat_avg=bikes_prep.groupby('hour').mean()['demand']
plt.bar(cat_list,cat_avg, color=colors)

plt.subplot(3,3,5)
plt.title('holiday vs demand')
cat_list=bikes_prep['holiday'].unique()
cat_avg=bikes_prep.groupby('holiday').mean()['demand']
plt.bar(cat_list,cat_avg, color=colors)

plt.subplot(3,3,6)
plt.title('weekday vs demand')
cat_list=bikes_prep['weekday'].unique()
cat_avg=bikes_prep.groupby('weekday').mean()['demand']
plt.bar(cat_list,cat_avg, color=colors)

plt.subplot(3,3,7)
plt.title('workingday vs demand')
cat_list=bikes_prep['workingday'].unique()
cat_avg=bikes_prep.groupby('workingday').mean()['demand']
plt.bar(cat_list,cat_avg, color=colors)

plt.subplot(3,3,8)
plt.title('weather vs demand')
cat_list=bikes_prep['weather'].unique()
cat_avg=bikes_prep.groupby('weather').mean()['demand']
plt.bar(cat_list,cat_avg, color=colors)

plt.tight_layout()



# checking for the outliers
bikes_prep['demand'].describe()
bikes_prep['demand'].quantile([.05,.10,.15,.9,.95,.99])

#check the multiple linear regression assumption
#linearity using correlation coefficient matrix using corr
correlation=bikes_prep[['temp','atemp','humidity','windspeed','demand']].corr()

#drop the irrleevent features
bikes_prep=bikes_prep.drop(['weekday','workingday','atemp','windspeed','year'],axis=1)

# check the autocorrelation in demand using accor plot
# value for autocor should be the float not the integer
plt.figure('fig04')
plt.title('demand auto correlation')
df1=pd.to_numeric(bikes_prep['demand'],downcast='float')
plt.acorr(df1,maxlags=12)

# create/ modify new features
#log normalise the feature demand
df2=bikes_prep['demand']
df3=np.log(df2)
plt.figure('fig05')
plt.subplot(1,2,1)
plt.title('demand plot')
df2.hist(rwidth=.9,bins=20)
plt.subplot(1,2,2)
plt.title('log demand plot')
df3.hist(rwidth=.9,bins=20)

bikes_prep['demand']=np.log(bikes_prep['demand'])

# autocorrelation in demand column
t_1=bikes_prep['demand'].shift(+1).to_frame()
t_1.columns=['t-1']
    

t_2=bikes_prep['demand'].shift(+2).to_frame()
t_2.columns=['t-2']
    

t_3=bikes_prep['demand'].shift(+3).to_frame()
t_3.columns=['t-3']
    
bikes_prep_lag=pd.concat([bikes_prep,t_1,t_2,t_3],axis=1)
bikes_prep_lag=bikes_prep_lag.dropna()


#step:7 -create the dummy variable and drop first to avoid dummy variabl trap
#dealing the categorical data
bikes_prep_lag['season']=bikes_prep_lag['season'].astype('category')
bikes_prep_lag['holiday']=bikes_prep_lag['holiday'].astype('category')
bikes_prep_lag['weather']=bikes_prep_lag['weather'].astype('category')
bikes_prep_lag['month']=bikes_prep_lag['month'].astype('category')
bikes_prep_lag['hour']=bikes_prep_lag['hour'].astype('category')


bikes_prep_lag=pd.get_dummies(bikes_prep_lag,drop_first=True)

#step-8 ; create the train and test split
#split the x and y dataset into training and testing dataset
#from sklearn.model_selection import train_test_split
#x_train,x_test,y_train,y_test=   \
 #   train_test_split(x,y,test_size=.4,random_state=1224)
 # but here the demand is time dependent  
y=bikes_prep_lag[['demand']]
x=bikes_prep_lag.drop(['demand'],axis=1)
tr_size=int(.7*len(x))
x_train=x.values[0:tr_size]
x_test=x.values[tr_size:len(x)]

y_train=y.values[0:tr_size]
y_test=y.values[tr_size:len(y)]
 
#step-9 fit and score the model
from sklearn.linear_model import LinearRegression
std_reg=LinearRegression()
std_reg.fit(x_train,y_train)

r2_train=std_reg.score(x_train,y_train)
r2_test=std_reg.score(x_test,y_test)

# create y prediction
y_predict=std_reg.predict(x_test)
from sklearn.metrics import mean_squared_error
rmse=math.sqrt(mean_squared_error(y_test, y_predict))

#rmsle value
# as we have change the demand to the log value..
#we again take the exponent  to get the real value
y_test_e=[]
y_predict_e=[]
for i in range(0,len(y_test)):
    y_test_e.append(math.exp(y_test[i]))
    y_predict_e.append(math.exp(y_predict[i]))
    
    #calculate the sum
    
log_sq_sum=0   
for i in range(0,len(y_test_e)):
    log_a=math.log(y_test_e[i]+1)
    log_p=math.log(y_predict_e[i]+1)
    log_diff=(log_p-log_a)**2
    log_sq_sum=log_sq_sum+log_diff


rmsle=math.sqrt(log_sq_sum/len(y_test))
print(rmsle)









