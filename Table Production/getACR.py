
import pandas as pd
from table_generation import Phenotype_3condition_sex_4func
from globalVariables import *

'''def getACR (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):'''
def getACR ():
    '''Function to generate phenotype specific data capturing for the column acr in the input spreadsheet.
    This phenotype data is sex specific and is classified in both casses into 4 classes.'''

    desired_var = 'acr'
    con_m_1 = 2.5
    con_f_1 = 3.5
    con_m_2 = 25
    con_f_2 = 35
    
    output_table_QC_acr = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_value_phen_acr = str(directory_for_output)  + str(desired_var) + "_" + "Phen-table_" + str(input_filename) + "_" + date_time_var + ".xls"
    
    writer_acr = pd.ExcelWriter(output_table_QC_acr)
    
    Phenotype_3condition_sex_4func(  desired_var ,data_field1 ,writer_acr,
                                   output_value_phen_acr,con_m_1,con_m_2,con_f_1,con_f_2)
    

    
    writer_acr.save()
    
