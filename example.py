import numpy as np
import pickle
import pandas as pd

def Ncen_to_int(Ncen_probability):
	#This function outputs integer number of central based on the predicted probability of each classes 
	return np.where(np.random.uniform(np.rint(Ncen_probability[:,0]),np.rint(Ncen_probability[:,1]))<Ncen_probability[:,1],1,0)

def Nsat_to_int(Nsat_real):
	#This function outputs integer number of satellites based on the predicted real number
	return np.where(np.random.uniform(np.floor(Nsat_real),np.ceil(Nsat_real))<Nsat_real,np.ceil(Nsat_real),np.floor(Nsat_real)).astype(int)

#central model example
#create data for predicting central
data=np.zeros((2,4))
data=pd.DataFrame(data,columns=['vmax','z_lastmerg','mvir','a05']) 
data['vmax']=np.array([71.57522, 918.25134])
data['z_lastmerg']=np.array([0.089288, 0.115883])
data['mvir']=np.array([7.573779, 14376.668])
data['a05']=np.array([0.540266, 0.470944])

#load random forest classification model for central galaxy
#here the model tested is the one with top 4 features
rfmodel='cenpred_top.sav' #if other trained model is used, the data columns should include the features listed in README with the same order 
loaded_model=pickle.load(open(rfmodel,'rb'))

#predict the possibility of two class (0 or 1) for each halo
Ncen_proba=loaded_model.predict_proba(data)
#obtain the final number of central (0 or 1) based on predicted possibility 
Ncen_int=Ncen_to_int(Ncen_proba)
print('The number of central galaxy for these haloes are:',Ncen_int) # the output should be [0,1]	


#satellite model example
#create data for predicting satellite
data=np.zeros((2,4))
data=pd.DataFrame(data,columns=['mvir','g2_5','g1_25','con'])
data['mvir']=np.array([7.573779, 14376.668])
data['g2_5']=np.array([4.606767, 13.981967])
data['g1_25']=np.array([5.330508, 55.103374])
data['con']=np.array([1.040267, 1.077859])

#load random forest regression model for satellite galaxy
#load random forest classification model for central galaxy
#here the model tested is the one with top 4 features
rfmodel='satpred_top.sav'
loaded_model=pickle.load(open(rfmodel,'rb'))

#predict the number of satellites for each halo, could be non-integer
Nsat_pred=loaded_model.predict(data)
#obtain the integer number of satellite based on the direct prediction above  
Nsat_int=Nsat_to_int(Nsat_pred)
print('The number of satellite galaxies for these haloes are:',Nsat_int) # the output should be [0,35] or [0,34] due to the randomness of assigning integer numbers		

