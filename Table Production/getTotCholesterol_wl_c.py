import pandas as pd

from table_generation import stat_and_QC
from table_generation import Phenotype_1conditions
from globalVariables import *

'''def getTotCholesterol (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):'''
def getTotCholesterol ():
    '''Function to generate QC ,statistics and phenotype specific data for the column 'cholesterol_1' in the input spreadsheet.
    The phenotype specific data is classified based on 1 condition'''
    
    desired_var = 'cholesterol_1_withlimits_c'
    
    
    output_table_QC_tot_chol = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_tot_chol = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    output_value_phen_tot_chol = str(directory_for_output)  + str(desired_var) + "_" + "Phen-table_" + str(input_filename) + "_" + date_time_var + ".xls"
    
    writer_tot_chol = pd.ExcelWriter(output_table_QC_tot_chol)
    
    llq_tot_chol = 0.30
    ulq_tot_chol = 17.20
    con1_tot_chol = 5.0
    
    
    
    stat_and_QC(desired_var, data_field1, output_values_QC_tot_chol, writer_tot_chol, 
                below_spec, above_spec, replaced_missing, replaced_branching, 
                replaced_missing_bio, replaced_missing_bio_ex)
    
    Phenotype_1conditions( con1_tot_chol, desired_var ,data_field1 ,  writer_tot_chol ,
            output_value_phen_tot_chol)
    
    writer_tot_chol.save()
    
    
