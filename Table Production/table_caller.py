# Code utilised to call the functions responsible for generating the tables
#associated with each biomarker 

import pandas as pd

from getVariable import getVariable
from getGlucose import getGlucose
from getGlucose_wl_c import getGlucose_wl_c
from getTriglycerides import getTriglycerides
from getTotCholesterol import getTotCholesterol
from getLDL import getLDL
from getCreatinine_serum  import getCreatinine_serum 
from getInsulin_serum  import getInsulin_serum 
from getAlbumin_urine import getAlbumin_urine
from getTotProtein_urine import getTotProtein_urine
from getCreatinine_urine import getCreatinine_urine
from getHDL import getHDL 
from getACR  import  getACR 
from getVisceral_fat import getVisceral_fat
from getSubcutaneous_fat import getSubcutaneous_fat 
from globalVariables import *

#directory_for_input = "/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/"
#input_filename = "new.csv"

data_field1 = pd.read_csv(input_file,low_memory=False)
field_names_list = data_field1.columns.tolist()
for var in field_names_list:
    getVariable(var)
    
#data_field1
#getVariable()
#getGlucose()
#getGlucose_wl_c()
#getTriglycerides()
#getTotCholesterol()
#getLDL()
#getCreatinine_serum ()
#getInsulin_serum()
#getAlbumin_urine()
#getTotProtein_urine()
#getCreatinine_urine()
#getHDL()
#getACR ()
#getVisceral_fat()
#getSubcutaneous_fat()
'''getNonHDLCC()'''
'''friedewald_ldl_c_c'''
'''BMI
...with phenotype categories
...BMI<18.5, BMI ≥18.5 and <25 ≥25 to <29.9 and ≥30 kg/m2)'''
'''height'''
'''weight'''
'''waist circumference'''
'''hip circumference'''
'''Waist/hip ratio'''
'''systolic_1'''
'''systolic_2'''
'''systolic_3'''
'''bp_sys_avg'''
'''diastolic_1'''
'''diastolic_2'''
'''disatolic_3'''
'''bp_dia_avg'''
'''pulse_1'''
'''pulse_2'''
'''pulse_3'''
'''pulse_avg'''