
import pandas as pd
import numpy as num

from stat_table import site_sorter
from stat_table import min_per_site
from stat_table import max_per_site
from stat_table import mean_per_site
from stat_table import median_per_site
from stat_table import standard_dev_per_site
from QC_table import tot_values
from stat_table import getNum_sites
from QC_table import null_number
from QC_table import zero_number
from QC_table import LLD_inc_zero
from QC_table import LLD_exc_zero
from QC_table import ULD
f#rom Phenotype_table import below_LLD_to_con1

lld_glucose = 0.36
uld_glucose = 35
condition1 = 5.6

writer = pd.ExcelWriter("output.xls")
sites = list([0,0,0,0,0,0])
#data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/new.csv",low_memory=False)
#glucose_all_sites =site_sorter(data_field1['site'], data_field1['glucose'],sites)

data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/all_sites_v2.5.2.csv",low_memory=False)
glucose_all_sites =site_sorter(data_field1['site'], data_field1['glucose'],sites)



######
#Statistics table
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




##########
#QC table

total = tot_values(glucose_all_sites)
null_num = null_number(glucose_all_sites)
zero_nums = zero_number(glucose_all_sites)
LLD_inc_zero_num = LLD_inc_zero(glucose_all_sites,lld_glucose)
LLD_exc_zero_num = LLD_exc_zero(glucose_all_sites,lld_glucose)
ULD_num =ULD(glucose_all_sites,uld_glucose)


QC_table = pd.DataFrame({ 'Total Values ' : total ,
                        'Null Values ' : null_num,
                         'Zero Values ' : zero_nums,
                         'Values Below LLD (inc 0) ' : LLD_inc_zero_num,
                         'Values Below LLD (exc 0)' :LLD_exc_zero_num , 
                         'Values Above ULD ': ULD_num}, index=sites)

print(QC_table)
QC_table.to_excel(writer , sheet_name='Sheet2')
writer.save()


##########
#Phenotype table

#lower_limit = below_LLD_to_con1(glucose_all_sites,lld_glucose,condition1)
#print(lower_limit)













