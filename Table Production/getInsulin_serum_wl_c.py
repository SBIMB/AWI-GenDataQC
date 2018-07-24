import pandas as pd

from table_generation import stat_and_QC
from globalVariables import *

'''def getInsulin_serum (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):'''
def getInsulin_serum ():
    '''Function to generate QC and statistics specific data for the column 'insulin' in the input spreadsheet.'''
    
    desired_var = 'insulin_withlimits_c'
    
    
    output_table_QC_insulin = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_insulin = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    
    
    writer_insulin = pd.ExcelWriter(output_table_QC_insulin)
    
    llq_insulin = 2.0
    ulq_insulin = 300.0

    
    
    stat_and_QC(desired_var, data_field1, output_values_QC_insulin, writer_insulin, 
                below_spec, above_spec, replaced_missing, replaced_branching, 
                replaced_missing_bio, replaced_missing_bio_ex)
    
    
    writer_insulin.save()
    
