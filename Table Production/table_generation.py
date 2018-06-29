#Functions utilised to build the specific QC, statistics and phenotype tables for each specific biomarker 


import pandas as pd

from general import site_sorter
from general import getNum_sites
from general import site_and_sex_sorter
from general import siteCompare
from stat_table import min_per_site
from stat_table import max_per_site
from stat_table import mean_per_site
from stat_table import median_per_site
from stat_table import standard_dev_per_site
from Phenotype_table import below_LLQ_to_con1
from Phenotype_table import above_con1_exc_zero
from Phenotype_table import con1_to_con2
from Phenotype_table import greater_than_con
from Phenotype_table import below_con1_exc_zero_sex
from Phenotype_table import below_con1_inc_zero_sex
from Phenotype_table import greater_than_con_sex
from Phenotype_table import con1_to_con2_sex
from Phenotype_table import not_con1_exc_zero_sex
from Phenotype_table import not_con1_inc_zero_sex
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
    '''Function to create a statistics and QC table in seperate tabs of an excel spreadsheet. '''
    
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
    '''Function to create a phenotype table in a seperate tab of an excel spreadsheet. Creates a table with 5 different 
    conditions. '''
    
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
    '''Function to create a phenotype table in a seperate tab of an excel spreadsheet. Creates a table with 1 
    conditions. '''
    
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
    
def Phenotype_1condition_sex_2func(  desired_var ,data_field1 ,table_names, Phen_filename,con_m,con_f): 
    '''Function to create a phenotype table in a seperate tab of an excel spreadsheet. Creates a table with 2 
    conditions. Takes sex into consideration. '''
    
    values_phen = pd.ExcelWriter(Phen_filename)
    
    sites_m = list([0,0,0,0,0,0])
    sites_f = list([0,0,0,0,0,0])
    

    
    [var_f,var_m] = site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1[desired_var],data_field1['sex'])
    [site_ids_f, site_ids_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['site_id'],data_field1['sex'])
    [study_ids_f, study_ids_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['study_id'],data_field1['sex'])
    [cohort_ids_f, cohort_ids_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['Cohort_ID_c'],data_field1['sex'])
    [site_nums_f, site_nums_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['site'],data_field1['sex'])
    sites_true = siteCompare(sites_m,sites_f)
  

    
    ##########
    #Phenotype table
    inc_zero_males = below_con1_inc_zero_sex(study_ids_m,var_m,site_ids_m,values_phen,cohort_ids_m,site_nums_m, con_m,'Male')
    exc_zero_males = below_con1_exc_zero_sex(study_ids_m,var_m,site_ids_m,values_phen,cohort_ids_m,site_nums_m, con_m,'Male')
    inc_zero_females = below_con1_inc_zero_sex(study_ids_f,var_f,site_ids_f,values_phen,cohort_ids_f,site_nums_f, con_f,'Female')
    exc_zero_females = below_con1_exc_zero_sex(study_ids_f,var_f,site_ids_f,values_phen,cohort_ids_f,site_nums_f, con_f,'Female')
    
    
    
    Phenotype_table = pd.DataFrame({ '0 < Male Values <= '+ str(con_m)   : exc_zero_males,
                                '0 =< Male Values <= '+ str(con_m) : inc_zero_males ,
                             '0 < Female Values <= '+ str(con_f): exc_zero_females,
                             '0 =< Female Values <= '+ str(con_f) : inc_zero_females}, index = sites_true)
    
    
    Phenotype_table.to_excel(table_names , sheet_name='Phenotype')
    values_phen.save()
    
def Phenotype_3condition_sex_4func(  desired_var ,data_field1 ,table_names, Phen_filename,con_m_1,con_m_2,con_f_1 ,con_f_2): 
    '''Function to create a phenotype table in a seperate tab of an excel spreadsheet. Creates a table with 4 
    conditions. Takes sex into consideration. '''
    
    values_phen = pd.ExcelWriter(Phen_filename)
    
    sites_m = list([0,0,0,0,0,0])
    sites_f = list([0,0,0,0,0,0])

    
    [var_f,var_m] = site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1[desired_var],data_field1['sex'])
    [site_ids_f, site_ids_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['site_id'],data_field1['sex'])
    [study_ids_f, study_ids_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['study_id'],data_field1['sex'])
    [cohort_ids_f, cohort_ids_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['Cohort_ID_c'],data_field1['sex'])
    [site_nums_f, site_nums_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['site'],data_field1['sex'])
    sites_true = siteCompare(sites_m,sites_f)
  
    ##########
    #Phenotype table
    inc_zero_males = not_con1_inc_zero_sex(study_ids_m,var_m,site_ids_m,values_phen,cohort_ids_m,site_nums_m, con_m_1,'Male')
    exc_zero_males = not_con1_exc_zero_sex(study_ids_m,var_m,site_ids_m,values_phen,cohort_ids_m,site_nums_m, con_m_1,'Male')
    con1_to_con2_males = con1_to_con2_sex(study_ids_m,var_m,site_ids_m,values_phen,cohort_ids_m,site_nums_m, con_m_1,con_m_2,'Male')
    greater_than_males = greater_than_con_sex(study_ids_m,var_m,site_ids_m,values_phen,cohort_ids_m,site_nums_m, con_m_2,'Male')
    
    inc_zero_females = not_con1_inc_zero_sex(study_ids_f,var_f,site_ids_f,values_phen,cohort_ids_f,site_nums_f, con_f_1,'Female')
    exc_zero_females = not_con1_exc_zero_sex(study_ids_f,var_f,site_ids_f,values_phen,cohort_ids_f,site_nums_f, con_f_1,'Female')
    con1_to_con2_females = con1_to_con2_sex(study_ids_f,var_f,site_ids_f,values_phen,cohort_ids_f,site_nums_f, con_f_1,con_f_2,'Female')
    greater_than_females = greater_than_con_sex(study_ids_f,var_f,site_ids_f,values_phen,cohort_ids_f,site_nums_f, con_f_1,'Female')
    
    
    Phenotype_table = pd.DataFrame({ '0 <= Male Values < '+ str(con_m_1)   : inc_zero_males,
                                '0 < Male Values < '+ str(con_m_1) : exc_zero_males ,
                                str(con_m_1)+ '<= Male Values <= '+ str(con_m_2) : con1_to_con2_males ,
                                str(con_m_2) + '< Male Values ' : greater_than_males ,
                              '0 <= Female Values <= '+ str(con_f_1)  : inc_zero_females,
                             '0 < Female Values < '+ str(con_f_1) : exc_zero_females,
                             str(con_f_1)+ '<= Female Values <= '+ str(con_f_2) : con1_to_con2_females ,
                              str(con_f_2) + '< Female Values ' : greater_than_females }, index = sites_true)
    
    
    Phenotype_table.to_excel(table_names , sheet_name='Phenotype')
    values_phen.save()
    
    
    
    
    

