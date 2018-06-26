import pandas as pd

from table_generation import skeleton

lld_glucose = 0.36
uld_glucose = 35
con1_glucose = 5.6
con2_glucose = 7.0
con3_glucose = 11.1
desired_var = 'glucose'
file_name = "values_new.txt"
table_name = "output_new.xls"

data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/new.csv",low_memory=False)
#data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/data/all_sites_v2.5.2.csv",low_memory=False)

skeleton(lld_glucose, uld_glucose, con1_glucose, con2_glucose ,
         con3_glucose, desired_var ,data_field1 , file_name , table_name )
    