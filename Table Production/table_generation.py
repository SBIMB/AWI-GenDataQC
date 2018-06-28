import pandas as pd

from general import site_sorter
from general import getNum_sites
from stat_table import min_per_site
from stat_table import max_per_site
from stat_table import mean_per_site
from stat_table import median_per_site
from stat_table import standard_dev_per_site
from Phenotype_table import below_LLQ_to_con1
from Phenotype_table import above_con1_exc_zero
from Phenotype_table import con1_to_con2
from Phenotype_table import greater_than_con
from QC_table import zero_capturing
from QC_table import null_capturing
from QC_table import LLQ_inc_zero_capturing
from QC_table import LLQ_exc_zero_capturing
from QC_table import ULQ_capturing
from QC_table import replaced_missing_capturing
from QC_table import replaced_branching_capturing
from QC_table import all_values



def stat_and_QC(llq_val, ulq_val , desired_var ,data_field1 ,
             QC_filename , table_names, replaced_missing, replaced_branching):
    
    
    #Initializing values  
    
    
    values = pd.ExcelWriter(QC_filename )
    
    
    
    sites = list([0,0,0,0,0,0])
    
    variable_all_sites =site_sorter(data_field1['site'], data_field1[desired_var],sites)
    site_ids = site_sorter(data_field1['site'], data_field1['site_id'], sites)
    study_ids = site_sorter(data_field1['site'], data_field1['study_id'], sites)
    cohort_ids = site_sorter(data_field1['site'], data_field1['Cohort_ID_c'], sites)
    site_numbers = site_sorter(data_field1['site'], data_field1['site'], sites)
    
    #######
    ##Statistics table
    minimum = min_per_site(variable_all_sites,replaced_branching,replaced_missing)
    maximum = max_per_site(variable_all_sites,replaced_branching,replaced_missing)
    mean =  mean_per_site(variable_all_sites,replaced_branching,replaced_missing)
    median = median_per_site (variable_all_sites,replaced_branching,replaced_missing)
    stand_dev = standard_dev_per_site(variable_all_sites,replaced_branching,replaced_missing)
    sites = getNum_sites(sites)
    
    
    stat_table = pd.DataFrame({    'Minimum' : minimum,
                            'Maximum' : maximum,
                             'Mean' : mean,
                             'Median' : median,
                             'Standard Deviation' : stand_dev }, index=sites)
    
    stat_table.to_excel(table_names , sheet_name='Statistics')
    
    
    
    ###########
    ###QC table
    total = all_values(study_ids,variable_all_sites,site_ids,values,cohort_ids,site_numbers)
    null_num = null_capturing(study_ids,variable_all_sites,site_ids,values,cohort_ids,site_numbers)
    zero_nums = zero_capturing(study_ids,variable_all_sites,site_ids,values,cohort_ids,site_numbers)
    LLQ_inc_zero_num = LLQ_inc_zero_capturing(variable_all_sites,llq_val,study_ids,site_ids,values,cohort_ids,site_numbers)
    LLQ_exc_zero_num =LLQ_exc_zero_capturing(variable_all_sites,llq_val,study_ids,site_ids,values,cohort_ids,site_numbers)
    ULQ_num = ULQ_capturing(variable_all_sites, ulq_val,study_ids,site_ids,values,cohort_ids,site_numbers)
    replaced_missing_num = replaced_missing_capturing(variable_all_sites,replaced_missing,study_ids,site_ids,values,cohort_ids,site_numbers)
    branching_missing_num = replaced_branching_capturing(variable_all_sites,replaced_branching,study_ids,site_ids,values,cohort_ids,site_numbers)
    
    QC_table = pd.DataFrame({ 'Total Values ' : total ,
                        'Null Values ' : null_num,
                         'Zero Values ' : zero_nums,
                         'Values Below LLQ (inc 0) ' : LLQ_inc_zero_num,
                         'Values Below LLQ (exc 0)' :LLQ_exc_zero_num , 
                         'Values Above ULQ ': ULQ_num,
                         "Replaced True Missing Values ("+str(replaced_missing)+")": replaced_missing_num,
                         "Replaced Branching Missing Values ("+str(replaced_branching)+")": branching_missing_num,
                          }, index=sites)
    
    QC_table.to_excel(table_names, sheet_name='QC')
   
    values.save()
    
    
def Phenotype_5conditions(llq_val,  condition1 ,  condition2 , condition3 , desired_var ,data_field1 ,
              table_names,Phen_filename): 
    
    values_phen = pd.ExcelWriter(Phen_filename)
    
    sites = list([0,0,0,0,0,0])
    variable_all_sites =site_sorter(data_field1['site'], data_field1[desired_var],sites)
    site_ids = site_sorter(data_field1['site'], data_field1['site_id'], sites)
    study_ids = site_sorter(data_field1['site'], data_field1['study_id'], sites)
    cohort_ids = site_sorter(data_field1['site'], data_field1['Cohort_ID_c'], sites)
    site_numbers = site_sorter(data_field1['site'], data_field1['site'], sites)
    sites = getNum_sites(sites)
    
    
    ##########
    #Phenotype table
    
    lower_limit = below_LLQ_to_con1(study_ids,variable_all_sites,site_ids,values_phen
                                ,cohort_ids,site_numbers,llq_val, condition1)
    above_initial_limit = above_con1_exc_zero(study_ids,variable_all_sites,site_ids,values_phen
                                ,cohort_ids,site_numbers, condition1)
    between_con1_to_con2 = con1_to_con2 (study_ids,variable_all_sites,site_ids,values_phen
                                ,cohort_ids,site_numbers, condition1, condition2)
    greater_than_7 = greater_than_con(study_ids,variable_all_sites,site_ids,values_phen
                                ,cohort_ids,site_numbers, condition2)
    greater_than_11 = greater_than_con(study_ids,variable_all_sites,site_ids,values_phen
                                ,cohort_ids,site_numbers, condition3)
    
    Phenotype_table = pd.DataFrame({ 'LLQ =< Values <= '+ str(condition1) : lower_limit ,
                            'Values <='+ str(condition1) +" (exc 0) " : above_initial_limit,
                             str(condition1) + ' < Values < ' + str(condition2)  : between_con1_to_con2,
                             'Values >= ' + str(condition2): greater_than_7,
                             'Values >= ' + str(condition3) :greater_than_11 }, index=sites)
    
    
    Phenotype_table.to_excel(table_names , sheet_name='Phenotype')
    values_phen.save()
    
def Phenotype_1conditions( condition1  , desired_var ,data_field1 ,table_names, Phen_filename): 
    
    values_phen = pd.ExcelWriter(Phen_filename)
    
    sites = list([0,0,0,0,0,0])
    variable_all_sites =site_sorter(data_field1['site'], data_field1[desired_var],sites)
    site_ids = site_sorter(data_field1['site'], data_field1['site_id'], sites)
    study_ids = site_sorter(data_field1['site'], data_field1['study_id'], sites)
    cohort_ids = site_sorter(data_field1['site'], data_field1['Cohort_ID_c'], sites)
    site_numbers = site_sorter(data_field1['site'], data_field1['site'], sites)
    sites = getNum_sites(sites)
    
    
    ##########
    #Phenotype table
    
    greater_than_condition1  = greater_than_con(study_ids,variable_all_sites,site_ids,values_phen
                                ,cohort_ids,site_numbers, condition1)
    
    Phenotype_table = pd.DataFrame({ 'Values >= ' + str(condition1) :greater_than_condition1 }, index=sites)
    
    
    Phenotype_table.to_excel(table_names , sheet_name='Phenotype')
    values_phen.save()
    
    
    
    
    
    
