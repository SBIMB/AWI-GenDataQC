import pandas as pd

from table_generation import stat_and_QC
from table_generation import Phenotype_1conditions



def getTriglycerides (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):
    '''Function to generate QC ,statistics and phenotype specific data for the column 'triglycerides' in the input spreadsheet.
    The phenotype specific data is classified based on 1 condition'''

    desired_var = 'triglycerides'
    
    
    output_table_QC_tri = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_tri = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    output_value_phen_tri = str(directory_for_output)  + str(desired_var) + "_" + "Phen-table_" + str(input_filename) + "_" + date_time_var + ".xls"
    
    writer_tri = pd.ExcelWriter(output_table_QC_tri)
    
    llq_tri = 0.13
    ulq_tri = 5.60
    con1_tri = 1.7
    
    
    
    
    
    stat_and_QC(llq_tri, ulq_tri ,desired_var ,data_field1 , output_values_QC_tri , writer_tri, 
                replaced_missing, replaced_branching  )
    
    Phenotype_1conditions( con1_tri, desired_var ,data_field1 ,  writer_tri,
            output_value_phen_tri)
    
    writer_tri.save()
