import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seaB



def histogram_plotter(field, bin_count , title, x_lab , y_lab):
    '''Plots a basic histogram'''
    plt.hist(field , bin_count )
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.show()
    plt.clf()
    
def histo_shape_plotter(field, bin_count , title, x_lab , y_lab, col):
    
    plot = seaB.distplot(field, hist=True, kde=False, 
             bins=bin_count, color = col, 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 2})

    second_ax = plot.twinx()

    seaB.distplot(field, hist=False, kde=True, 
             bins=bin_count, color = col, 
             hist_kws={'edgecolor':'black'},
             kde_kws={'linewidth': 2})
    second_ax.set_yticks([])
    plot.set(xlabel=x_lab, ylabel=y_lab,title =title)
    plt.show()
    plt.clf()


def box_plotter(concate_data, idVar,xlab,ylab,tit):
                                 # CONCATENATE
    mdf = pd.melt(concate_data, id_vars = [idVar])      # MELT
    ax = seaB.boxplot(x=idVar, y="value", data=mdf)  # RUN PLOT   
    ax.set(xlabel=xlab, ylabel=ylab,title = tit)
    plt.show()
    plt.clf()
    plt.close()


def histogram_plotter_var2(field1,field2,legend_tit1,legend_tit2,  bin_count , title, x_lab , y_lab):
    '''Plots a basic histogram with 2 variables'''
    legend = [legend_tit1,legend_tit2]
    plt.hist([field1,field2], bins = bin_count )
    plt.legend(legend)
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.show()
    plt.clf()
    
def histogram_plotter_var3(field1,field2,field3,legend_tit1,legend_tit2,legend_tit3,  bin_count , title, x_lab , y_lab):
    '''Plots a basic histogram with 3 variables'''
    legend = [legend_tit1,legend_tit2,legend_tit3]
    plt.hist([field1,field2,field3], bins = bin_count )
    plt.legend(legend)
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.show()
    plt.clf()
    
def histogram_plotter_var2_site(site_var1,site_var2,legend_tit1,legend_tit2,  bin_count , title, x_lab , y_lab):
    
    title0= 'Site 1 - ' + title
    histogram_plotter_var2(site_var1[0],site_var2[0],legend_tit1, legend_tit2,  bin_count , title0, x_lab , y_lab)
    title1= 'Site 2 - ' + title
    histogram_plotter_var2(site_var1[1],site_var2[1],legend_tit1,legend_tit2,  bin_count , title1, x_lab , y_lab)
    title2= 'Site 3 - ' + title
    histogram_plotter_var2(site_var1[2],site_var2[2],legend_tit1,legend_tit2,  bin_count , title2, x_lab , y_lab)
    title3= 'Site 4 - ' + title
    histogram_plotter_var2(site_var1[3],site_var2[3],legend_tit1,legend_tit2,  bin_count , title3, x_lab , y_lab)
    title4= 'Site 5 - ' + title
    histogram_plotter_var2(site_var1[4],site_var2[4],legend_tit1,legend_tit2,  bin_count , title4, x_lab , y_lab)
    title5= 'Site 6 - ' + title
    histogram_plotter_var2(site_var1[5],site_var2[5],legend_tit1,legend_tit2,  bin_count , title5, x_lab , y_lab)
    
    
def histogram_plotter_var2_sex(sex_var1,sex_var2,legend_tit1,legend_tit2,  bin_count , title, x_lab , y_lab):
    
    title0= title + ' for Males'
    histogram_plotter_var2(sex_var1[0],sex_var2[0],legend_tit1, legend_tit2,  bin_count , title0, x_lab , y_lab)
    title1= title + ' for Females'
    histogram_plotter_var2(sex_var1[1],sex_var2[1],legend_tit1,legend_tit2,  bin_count , title1, x_lab , y_lab)
   
    
    
    
    
    
    