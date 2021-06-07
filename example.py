import numpy as np
import pickle
import pandas as pd

#central model example
#create data for predicting central
data=np.zeros((2,4))
data=pd.DataFrame(data,columns=['vmax','z_lastmerg','mvir','a05'])
data['vmax']=np.array([70., 80.])
data['z_lastmerg']=np.array([0.1, 0.2])
data['mvir']=np.array([10., 11.])
data['a05']=np.array([0.3, 0.5])

#load random forest classification model for central galaxy
#here the model tested is the one with top 4 features
rfmodel='cenpred_top.sav'
loaded_model=pickle.load(open(rfmodel,'rb'))

#predict the possibility of two class (0 or 1) for each halo
Ncen_proba=loaded_model.predict_proba(data)
#obtain the final number of central (0 or 1) based on predicted possibility 
Ncen_int=np.where(np.random.uniform(np.rint(Ncen_proba[:,0]),np.rint(Ncen_proba[:,1]))<Ncen_proba[:,1],1,0)
print(Ncen_int)	


#satellite model example
#create data for predicting satellite
data=np.zeros((2,4))
data=pd.DataFrame(data,columns=['mvir','g2_5','g1_25','con'])
data['mvir']=np.array([10., 11.])
data['g2_5']=np.array([4., 3.])
data['g1_25']=np.array([5., 4.])
data['con']=np.array([1., 1.5])

#load random forest regression model for satellite galaxy
#load random forest classification model for central galaxy
#here the model tested is the one with top 4 features
rfmodel='satpred_top.sav'
loaded_model=pickle.load(open(rfmodel,'rb'))

#predict the number of satellites for each halo, could be non-integer
Nsat_pred=loaded_model.predict(data)
#obtain the integer number of satellite based on the direct prediction above  
Nsat_int=np.where(np.random.uniform(np.floor(Nsat_pred),np.ceil(Nsat_pred))<Nsat_pred,np.ceil(Nsat_pred),np.floor(Nsat_pred))
print(Nsat_int)	

