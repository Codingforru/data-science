
demand is not normally distributed
tem and atemp appear to have direct correlation
humidity and windspeed affect demand but need more statistical analysis

- features to be dropped
  - weekdays
  -years
  -workingday
  -atemp
  -windspeed
  by seeing the correlation  there is a linearity b/w  winspeed and humdity  \
      so we can droped 1.
high autocorrelation in demand feature
bikes_prep_lag['season']=bikes_prep_lag['season'].astype('category')
bikes_prep_lag['holiday']=bikes_prep_lag['holiday'].astype('category')
bikes_prep_lag['weather']=bikes_prep_lag['weather'].astype('category')
bikes_prep_lag['month']=bikes_prep_lag['month'].astype('category')
bikes_prep_lag['hour']=bikes_prep_lag['hour'].astype('category')
