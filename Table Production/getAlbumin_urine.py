import pandas as pd
from table_generation import stat_and_QC



def getAlbumin_urine(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):
    '''Function to generate QC and statistics specific data for the column 'ur_albumin' in the input spreadsheet.'''
    
    desired_var = 'ur_albumin'
    
    
    output_table_QC_albumin = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_albumin = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    
    
    writer_albumin = pd.ExcelWriter(output_table_QC_albumin)
    
    llq_albumin = 0.05
    ulq_albumin = 6.08

    
    
    stat_and_QC(llq_albumin, ulq_albumin ,desired_var ,data_field1 , output_values_QC_albumin , writer_albumin , 
                replaced_missing, replaced_branching  )
    
    
    writer_albumin.save()
    
