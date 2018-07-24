import pandas as pd
from table_generation import stat_and_QC
from globalVariables import *

'''def getAlbumin_urine(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):'''
def getAlbumin_urine():
    '''Function to generate QC and statistics specific data for the column 'ur_albumin' in the input spreadsheet.'''
    
    desired_var = 'ur_albumin_withlimits_c'
    
    
    output_table_QC_albumin = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_albumin = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    
    
    writer_albumin = pd.ExcelWriter(output_table_QC_albumin)
    
    llq_albumin = 3.00
    ulq_albumin = 400.00

    
    
    stat_and_QC(desired_var, data_field1, output_values_QC_albumin, writer_albumin, 
                below_spec, above_spec, replaced_missing, replaced_branching, 
                replaced_missing_bio, replaced_missing_bio_ex)
    
    
    writer_albumin.save()
    
