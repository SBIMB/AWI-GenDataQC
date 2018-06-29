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
values = pd.ExcelWriter("values-QC.xls")
values_phen = pd.ExcelWriter("values-Phenotype.xls")

#open("values-Phenotype.csv", "w+").close()
#values_phen = open("values-Phenotype.csv", "a+")
#values_phen.truncate()


writer = pd.ExcelWriter("output.xls")
sites = list([0,0,0,0,0,0])
#data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/new.csv",low_memory=False)
data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/data/all_sites_v2.5.2.csv",low_memory=False)
glucose_all_sites =site_sorter(data_field1['site'], data_field1['glucose'],sites)
site_ids = site_sorter(data_field1['site'], data_field1['site_id'], sites)
study_ids = site_sorter(data_field1['site'], data_field1['study_id'], sites)
cohort_ids = site_sorter(data_field1['site'], data_field1['Cohort_ID_c'], sites)
site_numbers = site_sorter(data_field1['site'], data_field1['site'], sites)

#######
##Statistics table
minimum = min_per_site(glucose_all_sites,replaced_branching,replaced_missing)
maximum = max_per_site(glucose_all_sites,replaced_branching,replaced_missing)
mean =  mean_per_site(glucose_all_sites,replaced_branching,replaced_missing)
median = median_per_site (glucose_all_sites,replaced_branching,replaced_missing)
stand_dev = standard_dev_per_site(glucose_all_sites,replaced_branching,replaced_missing)
sites = getNum_sites(sites)


stat_table = pd.DataFrame({    'Minimum' : minimum,
                        'Maximum' : maximum,
                         'Mean' : mean,
                         'Median' : median,
                         'Standard Deviation' : stand_dev }, index=sites)



stat_table.to_excel(writer , sheet_name='Sheet1')



###########
###QC table
total = all_values(study_ids,glucose_all_sites,site_ids,values,cohort_ids,site_numbers)
null_num = null_capturing(study_ids,glucose_all_sites,site_ids,values,cohort_ids,site_numbers)
zero_nums = zero_capturing(study_ids,glucose_all_sites,site_ids,values,cohort_ids,site_numbers)
LLQ_inc_zero_num = LLQ_inc_zero_capturing(glucose_all_sites,llq_glucose,study_ids,site_ids,values,cohort_ids,site_numbers)
LLQ_exc_zero_num =LLQ_exc_zero_capturing(glucose_all_sites,llq_glucose,study_ids,site_ids,values,cohort_ids,site_numbers)
ULQ_num = ULQ_capturing(glucose_all_sites,ulq_glucose,study_ids,site_ids,values,cohort_ids,site_numbers)
replaced_missing_num = replaced_missing_capturing(glucose_all_sites,replaced_missing,study_ids,site_ids,values,cohort_ids,site_numbers)
branching_missing_num = replaced_branching_capturing(glucose_all_sites,replaced_branching,study_ids,site_ids,values,cohort_ids,site_numbers)

QC_table = pd.DataFrame({ 'Total Values ' : total ,
                        'Null Values ' : null_num,
                         'Zero Values ' : zero_nums,
                         'Values Below LLQ (inc 0) ' : LLQ_inc_zero_num,
                         'Values Below LLQ (exc 0)' :LLQ_exc_zero_num , 
                         'Values Above ULQ ': ULQ_num,
                         "Replaced True Missing Values ("+str(replaced_missing)+")": replaced_missing_num,
                         "Replaced Branching Missing Values ("+str(replaced_branching)+")": branching_missing_num,
                          }, index=sites)

QC_table.to_excel(writer , sheet_name='Sheet2')



##########
#Phenotype table

lower_limit = below_LLQ_to_con1(study_ids,glucose_all_sites,site_ids,values_phen
                                ,cohort_ids,site_numbers,llq_glucose, condition1)
above_initial_limit = above_con1_exc_zero(study_ids,glucose_all_sites,site_ids,values_phen
                               ,cohort_ids,site_numbers, condition1)
between_con1_to_con2 = con1_to_con2 (study_ids,glucose_all_sites,site_ids,values_phen
                               ,cohort_ids,site_numbers, condition1, condition2)
greater_than_7 = greater_than_con(study_ids,glucose_all_sites,site_ids,values_phen
                               ,cohort_ids,site_numbers, condition2)
greater_than_11 = greater_than_con(study_ids,glucose_all_sites,site_ids,values_phen
                                ,cohort_ids,site_numbers, condition3)

Phenotype_table = pd.DataFrame({ 'LLQ =< Values <= '+ str(condition1) : lower_limit ,
                            'Values <= '+ str(condition1) +" (exc 0) " : above_initial_limit,
                             str(condition1) + ' < Values < ' + str(condition2)  : between_con1_to_con2,
                             'Values >= ' + str(condition2): greater_than_7,
                             'Values >= ' + str(condition3) :greater_than_11 }, index=sites)
    

Phenotype_table.to_excel(writer , sheet_name='Sheet3')


writer.save()
#values.close()
values.save()
#values_phen.close()
values_phen.save()




