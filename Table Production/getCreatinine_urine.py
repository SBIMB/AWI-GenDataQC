import pandas as pd

from table_generation import stat_and_QC



def getCreatinine_urine(replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):
    '''Function to generate QC and statistics specific data for the column 'ur_creatinine' in the input spreadsheet.'''
    
    
    desired_var = 'ur_creatinine'
    
    
    output_table_QC_creatinine_u = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_creatinine_u = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    
    
    writer_creatinine_u = pd.ExcelWriter(output_table_QC_creatinine_u)
    
    llq_creatinine_u = 375
    ulq_creatinine_u = 55000

    
    
    stat_and_QC(llq_creatinine_u, ulq_creatinine_u ,desired_var ,data_field1 , output_values_QC_creatinine_u, writer_creatinine_u , 
                replaced_missing, replaced_branching  )
    
    
    writer_creatinine_u.save()
    