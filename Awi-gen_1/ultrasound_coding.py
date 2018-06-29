#Code to plot a box plot and histogram for the ultrasound variables subcutaneous fat and visceral fat



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seaB
from statistics import calculate_stats
from plotters import histogram_plotter
from plotters  import histo_shape_plotter
from plotters import box_plotter
from variable_Grouping import site_sorter
from variable_Grouping import sex_sorter
from variable_Grouping import box_plotter_var_site
from variable_Grouping import box_plotter_var_sex
from variable_Grouping import histo_shape_plotter_sites
from variable_Grouping import histo_shape_plotter_sex
from matplotlib.backends.backend_pdf import PdfPages
#Test Data.csv

data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/Data/all_sites_v2.5.2.csv")
standard_deviation_limit = 0.6
hist_bin_num = 10
col = 'darkblue'
#####
#Plaque is defined as a focal structure that encroaches into the arterial lumen of at least 0.5 mm or 50% of 
#the surrounding IMT value or demonstrates a thickness >1.5 mm as measured from the media-adventitia interface 
#to the intima-lumen interface.

#https://www.karger.com/Article/Abstract/97034
######



#Sex specific Subcutaneous Fat
[male_sub_fat,female_sub_fat]=sex_sorter(data_field1['sex'],data_field1['subcutaneous_fat'])
x_lab_sub_s = 'Subcutaneous Fat (cm)'
y_lab_sub_s = 'Number of People'
var_type_sub_s = 'Subcutaneous Fat Distribution '
histo_shape_plotter_sex(male_sub_fat,female_sub_fat,hist_bin_num,x_lab_sub_s,y_lab_sub_s,var_type_sub_s ,col)
[mean_sub_m,std_sub_m , median_sub_m,all_good_sub_m] = calculate_stats (male_sub_fat, 'subcutaneous_fat males', standard_deviation_limit)
[mean_sub_f,std_sub_f , median_sub_f,all_good_sub_f] = calculate_stats (female_sub_fat,'subcutaneous_fat females',standard_deviation_limit)


#Sex specific Visceral Fat
[male_vis_fat,female_vis_fat]=sex_sorter(data_field1['sex'],data_field1['visceral_fat'])
x_lab_vis_s = 'Visceral Fat (cm)'
y_lab_vis_s = 'Number of People'
var_type_vis_s = 'Visceral Fat Distribution'
histo_shape_plotter_sex(male_vis_fat,female_vis_fat,hist_bin_num,x_lab_vis_s,y_lab_vis_s,var_type_vis_s ,col)
[mean_vis_f,std_vis_f , median_vis_f,all_good_vis_f] = calculate_stats (female_vis_fat,'visceral_fat females',standard_deviation_limit)
[mean_vis_m,std_vis_m , median_vis_m,all_good_vis_m] = calculate_stats (male_vis_fat,'visceral_fat males',standard_deviation_limit)


#Total Data for Visceral Fat
[mean_vis_tot,std_vis_tot , median_vis_tot,all_good_vis_tot] = calculate_stats (data_field1['visceral_fat'],'visceral_fat total',standard_deviation_limit)
title = 'Total Visceral Fat Distribution'
x_lab = 'Visceral Fat (cm)'
y_lab = 'Number of People'
histo_shape_plotter(data_field1['visceral_fat'],hist_bin_num,title, x_lab , y_lab,col )

#Total Data for Subcutaneous Fat
[mean_sub_tot,std_sub_tot, median_sub_tot,all_good_sub_tot] = calculate_stats (data_field1['subcutaneous_fat'],'subcutaneous_fat total',standard_deviation_limit)
title = 'Total Subcutaneous Fat Distribution'
x_lab = 'Subcutaneous Fat (cm)'
y_lab = 'Number of People'
histo_shape_plotter(data_field1['subcutaneous_fat'],hist_bin_num,title, x_lab , y_lab,col )


# Site Based Visceral and Subcutaneous Fat Histograms
[site1_vis,site2_vis,site3_vis,site4_vis,site5_vis,site6_vis] =site_sorter(data_field1['site'], data_field1['visceral_fat'])
var_type_vis='Visceral Fat Distribution'
x_lab_vis = 'Visceral Fat (cm)'
y_lab_vis = 'Number of People'
histo_shape_plotter_sites(site1_vis,site2_vis,site3_vis,site4_vis,site5_vis,site6_vis ,hist_bin_num,x_lab_vis,y_lab_vis, var_type_vis,col )

[site1_sub,site2_sub,site3_sub,site4_sub,site5_sub,site6_sub] =site_sorter(data_field1['site'], data_field1['subcutaneous_fat'])
var_type_sub ='Subcutaneous Fat Distribution'
x_lab_sub = 'Subcutaneous Fat (cm)'
y_lab_sub = 'Number of People'
histo_shape_plotter_sites(site1_sub,site2_sub,site3_sub,site4_sub,site5_sub,site6_sub ,hist_bin_num,x_lab_sub,y_lab_sub, var_type_sub,col )


# Sex Based Visceral and Subcutaneous Fat Box plots
cdf = box_plotter_var_sex(male_sub_fat, female_sub_fat)                             
box_plotter(cdf, 'Sex','Sex','Number of People','Subcutaneous Fat- Sex Based Division')

cdf_2 = box_plotter_var_sex(male_vis_fat, female_vis_fat)                                
box_plotter(cdf_2, 'Sex','Sex','Number of People','Visceral Fat - Sex Based Division')

# Site Based Visceral and Subcutaneous Fat Box plots
cdf_3= box_plotter_var_site(site1_sub,site2_sub,site3_sub,site4_sub,site5_sub,site6_sub)
box_plotter(cdf_3, 'Site','Site','Number of People','Subcutaneous Fat - Site Based Division')      

cdf_4= box_plotter_var_site(site1_vis,site2_vis,site3_vis,site4_vis,site5_vis,site6_vis)
box_plotter(cdf_4, 'Site','Site','Number of People','Visceral Fat - Site Based Division')  