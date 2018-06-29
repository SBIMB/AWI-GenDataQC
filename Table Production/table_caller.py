import pandas as pd
import datetime

from getGlucose import getGlucose
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

#Set up variables 
#replaced missing and replced branching must be negative values
replaced_missing = -999
replaced_branching = -555
#directory_for_input = "/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/"
#input_filename = "new.csv"
directory_for_input = "/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/data/"
input_filename = "all_sites_v2.5.2.csv"
directory_for_output = "/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/QC_table/"
present_datetime = datetime.datetime.now()
date_time_var = present_datetime.strftime("%d-%m-%Y_%H-%M")

input_file = directory_for_input + input_filename 
data_field1 = pd.read_csv(input_file,low_memory=False)


getGlucose (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)
getTriglycerides (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)
getTotCholesterol(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)
getLDL(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)
getCreatinine_serum (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)
getInsulin_serum(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)
getAlbumin_urine(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)
getTotProtein_urine(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)
getCreatinine_urine(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)
getHDL(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)
getACR (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output)