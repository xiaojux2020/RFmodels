# RFmodels

The .sav files are trained RF models for predicting the number of central and satellite galaxies of the stellar mass threshold 1.42*10^10M_sun/h. Examples of how to load the models are shown in examples.py 

The models are trained based on the Guo et al. 2011 semi-analytic galaxy sample implemented on the Millennium simulation. The inputs are halo internal or/and environmental properties, and the outputs are the number of central or satellite galaxies in each halo. Centrals are predicted by random forest classification, saved in files of name 'cenpred_*.sav'. Satellites are predicted by random forest regression, saved in files of name 'satpred_*.sav'. Models with different input halo features are indicated after '_' in the file name:
(1) _all: models with all halo features (listed below) as input.
(2) _top: models with top 4 features as input. 
          The top 4 features are 'vmax','z_lastmerg','mvir','a05' for central and 'mvir','g2_5','g1_25','con' for satellite.
(3) _in: models with halo internal features as input. 
         The internal features are: 'con','mvir','vmax','a05','a08','vpeak','zvpeak','macc','smacc','mergnum','z_firstmerg','z_lastmerg','total_spin'
(4) _ME: models with halo mass and environment ('mvir' and 'g1_25') as input. 
(4) _non: models with non-tree related halo features (not calculated from the merger tree) as input. 
          The non-tree related features are: 'mvir','vmax','con','total_spin','g1_25'
!Important: when using the models, the halo features need to be listed in the same order as described here.          
          
Descriptions of halo features:
(1)'mvir', viral mass of halo defined as 200 times of critical density, in the unit of 10^10M_sun/h.
(2)'con', concentration parameter estimated by V_max/V_vir
(3)'vmax', maximum circular velocity, in the unit of km/s
(4)'a05', the cosmic scale factor at the time the halo reaches 0.5*final mass (for the first time in the merger history), unit less value in range of 0~1.
(5)'a08', the cosmic scale factor at the time the halo reaches 0.8*final mass (for the first time in the merger history).
(6)'vpeak', peak maximum circular velocity, in the unit of km/s.
(7)'zvpeak', redshift at the time reaching vpeak.
(8)'macc', mass accretion rate during z=0.02 and z=0, in the unit of M_sun/h/yr.
(9)'smacc', specific mass accretion rate, 'macc' devided by 'mvir'.
(10)'mergnum', the number of major mergers in the history of the halo. Major mergers are defined by a ratio of 3:1 between progenitors.  
(11)'z_firstmerg', redshift of the first major merger, if 'mergnum'=0, 'z_firstmerg' is set to 99999.0.
(12)'z_lastmerg', redshift of the last major merger, if 'mergnum'=0, 'z_lastmerg' is set to 99999.0.
(13)'total_spin', specific angular momentom of the halo, in the unit of (Mpc/h)(km/s).
(14)'g1_25', matter density field smoothed with a Gaussian filter of radius 1.25 Mpc/h, normalized by mean density. 
(15)'g2_5', matter density field smoothed with a Gaussian filter of radius 2.5 Mpc/h.
(16)'g5', matter density field smoothed with a Gaussian filter of radius 5 Mpc/h.
(17)'g10', matter density field smoothed with a Gaussian filter of radius 10 Mpc/h.
(19)'alpha', tidal anisotropy.        
