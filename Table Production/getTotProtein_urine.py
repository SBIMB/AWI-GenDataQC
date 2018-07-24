import pandas as pd

from table_generation import stat_and_QCC
from globalVariables import *

def getTotProtein_urine():
    '''Function to generate QC and statistics specific data for the column 'ur_protein' in the input spreadsheet.'''
    
    desired_var = 'ur_protein'
    
    
    output_table_QC_TotProtein = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_TotProtein = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    
    
    writer_TotProtein = pd.ExcelWriter(output_table_QC_TotProtein)
    
    llq_TotProtein = 40
    ulq_TotProtein = 2000

    
    
    stat_and_QCC(llq_TotProtein, ulq_TotProtein ,desired_var ,data_field1 , output_values_QC_TotProtein, writer_TotProtein , 
                replaced_missing, replaced_branching  )
    
    
    writer_TotProtein.save()
