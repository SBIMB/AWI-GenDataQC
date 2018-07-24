import pandas as pd

from table_generation import stat_and_QC
from table_generation import Phenotype_5conditions
from globalVariables import *

def getGlucose_wl_c ():
    '''Function to generate QC ,statistics and phenotype specific data for the column 'glucose'' in the input spreadsheet.
    The phenotype specific data is classified into 5 different classes'''
    
    desired_var = 'glucose_withlimits_c'
    

    output_table_QC_glucose = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_glucose = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    output_value_phen_glucose = str(directory_for_output)  + str(desired_var) + "_" + "Phen-table_" + str(input_filename) + "_" + date_time_var + ".xls"
    
    writer_glucose = pd.ExcelWriter(output_table_QC_glucose)
    
    llq_glucose = 0.36
    '''ulq_glucose = 35'''
    con1_glucose = 5.60
    con2_glucose = 7.00
    con3_glucose = 11.10   
    
    stat_and_QC(desired_var ,data_field1 , output_values_QC_glucose , writer_glucose, 
                replaced_missing, replaced_branching, below_spec,
                above_spec, replaced_missing_bio, replaced_missing_bio_ex)
    
    Phenotype_5conditions(llq_glucose, con1_glucose, con2_glucose ,
             con3_glucose, desired_var ,data_field1 ,  writer_glucose,
            output_value_phen_glucose )
    
    writer_glucose.save()