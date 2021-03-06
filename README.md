# Description

The .7z files are compressed trained random forest models for predicting the number of central and satellite galaxies (above the stellar mass threshold 1.42*10^10M_sun/h) based on input halo internal or environmental properties. The predicted number of galaxies can then be used to populate dark matter halos to create mock galaxy catalog with the specific stellar mass threshold. The prediction is fast once the model is loaded. It takes about 0.1 second to predict central or satellite in 10000 haloes on a single CPU of 4.2GHz (Intel Core i7-7700). For more information about the models, please see arXiv:2107.01223. Examples of how to load the models are shown in examples.py 

The models are trained based on the Guo et al. 2011 semi-analytic galaxy sample implemented on the [Millennium simulation](https://wwwmpa.mpa-garching.mpg.de/millennium/). The inputs are halo internal or/and environmental properties, and the outputs are the number of central or satellite galaxies in each halo. Centrals are predicted by random forest classification, saved in folders named 'cenpred_*'. Satellites are predicted by random forest regression, saved in folders named 'satpred_*'. Description of each model and the required input halo properties are listed in the first table below. 

# Load the models 

The models do not need an installation, and only a few basic python packages are required. **Required python package are: numpy, pandas, pickle.**

**Each model is saved in one folder as compressed file/files. Files in one folder need to be decompressed together. Decompressed files will be in the type of .sav.** 

After the decompression, the models can be directly import from python. Examples of how to load the models are shown in examples.py 

# Model details

Models with different sets of input are listed below:

| Model | Description | Input features |
| ---------- | ----------- | -------------- |
| cenpred_all <br /> satpred_all| models with all halo features as input | 'con','mvir','vmax','a05','a08','vpeak','zvpeak','macc','smacc','mergnum',<br /> 'z_firstmerg','z_lastmerg','total_spin','g1_25','g2_5','g5','g10','alpha'|
| cenpred_top <br /> satpred_top| models with top 4 features as input <br /> for central and satellite separately | cenpred_top: 'vmax','z_lastmerg','mvir','a05' <br /> satpred_top: 'mvir','g2_5','g1_25','con'|
| cenpred_in <br /> satpred_in| models with halo internal features as input | 'con','mvir','vmax','a05','a08','vpeak','zvpeak', <br /> 'macc','smacc','mergnum','z_firstmerg','z_lastmerg','total_spin'|
| cenpred_ME <br /> satpred_ME| models with halo mass and environment as input | 'mvir','g1_25'|
| cenpred_non <br /> satpred_non| models with non-tree related halo features (not calculated from the merger tree) as input | 'mvir','vmax','con','total_spin','g1_25'|
          
**Important: when using the models, the halo features need to be listed in the same order as described above, and the units need to be the same as listed below.** 


# Description of input halo features:
| Feature | Unit | Descriptions |
| ------- | ---- | ------------ |
| 'mvir' | 10^10M_sun/h | viral mass of halo defined as 200 times of critical density. |
| 'con' | - | concentration parameter estimated by V_max/V_vir. |
| 'vmax' | km/s | maximum circular velocity. |
| 'vpeak' | km/s | peak maximum circular velocity in the history of the halo. |
| 'zvpeak' | - | redshift at the time reaching vpeak. |
| 'a05' | - | the cosmic scale factor at the time the halo reaches 0.5*final mass (for the first time in the merger history). |
| 'a08' | - | the cosmic scale factor at the time the halo reaches 0.8*final mass (for the first time in the merger history). |
| 'macc' | M_sun/(h*yr) | mass accretion rate during z=0.02 and z=0. |
| 'smacc' | 1/(10^10*yr) | specific mass accretion rate, 'macc' devided by 'mvir'. |
| 'mergnum' | - | the number of major mergers in the history of the halo. Major mergers are defined by a ratio of 3:1 between progenitors.|
| 'z_firstmerg' | - | redshift of the first major merger, if 'mergnum'=0, 'z_firstmerg' is set to 99999.0.|
| 'z_lastmerg' | - | redshift of the last major merger, if 'mergnum'=0, 'z_lastmerg' is set to 99999.0.|
| 'total_spin' | (Mpc/h)(km/s) | specific angular momentom of the halo. |
| 'g1_25' | - | matter density field smoothed with a Gaussian filter of radius 1.25 Mpc/h, normalized by mean density. |
| 'g2_5' | - | matter density field smoothed with a Gaussian filter of radius 2.5 Mpc/h. |
| 'g5' | - | matter density field smoothed with a Gaussian filter of radius 5 Mpc/h. |
| 'g10' | - | matter density field smoothed with a Gaussian filter of radius 10 Mpc/h. |
| 'alpha' | - | tidal anisotropy. |



