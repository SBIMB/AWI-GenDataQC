import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seaB
#from statistics import calculate_stats
#from plotters import histogram_plotter
#from plotters  import histo_shape_plotter
from plotters import *
from variable_Grouping import site_sorter
from variable_Grouping import sex_sorter
from variable_Grouping import box_plotter_var_site
from variable_Grouping import box_plotter_var_sex
from variable_Grouping import histo_shape_plotter_sites
from variable_Grouping import histo_shape_plotter_sex


data_field1 = pd.read_csv("Data/all_sites_v2.5.2.csv")
col = 'darkblue'
hist_bin_num = 10

#Site based LDL and HDL representations
#HDL representations
[site1_hdl,site2_hdl,site3_hdl,site4_hdl,site5_hdl,site6_hdl] =site_sorter(data_field1['site'], data_field1['hdl'])
hdl_data_site = box_plotter_var_site(site1_hdl,site2_hdl,site3_hdl,site4_hdl,site5_hdl,site6_hdl)
box_plotter(hdl_data_site, 'Site','Site','Number of People','HDL - Site Based Division')
var_type_hdl='HDL Distribution'
x_lab_hdl = 'HDL Result'
y_lab_hdl = 'Number of People'
histo_shape_plotter_sites(site1_hdl,site2_hdl,site3_hdl,site4_hdl,site5_hdl,site6_hdl,hist_bin_num,x_lab_hdl,y_lab_hdl, var_type_hdl,col )

#LDL representations
[site1_ldl,site2_ldl,site3_ldl,site4_ldl,site5_ldl,site6_ldl] =site_sorter(data_field1['site'], data_field1['ldl'])
ldl_data_site = box_plotter_var_site(site1_ldl,site2_ldl,site3_ldl,site4_ldl,site5_ldl,site6_ldl)
box_plotter(ldl_data_site, 'Site','Site','Number of People','LDL - Site Based Division') 
var_type_ldl='LDL Distribution'
x_lab_ldl = 'LDL Result'
y_lab_ldl = 'Number of People'
histo_shape_plotter_sites(site1_ldl,site2_ldl,site3_ldl,site4_ldl,site5_ldl,site6_ldl,hist_bin_num,x_lab_ldl,y_lab_ldl, var_type_ldl,col )


#Combined representation for HDL and LDL per site
legend_hdl ='HDL'
legend_ldl = 'LDL'
title_hdl_ldl ='HDL and LDL Comparisons'
x_lab_hdl_ldl= 'Level of Biomarker Recorded'
y_lab_hdl_ldl ='Frequency'
HDL_site = [site1_hdl,site2_hdl,site3_hdl,site4_hdl,site5_hdl,site6_hdl]
LDL_site = [site1_ldl,site2_ldl,site3_ldl,site4_ldl,site5_ldl,site6_ldl]
histogram_plotter_var2_site(HDL_site,LDL_site,legend_hdl,legend_ldl,  hist_bin_num , title_hdl_ldl, x_lab_hdl_ldl , y_lab_hdl_ldl)


#Sex based LDL and HDL representations
#HDL representations
[male_hdl,female_hdl]=sex_sorter(data_field1['sex'],data_field1['hdl'])
hdl_data_sex = box_plotter_var_sex(male_hdl,female_hdl)
box_plotter(hdl_data_sex, 'Sex','Sex','Number of People','HDL - Sex Based Division')
x_lab_hdl_s = 'HDL Distribution'
y_lab_hdl_s = 'Number of People'
var_type_hdl_s = 'HDL Distribution'
histo_shape_plotter_sex(male_hdl,female_hdl,hist_bin_num,x_lab_hdl_s,y_lab_hdl_s,var_type_hdl_s ,col)

#LDL representations
[male_ldl,female_ldl]=sex_sorter(data_field1['sex'],data_field1['ldl'])
ldl_data_sex = box_plotter_var_sex(male_ldl,female_ldl)
box_plotter(ldl_data_sex, 'Sex','Sex','Number of People','LDL - Sex Based Division')
x_lab_ldl_s = 'LDL Distribution'
y_lab_ldl_s = 'Number of People'
var_type_ldl_s = 'LDL Distribution'
histo_shape_plotter_sex(male_ldl,female_ldl,hist_bin_num,x_lab_ldl_s,y_lab_ldl_s,var_type_ldl_s ,col)

legend_hdl_s ='HDL'
legend_ldl_s = 'LDL'
title_hdl_ldl_s='HDL and LDL Comparisons'
x_lab_hdl_ldl_s= 'Level of Biomarker Recorded'
y_lab_hdl_ldl_s='Frequency'
HDL_sex = [male_hdl,female_hdl]
LDL_sex = [male_ldl,female_ldl]
histogram_plotter_var2_sex(HDL_sex,LDL_sex,legend_hdl_s,legend_ldl_s,  hist_bin_num , title_hdl_ldl_s, x_lab_hdl_ldl_s , y_lab_hdl_ldl_s)

#Site based Cholesterol and Triglycerides representations
#Cholesterol representations
[site1_chol,site2_chol,site3_chol,site4_chol,site5_chol,site6_chol] =site_sorter(data_field1['site'], data_field1['cholesterol_1'])
chol_data_site = box_plotter_var_site(site1_chol,site2_chol,site3_chol,site4_chol,site5_chol,site6_chol)
box_plotter(chol_data_site, 'Site','Site','Number of People','Cholesterol - Site Based Division')
var_type_chol='Cholesterol Distribution'
x_lab_chol = 'Cholesterol Result'
y_lab_chol = 'Number of People'
histo_shape_plotter_sites(site1_chol,site2_chol,site3_chol,site4_chol,site5_chol,site6_chol,hist_bin_num,x_lab_chol,y_lab_chol, var_type_chol,col )


#Triglycerides representations
[site1_tri,site2_tri,site3_tri,site4_tri,site5_tri,site6_tri] =site_sorter(data_field1['site'], data_field1['triglycerides'])
tri_data_site = box_plotter_var_site(site1_tri,site2_tri,site3_tri,site4_tri,site5_tri,site6_tri)
box_plotter(tri_data_site , 'Site','Site','Number of People','Cholesterol - Site Based Division')
var_type_tri='Triglyceride Distribution'
x_lab_tri = 'Triglyceride Result'
y_lab_tri = 'Number of People'
histo_shape_plotter_sites(site1_tri,site2_tri,site3_tri,site4_tri,site5_tri,site6_tri,hist_bin_num,x_lab_tri,y_lab_tri, var_type_tri,col )


#Sex based Cholesterol and Triglycerides representations
#Cholesterol representations
[male_chol,female_chol]=sex_sorter(data_field1['sex'],data_field1['cholesterol_1'])
chol_data_sex = box_plotter_var_sex(male_chol,female_chol)
box_plotter(chol_data_sex , 'Sex','Sex','Number of People','Cholesterol - Sex Based Division')
x_lab_chol_s = 'Cholesterol Distribution'
y_lab_chol_s = 'Number of People'
var_type_chol_s = 'Cholesterol Distribution'
histo_shape_plotter_sex(male_chol,female_chol,hist_bin_num,x_lab_chol_s,y_lab_chol_s,var_type_chol_s ,col)

#Triglycerides representations
[male_tri,female_tri]=sex_sorter(data_field1['sex'],data_field1['triglycerides'])
tri_data_sex = box_plotter_var_sex(male_tri,female_tri)
box_plotter(chol_data_sex , 'Sex','Sex','Number of People',' Triglycerides- Sex Based Division')
x_lab_tri_s = 'Triglyceride Distribution'
y_lab_tri_s = 'Number of People'
var_type_tri_s = 'Triglyceride Distribution'
histo_shape_plotter_sex(male_tri,female_tri,hist_bin_num,x_lab_tri_s,y_lab_tri_s,var_type_tri_s ,col)


#Site based representation for Creatinine and Insulin 
#Creatinine 
[site1_cret,site2_cret,site3_cret,site4_cret,site5_cret,site6_cret] =site_sorter(data_field1['site'], data_field1['s_creatinine'])
cret_data_site = box_plotter_var_site(site1_cret,site2_cret,site3_cret,site4_cret,site5_cret,site6_cret)
box_plotter(cret_data_site , 'Site','Site','Number of People','Creatinine - Site Based Division')
var_type_cret='Creatinine Distribution'
x_lab_cret = 'Creatinine Result'
y_lab_cret = 'Number of People'
histo_shape_plotter_sites(site1_cret,site2_cret,site3_cret,site4_cret,site5_cret,site6_cret,hist_bin_num,x_lab_cret,y_lab_cret , var_type_cret,col )

#Insulin 
[site1_insulin,site2_insulin,site3_insulin,site4_insulin,site5_insulin,site6_insulin] =site_sorter(data_field1['site'], data_field1['insulin'])
hdl_data_site = box_plotter_var_site(site1_insulin,site2_insulin,site3_insulin,site4_insulin,site5_insulin,site6_insulin)
box_plotter(hdl_data_site, 'Site','Site','Number of People','Insulin - Site Based Division')
var_type_insulin='Insulin Distribution'
x_lab_insulin = 'Insulin Result'
y_lab_insulin = 'Number of People'
histo_shape_plotter_sites(site1_insulin,site2_insulin,site3_insulin,site4_insulin,site5_insulin,site6_insulin,hist_bin_num,x_lab_insulin,y_lab_insulin, var_type_insulin,col )

#Sex based Creatinine and Insulin representations
#Creatinine representations
[male_cret,female_cret]=sex_sorter(data_field1['sex'],data_field1['s_creatinine'])
cret_data_sex = box_plotter_var_sex(male_cret,female_cret)
box_plotter(cret_data_sex , 'Sex','Sex','Number of People','Creatinine - Sex Based Division')
x_lab_cret_s = 'Creatinine Distribution'
y_lab_cret_s = 'Number of People'
var_type_cret_s = 'Creatinine Distribution'
histo_shape_plotter_sex(male_cret,female_cret,hist_bin_num,x_lab_cret_s,y_lab_cret_s,var_type_cret_s ,col)

#Insulin representations
[male_insulin,female_insulin]=sex_sorter(data_field1['sex'],data_field1['insulin'])
insulin_data_sex = box_plotter_var_sex(male_insulin,female_insulin)
box_plotter(insulin_data_sex , 'Sex','Sex','Number of People',' Insulin- Sex Based Division')
x_lab_insulin_s = 'Insulin Distribution'
y_lab_insulin_s = 'Number of People'
var_type_insulin_s = 'Insulin Distribution'
histo_shape_plotter_sex(male_insulin,female_insulin,hist_bin_num,x_lab_insulin_s,y_lab_insulin_s,var_type_insulin_s ,col)



