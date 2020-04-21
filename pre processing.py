# data pre processing

import pandas as pd
dataset=pd.read_csv('loan_small.csv')
# aacess the data using the index values

subset=dataset.iloc[0:3,1:3]
# level base indexing
substN= dataset.loc["0":"3", "Gender":"ApplicantIncome"]

datasetT=pd.read_csv('loan_small_tsv.txt',sep='\t')

#acess the data for quick review using the head

dataset.head()

# to get the shape of dataset
dataset.shape

# to get columns names
dataset.columns

#identify the columns with the missing values along with the count
dataset.isnull().sum(axis=0)

#replacing the missing values
#drop the rows with missing values
cleandata=dataset.dropna()

# to remove particuler coulmns
cleandata=dataset.dropna(subset=['Loan_Status'])


#mode for missing catagorical variable and mean for numericals values
dt=dataset.copy()
cols=['Gender','Area','Loan_Status']
dt[cols]=dt[cols].fillna(dt.mode().iloc[0])
dt.isnull().sum(axis=0)


#replace the numerical variable with mean
cols2=['ApplicantIncome','CoapplicantIncome','LoanAmount']
dt[cols2]=dt[cols2].fillna(dt.mean()) 
dt.isnull().sum(axis=0)


#label encoding using pandas
dt.dtypes
#change the data types to catagories
dt[cols]=dt[cols].astype('category')

dt.dtypes
for columns  in cols:
    dt[columns]=dt[columns].cat.codes
    
df2=dataset.drop("Loan_ID",1)

#using the one hot coding
df2=pd.get_dummies(df2)
   
 

    
    













