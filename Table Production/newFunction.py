#Original code for checking whether the site_and_sex_sorter function needed for the hdl and acr biomarkers was 
#functioning optimally. The hdl variable was investigated via modifications made to the fasting_glucose.py code



from functionTester import site_and_sex_sorter
from functionTester import siteCompare


import pandas as pd




from general import site_sorter
from general import getNum_sites
from stat_table import min_per_site
from stat_table import max_per_site
from stat_table import mean_per_site
from stat_table import median_per_site
from stat_table import standard_dev_per_site


from Phenotype_table import below_con1_exc_zero_sex
from Phenotype_table import below_con1_inc_zero_sex


from QC_table import zero_capturing
from QC_table import null_capturing
from QC_table import LLQ_inc_zero_capturing
from QC_table import LLQ_exc_zero_capturing
from QC_table import ULQ_capturing
from QC_table import replaced_missing_capturing
from QC_table import replaced_branching_capturing
from QC_table import all_values

llq_glucose = 0.36
ulq_glucose = 35
condition1 = 5.60
condition2 = 7.0
condition3 = 11.1

replaced_missing = -999
replaced_branching = -555

#Initializing values 
#open("values-QC.xls", "w+").close()
#values = open("values-QC.xls", "a+")
#values.truncate()
#values = pd.ExcelWriter("values-QC.xls")
values_phen = pd.ExcelWriter("values-Phenotype.xls")

#open("values-Phenotype.csv", "w+").close()
#values_phen = open("values-Phenotype.csv", "a+")
#values_phen.truncate()


writer = pd.ExcelWriter("output.xls")

sites_m = list([0,0,0,0,0,0])
sites_f = list([0,0,0,0,0,0])

#data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/new.csv",low_memory=False)
data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/data/all_sites_v2.5.2.csv",low_memory=False)
#glucose_all_sites =site_sorter(data_field1['site'], data_field1['glucose'],sites)
#site_ids = site_sorter(data_field1['site'], data_field1['site_id'], sites)
#study_ids = site_sorter(data_field1['site'], data_field1['study_id'], sites)
#cohort_ids = site_sorter(data_field1['site'], data_field1['Cohort_ID_c'], sites)
#site_numbers = site_sorter(data_field1['site'], data_field1['site'], sites)


[HDL_f,HDL_m] = site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['hdl'],data_field1['sex'])
[site_ids_f, site_ids_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['site_id'],data_field1['sex'])
[study_ids_f, study_ids_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['study_id'],data_field1['sex'])
[cohort_ids_f, cohort_ids_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['Cohort_ID_c'],data_field1['sex'])
[site_nums_f, site_nums_m]=site_and_sex_sorter(data_field1['site'],sites_m,sites_f, data_field1['site'],data_field1['sex'])
sites_true = siteCompare(sites_m,sites_f)
#print(sites_m)
#print(HDL_f)

#print(HDL_m)

########
###Statistics table
#minimum = min_per_site(glucose_all_sites,replaced_branching,replaced_missing)
#maximum = max_per_site(glucose_all_sites,replaced_branching,replaced_missing)
#mean =  mean_per_site(glucose_all_sites,replaced_branching,replaced_missing)
#median = median_per_site (glucose_all_sites,replaced_branching,replaced_missing)
#stand_dev = standard_dev_per_site(glucose_all_sites,replaced_branching,replaced_missing)
#sites = getNum_sites(sites)
#
#
#stat_table = pd.DataFrame({    'Minimum' : minimum,
#                        'Maximum' : maximum,
#                         'Mean' : mean,
#                         'Median' : median,
#                         'Standard Deviation' : stand_dev }, index=sites)
#
#
#
#stat_table.to_excel(writer , sheet_name='Sheet1')
#
#
#
############
####QC table
#total = all_values(study_ids,glucose_all_sites,site_ids,values,cohort_ids,site_numbers)
#null_num = null_capturing(study_ids,glucose_all_sites,site_ids,values,cohort_ids,site_numbers)
#zero_nums = zero_capturing(study_ids,glucose_all_sites,site_ids,values,cohort_ids,site_numbers)
#LLQ_inc_zero_num = LLQ_inc_zero_capturing(glucose_all_sites,llq_glucose,study_ids,site_ids,values,cohort_ids,site_numbers)
#LLQ_exc_zero_num =LLQ_exc_zero_capturing(glucose_all_sites,llq_glucose,study_ids,site_ids,values,cohort_ids,site_numbers)
#ULQ_num = ULQ_capturing(glucose_all_sites,ulq_glucose,study_ids,site_ids,values,cohort_ids,site_numbers)
#replaced_missing_num = replaced_missing_capturing(glucose_all_sites,replaced_missing,study_ids,site_ids,values,cohort_ids,site_numbers)
#branching_missing_num = replaced_branching_capturing(glucose_all_sites,replaced_branching,study_ids,site_ids,values,cohort_ids,site_numbers)
#
#QC_table = pd.DataFrame({ 'Total Values ' : total ,
#                        'Null Values ' : null_num,
#                         'Zero Values ' : zero_nums,
#                         'Values Below LLQ (inc 0) ' : LLQ_inc_zero_num,
#                         'Values Below LLQ (exc 0)' :LLQ_exc_zero_num , 
#                         'Values Above ULQ ': ULQ_num,
#                         "Replaced True Missing Values ("+str(replaced_missing)+")": replaced_missing_num,
#                         "Replaced Branching Missing Values ("+str(replaced_branching)+")": branching_missing_num,
#                          }, index=sites)
#
#QC_table.to_excel(writer , sheet_name='Sheet2')



##########
#Phenotype table
con_m=1.0
con_f =1.3

inc_zero_males = below_con1_inc_zero_sex(study_ids_m,HDL_m,site_ids_m,values_phen,cohort_ids_m,site_nums_m, con_m,'Male')
#print(inc_zero_males)
exc_zero_males = below_con1_exc_zero_sex(study_ids_m,HDL_m,site_ids_m,values_phen,cohort_ids_m,site_nums_m, con_m,'Male')
inc_zero_females = below_con1_inc_zero_sex(study_ids_f,HDL_f,site_ids_f,values_phen,cohort_ids_f,site_nums_f, con_f,'Female')
exc_zero_females = below_con1_exc_zero_sex(study_ids_f,HDL_f,site_ids_f,values_phen,cohort_ids_f,site_nums_f, con_f,'Female')
#print(inc_zero_females)

#lower_limit = below_LLQ_to_con1(study_ids,glucose_all_sites,site_ids,values_phen
#                                ,cohort_ids,site_numbers,llq_glucose, condition1)
#above_initial_limit = above_con1_exc_zero(study_ids,glucose_all_sites,site_ids,values_phen
#                               ,cohort_ids,site_numbers, condition1)
#between_con1_to_con2 = con1_to_con2 (study_ids,glucose_all_sites,site_ids,values_phen
#                               ,cohort_ids,site_numbers, condition1, condition2)
#greater_than_7 = greater_than_con(study_ids,glucose_all_sites,site_ids,values_phen
#                               ,cohort_ids,site_numbers, condition2)
#greater_than_11 = greater_than_con(study_ids,glucose_all_sites,site_ids,values_phen
#                                ,cohort_ids,site_numbers, condition3)
#
Phenotype_table = pd.DataFrame({ '0 < Male Values <= '+ str(con_m)   : exc_zero_males,
                                '0 =< Male Values <= '+ str(con_m) : inc_zero_males ,
                             '0 < Female Values <= '+ str(con_f): exc_zero_females,
                             '0 =< Female Values <= '+ str(con_f) : inc_zero_females},index = sites_true)
#                             'Values >= ' + str(condition3) :greater_than_11 }, index=sites)
#    
#
Phenotype_table.to_excel(writer , sheet_name='Sheet1')
#
#
writer.save()
##values.close()
#values.save()
##values_phen.close()
values_phen.save()