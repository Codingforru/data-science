
# data pre processing

import pandas as pd
dataset=pd.read_csv('loan_small.csv')
# aacess the data using the index values
c=dataset['ApplicantIncome'].mean()


# to remove particuler coulmns
cleandata=dataset.dropna(subset=['Loan_Status'])


#mode for missing catagorical variable and mean for numericals values
dt=cleandata.copy()
cols=['Gender','Area','Loan_Status']
dt[cols]=dt[cols].fillna(dt.mode().iloc[0])
dt.isnull().sum(axis=0)


#replace the numerical variable with mean
cols2=['ApplicantIncome','CoapplicantIncome','LoanAmount']
dt[cols2]=dt[cols2].fillna(dt.mean()) 
dt.isnull().sum(axis=0)

    
dt=dt.drop("Loan_ID",1)

#using the one hot coding creating the dummyy variable

dt=pd.get_dummies(dt,drop_first=True)
   
# split  the data vertically

x=dt.iloc[:,:-1]      #all except las, independent variable (predictor)
y=dt.iloc[:,-1]        # only the last                                      
    
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=     \
    train_test_split(x,y,test_size=0.2,random_state=1234)
    













