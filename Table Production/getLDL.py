import pandas as pd

from table_generation import stat_and_QC
from table_generation import Phenotype_1conditions


def getLDL (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):
    '''Function to generate QC ,statistics and phenotype specific data for the column 'ldl' in the input spreadsheet.
    The phenotype specific data is classified based on 1 condition'''
    
    desired_var = 'ldl'
    
    
    output_table_QC_ldl = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_ldl = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    output_value_phen_ldl = str(directory_for_output)  + str(desired_var) + "_" + "Phen-table_" + str(input_filename) + "_" + date_time_var + ".xls"
    
    writer_ldl = pd.ExcelWriter(output_table_QC_ldl)
    
    llq_ldl = 0.40
    ulq_ldl = 4.90
    con1_tot_ldl = 3.0
    
    
    stat_and_QC(llq_ldl, ulq_ldl ,desired_var ,data_field1 , output_values_QC_ldl , writer_ldl , 
                replaced_missing, replaced_branching  )
    
    Phenotype_1conditions( con1_tot_ldl, desired_var ,data_field1 ,  writer_ldl ,
            output_value_phen_ldl)
    
    writer_ldl.save()
    



