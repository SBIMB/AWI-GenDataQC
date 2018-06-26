
import pandas as pd
import numpy as num

from general import site_sorter
from general import getNum_sites
from stat_table import min_per_site
from stat_table import max_per_site
from stat_table import mean_per_site
from stat_table import median_per_site
from stat_table import standard_dev_per_site
from Phenotype_table import below_LLD_to_con1
from Phenotype_table import above_con1_exc_zero
from Phenotype_table import con1_to_con2
from Phenotype_table import greater_than_con
from QC_table import zero_capturing
from QC_table import null_capturing
from QC_table import LLD_inc_zero_capturing
from QC_table import LLD_exc_zero_capturing
from QC_table import ULD_capturing
from QC_table import tot_values



lld_glucose = 0.36
uld_glucose = 35
condition1 = 5.6
condition2 = 7.0
condition3 = 11.1

values = open("values.txt", "w+")
values.truncate
writer = pd.ExcelWriter("output.xls")
sites = list([0,0,0,0,0,0])
data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/new.csv",low_memory=False)
#data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/data/all_sites_v2.5.2.csv",low_memory=False)
glucose_all_sites =site_sorter(data_field1['site'], data_field1['glucose'],sites)
site_ids = site_sorter(data_field1['site'], data_field1['site_id'], sites)
study_ids = site_sorter(data_field1['site'], data_field1['study_id'], sites)
cohort_ids = site_sorter(data_field1['site'], data_field1['Cohort_ID_c'], sites)

#study = studyID_of_zero(study_ids,glucose_all_sites)
#zeros_val = zero_number(glucose_all_sites)
#zero_val2 = siteID_of_zero(site_ids,glucose_all_sites)
#print(study)
#print(zeros_val)
#print(zero_val2 )


#######
##Statistics table
minimum = min_per_site(glucose_all_sites)
maximum = max_per_site(glucose_all_sites)
mean =  mean_per_site(glucose_all_sites)
median = median_per_site (glucose_all_sites)
stand_dev = standard_dev_per_site(glucose_all_sites)
sites = getNum_sites(sites)


stat_table = pd.DataFrame({    'Minimum' : minimum,
                        'Maximum' : maximum,
                         'Mean' : mean,
                         'Median' : median,
                         'Standard Deviation' : stand_dev }, index=sites)

print(stat_table)
stat_table.to_excel(writer , sheet_name='Sheet1')



###########
###QC table
total = tot_values(glucose_all_sites)
null_num = null_capturing(study_ids,glucose_all_sites,site_ids,values,cohort_ids)
zero_nums = zero_capturing(study_ids,glucose_all_sites,site_ids,values,cohort_ids)
LLD_inc_zero_num = LLD_inc_zero_capturing(glucose_all_sites,lld_glucose,study_ids,site_ids,values,cohort_ids)
LLD_exc_zero_num =LLD_exc_zero_capturing(glucose_all_sites,lld_glucose,study_ids,site_ids,values,cohort_ids)
ULD_num = ULD_capturing(glucose_all_sites,uld_glucose,study_ids,site_ids,values,cohort_ids)


QC_table = pd.DataFrame({ 'Total Values ' : total ,
                        'Null Values ' : null_num,
                         'Zero Values ' : zero_nums,
                         'Values Below LLD (inc 0) ' : LLD_inc_zero_num,
                         'Values Below LLD (exc 0)' :LLD_exc_zero_num , 
                         'Values Above ULD ': ULD_num}, index=sites)

print(QC_table)
QC_table.to_excel(writer , sheet_name='Sheet2')



##########
#Phenotype table

lower_limit = below_LLD_to_con1(glucose_all_sites,lld_glucose,condition1)
above_initial_limit = above_con1_exc_zero(glucose_all_sites,condition1)
between_con1_to_con2 = con1_to_con2 (glucose_all_sites,condition1,condition2)
greater_than_7 = greater_than_con(glucose_all_sites,condition2)
greater_than_11 = greater_than_con(glucose_all_sites,condition3)

Phenotype_table = pd.DataFrame({ 'LLD =< Values < 5.6' : lower_limit ,
                        'Values < 5.6 (exc 0) ' : above_initial_limit,
                         '5.6 < Values < 7.0 ' : between_con1_to_con2,
                         'Values >= 7.0' : greater_than_7,
                         'Values >= 11.1' :greater_than_11 }, index=sites)

print(Phenotype_table)
Phenotype_table.to_excel(writer , sheet_name='Sheet3')
writer.save()



values.close()




