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
X =site_sorter(data_field1['site'], data_field1['hdl'])
print(X)
print()
print()
print(X[4])
#hdl_data_site = box_plotter_var_site(site1_hdl,site2_hdl,site3_hdl,site4_hdl,site5_hdl,site6_hdl)
#ox_plotter(hdl_data_site, 'Site','Site','Number of People','HDL - Site Based Division')
    
