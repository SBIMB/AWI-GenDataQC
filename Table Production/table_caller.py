import pandas as pd
import datetime

from table_generation import skeleton

#Set up variables 
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
desired_var = 'glucose'

#output_table_QC = str(directory_for_output) + "Table_" + str(desired_var) + "_" + str(input_filename) + "_" + str(date_time_var) + ".xls"
output_table_QC = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
output_values_QC = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
output_table_phen = str(directory_for_output)  + str(desired_var) + "_" + "Phen-table_" + str(input_filename) + "_" + date_time_var + ".xls"

llq_glucose = 0.36
ulq_glucose = 35
con1_glucose = 5.60
con2_glucose = 7.00
con3_glucose = 11.10


data_field1 = pd.read_csv(input_file,low_memory=False)

skeleton(llq_glucose, ulq_glucose, con1_glucose, con2_glucose ,
         con3_glucose, desired_var ,data_field1 , output_values_QC , output_table_QC,
         output_table_phen, replaced_missing, replaced_branching  )


