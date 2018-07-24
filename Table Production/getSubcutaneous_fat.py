# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 08:49:19 2018

@author: Freedom
"""

import pandas as pd

from table_generation import stat_and_QC
from table_generation import Phenotype_1conditions
from globalVariables import *

'''def getSubcutaneous_fat (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):'''
def getSubcutaneous_fat ():
    '''Function to generate QC ,statistics and phenotype specific data for the column 'subglycerides' in the input spreadsheet.
    The phenotype specific data is classified based on 1 condition'''

    desired_var = 'subcutaneous_fat'    
    
    output_table_QC_sub = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_sub = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    output_value_phen_sub = str(directory_for_output)  + str(desired_var) + "_" + "Phen-table_" + str(input_filename) + "_" + date_time_var + ".xls"
    
    writer_sub = pd.ExcelWriter(output_table_QC_sub)
    
    llq_sub = 0.13
    ulq_sub = 5.60
    con1_sub = 1.7
    
    
    
    
    
    stat_and_QC(desired_var, data_field1, output_values_QC_sub, writer_sub, 
                below_spec, above_spec, replaced_missing, replaced_branching, 
                replaced_missing_bio, replaced_missing_bio_ex)
    
    Phenotype_1conditions( con1_sub, desired_var ,data_field1 ,  writer_sub,
            output_value_phen_sub)
    
    writer_sub.save()
