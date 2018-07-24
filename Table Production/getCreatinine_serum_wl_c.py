import pandas as pd

from table_generation import stat_and_QC
from globalVariables import *



'''def getCreatinine_serum (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):'''
def getCreatinine_serum ():
    '''Function to generate QC and statistics specific data for the column 's_creatinine' in the input spreadsheet.'''
    
    desired_var = 's_creatinine_withlimits_c'
    
    
    output_table_QC_creatinine_s = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_creatinine_s = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    
    
    writer_creatinine_s = pd.ExcelWriter(output_table_QC_creatinine_s)
    
    llq_creatinine_s = 11.80
    ulq_creatinine_s = 2448

    
    
    stat_and_QC(desired_var, data_field1, output_values_QC_creatinine_s, writer_creatinine_s, 
                below_spec, above_spec, replaced_missing, replaced_branching, 
                replaced_missing_bio, replaced_missing_bio_ex)
    
    
    writer_creatinine_s.save()
    
