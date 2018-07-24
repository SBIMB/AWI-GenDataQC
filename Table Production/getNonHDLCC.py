# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 08:50:24 2018

@author: Freedom Mukomana
"""

import pandas as pd

from table_generation import stat_and_QC
from table_generation import Phenotype_5conditions
from globalVariables import *

'''def getNonHDLCC (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):'''
def getNonHDLCC ():
    '''Function to generate QC ,statistics and phenotype specific data for the column 'NonHDLCC' in the input spreadsheet.
    The phenotype specific data is classified into 5 different classes'''
    
    desired_var = 'NonHDLCC_withlimits_c'
    

    output_table_QC_NonHDLCC = str(directory_for_output) + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_NonHDLCC = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    output_value_phen_NonHDLCC = str(directory_for_output)  + str(desired_var) + "_" + "Phen-table_" + str(input_filename) + "_" + date_time_var + ".xls"
    
    writer_NonHDLCC = pd.ExcelWriter(output_table_QC_NonHDLCC)
    
    llq_NonHDLCC = 0.36
    '''ulq_NonHDLCC = 35'''
    con1_NonHDLCC = 5.60
    con2_NonHDLCC = 7.00
    con3_NonHDLCC = 11.10   
    
    stat_and_QC(desired_var, data_field1, output_values_QC_NonHDLCC, writer_NonHDLCC, 
                below_spec, above_spec, replaced_missing, replaced_branching, 
                replaced_missing_bio, replaced_missing_bio_ex)
    
    Phenotype_5conditions(llq_NonHDLCC, con1_NonHDLCC, con2_NonHDLCC ,
             con3_NonHDLCC, desired_var ,data_field1 ,  writer_NonHDLCC,
            output_value_phen_NonHDLCC )
    
    writer_NonHDLCC.save()