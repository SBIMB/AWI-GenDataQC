# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:26:22 2018

@author: Freedom Mukomana
"""
import pandas as pd
import datetime

#Set up global variables 
#replaced missing and replaced branching must be negative values
below_spec = -111
above_spec = -222
replaced_missing = -999
replaced_missing_bio = -998
replaced_missing_bio_ex = -997
replaced_branching = -555

directory_for_input = "C:/Users/A0035863/Documents/SBIMB/AWI-Gen/Sites/ALL/QC/AWI-GenDataQC/Awi-gen_1/Data/"
input_filename = "all_sites_v2.5.3.6.csv"
directory_for_output = "C:/Users/A0035863/Documents/SBIMB/AWI-Gen/Sites/ALL/QC/AWI-GenDataQC/QC_table/"
present_datetime = datetime.datetime.now()
date_time_var = present_datetime.strftime("%d-%m-%Y_%H-%M")

input_file = directory_for_input + input_filename 
data_field1 = pd.read_csv(input_file,low_memory=False)