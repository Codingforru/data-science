# normalisation to the same scale

import pandas as pd
dataset=pd.read_csv('loan_small.csv')
cleandataset=dataset.dropna()
#extract the numerical columns
data_to_scale=cleandataset.iloc[:,2:5]

from sklearn.preprocessing import StandardScaler

scaler_=StandardScaler()
ss_scaler=scaler_.fit_transform(data_to_scale)


#minmax scaler


from sklearn.preprocessing import minmax_scale
mm_scaler=minmax_scale(data_to_scale)

