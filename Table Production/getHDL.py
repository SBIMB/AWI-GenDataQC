import pandas as pd

from table_generation import stat_and_QC
from table_generation import Phenotype_1condition_sex_2func


def getHDL (replaced_missing,replaced_branching,input_filename,data_field1,date_time_var,directory_for_output):
    
    desired_var = 'hdl'
    
    
    output_table_QC_hdl = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_hdl = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    output_value_phen_hdl = str(directory_for_output)  + str(desired_var) + "_" + "Phen-table_" + str(input_filename) + "_" + date_time_var + ".xls"
    
    writer_hdl = pd.ExcelWriter(output_table_QC_hdl)
    
    llq_hdl = 0.05
    ulq_hdl = 3.80
    con_m = 1.0
    con_f = 1.3
   
    
    
    stat_and_QC(llq_hdl, ulq_hdl ,desired_var ,data_field1 , output_values_QC_hdl , writer_hdl , 
                replaced_missing, replaced_branching  )
    
    Phenotype_1condition_sex_2func(  desired_var ,data_field1 ,writer_hdl, output_value_phen_hdl,con_m,con_f)
    

    
    writer_hdl.save()
    



