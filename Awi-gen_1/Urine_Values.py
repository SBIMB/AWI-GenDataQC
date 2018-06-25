# =============================================================================
# Urine Samples
# =============================================================================
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


data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/Test Data.csv")
col = 'darkblue'
hist_bin_num = 10


#Site based Creatinine
[site1_cret,site2_cret,site3_cret,site4_cret,site5_cret,site6_cret] =site_sorter(data_field1['site'], data_field1['ur_creatinine'])
cret_data_site = box_plotter_var_site(site1_cret,site2_cret,site3_cret,site4_cret,site5_cret,site6_cret)
#box_plotter(cret_data_site, 'Site','Site','Number of People','Creatinine - Site Based Division')
var_type_cret='Creatinine Distribution'
x_lab_cret = 'Creatinine Result'
y_lab_cret = 'Number of People'
histo_shape_plotter_sites(site1_cret,site2_cret,site3_cret,site4_cret,site5_cret,site6_cret,hist_bin_num,x_lab_cret,y_lab_cret, var_type_cret,col )
