import pandas as pd
import datetime

from getGlucose import getGlucose
from getTriglycerides import getTriglycerides
from getTotCholesterol import getTotCholesterol
from getLDL import getLDL


#Set up variables 
#replaced missing and replced branching must be negative values!
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

