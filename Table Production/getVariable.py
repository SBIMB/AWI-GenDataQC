import pandas as pd

from table_generation import stat_and_QCC
from table_generation import stat_and_QC
from table_generation import Phenotype_5conditions
from table_generation import Phenotype_1conditions
from table_generation import Phenotype_1condition_sex_2func
from table_generation import Phenotype_3condition_sex_4func
from globalVariables import *

def getVariable (desired_var):
    '''Function to generate QC ,statistics and phenotype specific data for the column 'glucose'' in the input spreadsheet.
    The phenotype specific data is classified into 5 different classes'''
    
    #desired_var = 'glucose'
    
    
    output_table_QC_variable = str(directory_for_output)  + str(desired_var) + "_" + "QC-tables_" + str(input_filename) + "_" + date_time_var + ".xls"
    output_values_QC_variable = directory_for_output + desired_var + "_" + "QC-values_" + input_filename + "_" + date_time_var + ".xls"
    output_value_phen_variable = str(directory_for_output)  + str(desired_var) + "_" + "Phen-table_" + str(input_filename) + "_" + date_time_var + ".xls"
    
    writer_variable = pd.ExcelWriter(output_table_QC_variable)
    
    #glucose
    llq_glucose = 0.36
    ulq_glucose = 35
    con1_glucose = 5.60
    con2_glucose = 7.00
    con3_glucose = 11.10  
    
    #triglycerides
    llq_tri = 0.13
    ulq_tri = 5.60
    con1_tri = 1.7
    
    #    getTotCholesterol()
    llq_tot_chol = 0.30
    ulq_tot_chol = 17.20
    con1_tot_chol = 5.0
    
    #    getLDL()
    llq_ldl = 0.40
    ulq_ldl = 4.90
    con1_tot_ldl = 3.0
    
    #    getCreatinine_serum ()
    llq_creatinine_s = 11.80
    ulq_creatinine_s = 2448
    
    #    getInsulin_serum()
    llq_insulin = 2.0
    ulq_insulin = 300.0  
    
    #    getAlbumin_urine()
    llq_albumin = 0.05
    ulq_albumin = 6.08   
    
    #    getTotProtein_urine()
    llq_TotProtein = 40
    ulq_TotProtein = 2000
    
    #    getCreatinine_urine()
    llq_creatinine_u = 375
    ulq_creatinine_u = 55000
    
    #    getHDL()
    llq_hdl = 0.05
    ulq_hdl = 3.80
    con_m = 1.0
    con_f = 1.3
    
    #    getACR()
    con_m_1 = 2.5
    con_f_1 = 3.5
    con_m_2 = 25
    con_f_2 = 35
    
    #    getVisceral_fat()
    llq_vat = 0.13
    ulq_vat = 5.60
    con1_vat = 1.7  
    
    #    getSubcutaneous_fat()
    llq_sub = 0.13
    ulq_sub = 5.60
    con1_sub = 1.7
   
    if desired_var == 'glucose':
        print(desired_var)
        stat_and_QCC(llq_glucose, ulq_glucose ,desired_var ,data_field1 , 
                     output_values_QC_variable , writer_variable, replaced_missing, 
                     replaced_branching)
    
        Phenotype_5conditions(llq_glucose, con1_glucose, con2_glucose ,
             con3_glucose, desired_var ,data_field1 ,  writer_variable,
            output_value_phen_variable )
    #elif desired_var == 'glucose':
    
        writer_variable.save()
        
    if desired_var == 'triglycerides':
        print(desired_var)
        stat_and_QCC(llq_tri, ulq_tri ,desired_var ,data_field1 , output_values_QC_variable , writer_variable, 
                replaced_missing, replaced_branching)
    
        Phenotype_1conditions( con1_tri, desired_var ,data_field1 ,  writer_variable,
            output_value_phen_variable)
    
        writer_variable.save()    
    
    if desired_var == 'cholesterol_1':
        print(desired_var)
        stat_and_QCC(llq_tot_chol, ulq_tot_chol ,desired_var ,data_field1 , output_values_QC_variable , writer_variable , 
                replaced_missing, replaced_branching  )
    
        Phenotype_1conditions( con1_tot_chol, desired_var ,data_field1 ,  writer_variable,
            output_value_phen_variable)
    
        writer_variable.save()     

    if desired_var == 'ldl':
        print(desired_var)
        stat_and_QCC(llq_ldl, ulq_ldl ,desired_var ,data_field1 , output_values_QC_variable , writer_variable , 
                replaced_missing, replaced_branching)
    
        Phenotype_1conditions(con1_tot_ldl, desired_var ,data_field1 ,  writer_variable ,
            output_value_phen_variable)
    
        writer_variable.save()
    
    if desired_var == 's_creatinine':
        print(desired_var)
        stat_and_QCC(llq_creatinine_s, ulq_creatinine_s ,desired_var ,data_field1 , output_values_QC_variable , writer_variable , 
                replaced_missing, replaced_branching)
        writer_variable.save()
  
    if desired_var == 'insulin':  
        print(desired_var)
        stat_and_QCC(llq_insulin, ulq_insulin ,desired_var ,data_field1 , output_values_QC_variable , writer_variable , 
                replaced_missing, replaced_branching)    
    
        writer_variable.save()

    if desired_var == 'albumin':
        print(desired_var)
        stat_and_QCC(llq_albumin, ulq_albumin ,desired_var ,data_field1 , output_values_QC_variable , writer_variable , 
                replaced_missing, replaced_branching)    
    
        writer_variable.save()
    
    if desired_var == 'ur_protein':
        print(desired_var)
        stat_and_QCC(llq_TotProtein, ulq_TotProtein ,desired_var ,data_field1 , output_values_QC_variable, writer_variable , 
                replaced_missing, replaced_branching  )
      
        writer_variable.save()
        
    if desired_var == 'ur_creatinine':
        print(desired_var)
        stat_and_QCC(llq_creatinine_u, ulq_creatinine_u ,desired_var ,data_field1 , output_values_QC_variable, writer_variable , 
                replaced_missing, replaced_branching  )
        
        writer_variable.save()  

    if desired_var == 'hdl':
        print(desired_var)
        stat_and_QCC(llq_hdl, ulq_hdl ,desired_var ,data_field1 , output_values_QC_variable , writer_variable , 
                replaced_missing, replaced_branching  )
    
        Phenotype_1condition_sex_2func(desired_var ,data_field1 ,writer_variable, output_value_phen_variable,con_m,con_f)
        
        writer_variable.save()
    
    if desired_var == 'acr':
        print(desired_var)
        Phenotype_3condition_sex_4func(  desired_var ,data_field1 ,writer_variable,
                                   output_value_phen_variable,con_m_1,con_m_2,con_f_1,con_f_2)
      
        writer_variable.save()
        
    if desired_var == 'visceral_fat':
        print(desired_var)
        stat_and_QC(desired_var, data_field1, output_values_QC_variable, 
                    writer_variable, below_spec, above_spec, replaced_missing,
                    replaced_branching, replaced_missing_bio, replaced_missing_bio_ex)
    
        Phenotype_1conditions(con1_vat, desired_var, data_field1,
                              writer_variable, output_value_phen_variable)
    
        writer_variable.save()
    
    if desired_var == 'subcutaneous_fat':
        print(desired_var)
        stat_and_QC(desired_var, data_field1, output_values_QC_variable, writer_variable, 
                below_spec, above_spec, replaced_missing, replaced_branching, 
                replaced_missing_bio, replaced_missing_bio_ex)
    
        Phenotype_1conditions(con1_sub, desired_var, data_field1, 
                              writer_variable, output_value_phen_variable)
    
        writer_variable.save()