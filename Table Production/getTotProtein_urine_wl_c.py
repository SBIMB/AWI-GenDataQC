import pandas as pd

from table_generation import stat_and_QC
from globalVariables import *

'''def getTotProtein_urine(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):'''
def getTotProtein_urine():
    '''Function to generate QC and statistics specific data for the column 'ur_protein' in the input spreadsheet.'''
    
    desired_var = 'ur_protein_withlimits_c'
    
    
    output_table_QC_TotProtein = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_TotProtein = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    
    
    writer_TotProtein = pd.ExcelWriter(output_table_QC_TotProtein)
    
    llq_TotProtein = 10
    ulq_TotProtein = 1000

    
    
    stat_and_QC(desired_var, data_field1, output_values_QC_TotProtein, writer_TotProtein, 
                below_spec, above_spec, replaced_missing, replaced_branching, 
                replaced_missing_bio, replaced_missing_bio_ex)
    
    
    writer_TotProtein.save()
    
