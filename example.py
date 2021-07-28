import numpy as np
import pickle
import pandas as pd
import os

def Ncen_to_int(Ncen_probability):
	#This function outputs integer number of central based on the predicted probability of each classes 
	return np.where(np.random.uniform(np.rint(Ncen_probability[:,0]),np.rint(Ncen_probability[:,1]))<Ncen_probability[:,1],1,0)

def Nsat_to_int(Nsat_real):
	#This function outputs integer number of satellites based on the predicted real number
	return np.where(np.random.uniform(np.floor(Nsat_real),np.ceil(Nsat_real))<Nsat_real,np.ceil(Nsat_real),np.floor(Nsat_real)).astype(int)

#central model example
#create data for predicting central
data=np.zeros((3,4))
data=pd.DataFrame(data,columns=['vmax','z_lastmerg','mvir','a05']) 
data['vmax']=np.array([71.57522, 918.25134, 1081.4639])
data['z_lastmerg']=np.array([0.089288, 0.115883, 1.275846])
data['mvir']=np.array([7.573779, 14376.668, 26018.943])
data['a05']=np.array([0.540266, 0.470944, 0.537648])

#load random forest classification model for central galaxy
#here the model tested is the one with top 4 features
script_dir=os.path.dirname(__file__) #absolute dir the script is in
model_path="cenpred_top/cenpred_top.sav"
rfmodel=os.path.join(script_dir, model_path) #if other trained model is used, the data columns should include the features listed in README with the same order 
loaded_model=pickle.load(open(rfmodel,'rb'))

#predict the possibility of two class (0 or 1) for each halo
Ncen_proba=loaded_model.predict_proba(data)
#obtain the final number of central (0 or 1) based on predicted possibility 
Ncen_int=Ncen_to_int(Ncen_proba)
print('The number of central galaxy for these haloes are:',Ncen_int) # the output should be [0,1,1]	


#satellite model example
#create data for predicting satellite
data=np.zeros((3,4))
data=pd.DataFrame(data,columns=['mvir','g2_5','g1_25','con'])
data['mvir']=np.array([7.573779, 14376.668, 26018.943])
data['g2_5']=np.array([4.606767, 13.981967, 22.418219])
data['g1_25']=np.array([5.330508, 55.103374, 80.966299])
data['con']=np.array([1.040267, 1.077859, 1.041683])

#load random forest regression model for satellite galaxy
#load random forest classification model for central galaxy
#here the model tested is the one with top 4 features
model_path="satpred_top/satpred_top.sav"
rfmodel=os.path.join(script_dir, model_path)
loaded_model=pickle.load(open(rfmodel,'rb'))

#predict the number of satellites for each halo, could be non-integer
Nsat_pred=loaded_model.predict(data)
#obtain the integer number of satellite based on the direct prediction above  
Nsat_int=Nsat_to_int(Nsat_pred)
print('The number of satellite galaxies for these haloes are:',Nsat_int) # the output of the 1st halo should be 0. The 2nd should be 35 or 34 due to the randomness of assigning integer numbers, and the 3rd should be 61 or 60.		

