import pandas as pd

from table_generation import stat_and_QC
from globalVariables import *

'''def getCreatinine_urine(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):'''
def getCreatinine_urine():
    '''Function to generate QC and statistics specific data for the column 'ur_creatinine' in the input spreadsheet.'''
    
    
    desired_var = 'ur_creatinine_withlimits_c'
    
    
    output_table_QC_creatinine_u = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_creatinine_u = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    
    
    writer_creatinine_u = pd.ExcelWriter(output_table_QC_creatinine_u)
    
    llq_creatinine_u = 3.75
    ulq_creatinine_u = 550.00

    
    
    stat_and_QC(desired_var, data_field1, output_values_QC_creatinine_u, writer_creatinine_u, 
                below_spec, above_spec, replaced_missing, replaced_branching, 
                replaced_missing_bio, replaced_missing_bio_ex)
    
    
    writer_creatinine_u.save()
    