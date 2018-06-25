import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seaB
#from statistics import calculate_stats
#from plotters import histogram_plotter
#from plotters  import histo_shape_plotter
from plotters import box_plotter
from variable_Grouping import site_sorter
from variable_Grouping import sex_sorter
from variable_Grouping import box_plotter_var_site
from variable_Grouping import box_plotter_var_sex
from variable_Grouping import histo_shape_plotter_sites
from variable_Grouping import histo_shape_plotter_sex


data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/data.csv")
col = 'darkblue'
hist_bin_num = 10

#Site based LDL and HDL representations
#HDL representations
[site1_hdl,site2_hdl,site3_hdl,site4_hdl,site5_hdl,site6_hdl] =site_sorter(data_field1['site'], data_field1['hdl'])
hdl_data_site = box_plotter_var_site(site1_hdl,site2_hdl,site3_hdl,site4_hdl,site5_hdl,site6_hdl)
#box_plotter(hdl_data_site, 'Site','Site','Number of People','HDL - Site Based Division')
var_type_hdl='HDL Distribution'
x_lab_hdl = 'HDL Result'
y_lab_hdl = 'Number of People'
histo_shape_plotter_sites(site1_hdl,site2_hdl,site3_hdl,site4_hdl,site5_hdl,site6_hdl,hist_bin_num,x_lab_hdl,y_lab_hdl, var_type_hdl,col )


#line 5887 , ultrasound notes , PLAQUE D'ATHEROSE D'ENVIRON 0.28 CM AU NIVEAU DE LA BIFURCATION DE L'ARTï¿½RE CAROTIDE DROITE
