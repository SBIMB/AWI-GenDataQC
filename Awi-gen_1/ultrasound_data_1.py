import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/Test Data.csv")
standard_deviation_limit = 0.6
hist_bin_num = 10
#####
#Plaque is defined as a focal structure that encroaches into the arterial lumen of at least 0.5 mm or 50% of 
#the surrounding IMT value or demonstrates a thickness >1.5 mm as measured from the media-adventitia interface 
#to the intima-lumen interface.

#https://www.karger.com/Article/Abstract/97034
######


#column_Names =list( data_field1)
#column_access = data_field1[column_Names[4]]  #eventually put this into a loop with each column being accessed 
#column_beg = ['ultrasound','visceral_fat','subcutaneous_fat', 'ultrasound_operator', 'date_ultrasound_taken','cimt','min_cimt_right']
#column_end = ['max_cimt_right','mean_cimt_right','min_cimt_left','max_cimt_left','mean_cimt_left','ultrasound_notes']
#columns = column_beg + column_end
#fields = data_field1[columns]
#tot_Values = fields.shape
#print(tot_Values[0])

def gen_stats(col):
    mean = np.mean(col)
    sd =np.std(col)
    median = np.median(col)
    return mean,sd,median

def calculate_stats (col,name):
    [mean,sd,median] = gen_stats(col)
    all_good = True
    
    if sd > standard_deviation_limit:
        print("Standard Deviation Exceeds Limit for " + name)
        all_good = False
        
    return mean,sd,median,all_good



def histogram_plotter(field, bin_count , title, x_lab , y_lab):
    plt.hist(field , bin_count)
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.show()
    plt.clf()
    
    
    

#Data per Site
def site_sorter(site_var, var):
    site_1= list()
    site_2= list()
    site_3= list()
    site_4= list()
    site_5= list()
    site_6= list()
    tot_Values = site_var.shape[0]
    for i in range(tot_Values):
     
        if site_var[i] ==1:
            site_1.append(var[i])
        
        elif site_var[i]==2:
            site_2.append(var[i])
             
        elif site_var[i] ==3:
            site_3.append(var[i])
             
        elif site_var[i] ==4:
            site_4.append(var[i])
             
        elif  site_var[i]==5:
            site_5.append(var[i])
             
        elif site_var[i] ==6:
            site_6.append(var[i])
            
             
        else:
            raise ValueError('Invalid site specified in row ' + str(i)+ ' of site column')
    return site_1,site_2,site_3,site_4,site_5,site_6




#Data per Sex where sex_var is the data_field1('sex')
def sex_sorter(sex_var, var ):
    male= list()
    female= list()
    tot_Values = sex_var.shape[0]
    for i in range(tot_Values):
     
        if sex_var[i] ==0:
            female.append(var[i])
        
        elif sex_var[i] ==1:
            male.append(var[i])
        
        else:
            raise ValueError('Invalid sex specified in row ' + str(i)+ ' of sex column')
    return male,female
    


#Sex specific Subcutaneous Fat
[male_sub_fat,female_sub_fat]=sex_sorter(data_field1['sex'],data_field1['subcutaneous_fat'])
[mean_sub_m,std_sub_m , median_sub_m,all_good_sub_m] = calculate_stats (male_sub_fat, 'subcutaneous_fat males')
title = 'Subcutaneous Fat Distribution for Males'
x_lab = 'Subcutaneous Fat Level'
y_lab = 'Number of People'
histogram_plotter(male_sub_fat,hist_bin_num,title, x_lab , y_lab )
title = 'Subcutaneous Fat Distribution for Females'
[mean_sub_f,std_sub_f , median_sub_f,all_good_sub_f] = calculate_stats (female_sub_fat,'subcutaneous_fat females')
histogram_plotter(female_sub_fat,hist_bin_num,title, x_lab , y_lab )


#Sex specific Visceral Fat
[male_vis_fat,female_vis_fat]=sex_sorter(data_field1['sex'],data_field1['visceral_fat'])
[mean_vis_m,std_vis_m , median_vis_m,all_good_vis_m] = calculate_stats (male_vis_fat,'visceral_fat males')
title = 'Visceral Fat Distribution for Males'
x_lab = 'Visceral Fat Level'
y_lab = 'Number of People'
histogram_plotter(male_vis_fat,hist_bin_num,title, x_lab , y_lab )
title = 'Visceral Fat Distribution for Females'
[mean_vis_f,std_vis_f , median_vis_f,all_good_vis_f] = calculate_stats (female_vis_fat,'visceral_fat females')
histogram_plotter(female_vis_fat,hist_bin_num,title, x_lab , y_lab )



#Total Data for Visceral and Subcutaneous Fat
[mean_vis_tot,std_vis_tot , median_vis_tot,all_good_vis_tot] = calculate_stats (data_field1['visceral_fat'],'visceral_fat total')
title = 'Total Visceral Fat Distribution'
x_lab = 'Visceral Fat Level'
y_lab = 'Number of People'
histogram_plotter(data_field1['visceral_fat'],hist_bin_num,title, x_lab , y_lab )

[mean_sub_tot,std_sub_tot, median_sub_tot,all_good_sub_tot] = calculate_stats (data_field1['subcutaneous_fat'],'subcutaneous_fat total')
title = 'Total Subcutaneous Fat Distribution'
x_lab = 'Subcutaneous Fat Level'
y_lab = 'Number of People'
histogram_plotter(data_field1['subcutaneous_fat'],hist_bin_num,title, x_lab , y_lab )



#Data per Sex where sex_var is the data_field1('sex')
#def sex_sorter(sex_var, var ,m,f):
#    
#    tot_Values = sex_var.shape[0]
#    for i in range(tot_Values):
#     
#        if sex_var[i] ==0:
#            f.append(var[i])
#        
#        elif sex_var[i] ==1:
#            m.append(var[i])
#        
#        else:
#            raise ValueError('Invalid sex specified in row ' + str(i)+ ' of sex column')
#    
#
#male= list()
#female= list()
#sex_sorter(data_field1['sex'],data_field1['subcutaneous_fat'],male,female)



#def check_min_cimt (col):
#    tot_Values = col.shape
#    minimum= ()
#    all_good = True
#    for i in range(tot_Values[0]):
#        if col[i] >0.35:
#            print('Minimum value for the entry in row ' + str(i) + " of " +  str(col.name)+ " were Below limit")
#            all_good= False
#            #minimum.append(col[i])
#    
#    [mean,sd,median] = gen_stats(col)
#    return mean,sd,median,all_good,minimum
#    
#   
#[mean_min_cimt_R,std_min_cimt_R, median_min_cimt_R,all_good_min_cimt_R,minimum_R]=check_min_cimt(data_field1['min_cimt_right'])
#[mean_min_cimt_L,std_min_cimt_L, median_min_cimt_L,all_good_min_cimt_L,minimum_L]=check_min_cimt(data_field1['min_cimt_left'])
#
#def check_max_cimt (col,minVal):
#    tot_Values = col.shape
#    all_good = True
#    for i in range(tot_Values[0]):
#        if col[i] >(minVal+0,5*minVal):
#            print('Minimum value for the entry in row ' + str(i) + " of " +  str(col.name)+ " were Below limit")
#            all_good= False
#    
#    [mean,sd,median] = gen_stats(col)
#    return mean,sd,median,all_good

#def check_Missing(col):
#    tot_Values = col.shape
#    for element in range(tot_Values[0]):
#        if col==1:
#         
#            
#        else:
#            return
#        
        

#
#def missing(data):
#     return sum(data.isnull())
# 
# 
#def sig_missing(list_val):
#    
#    s =list_val.size
#   
#    for i in range(s):
#        if list_val[i] > 0.0:
#            print(str(list_val.index[i])+ "\t\t\t".rjust(9) + str(list_val[i]) )
#            
#             
#
#data_missing=data_field1.apply(missing, axis=0) #axis=0 defines that function is to be applied on each colum
#print ("Missing values per column:")
#print()



#
##Sex specific Subcutaneous Fat
#[male_sub_fat,female_sub_fat]=sex_sorter(data_field1['sex'],data_field1['subcutaneous_fat'])
#[mean_sub_m,std_sub_m , median_sub_m,all_good_sub_m] = calculate_stats (male_sub_fat, 'subcutaneous_fat males')
#title = 'Subcutaneous Fat Distribution for Males'
#x_lab = 'Subcutaneous Fat Level'
#y_lab = 'Number of People'
#histogram_plotter(male_sub_fat,hist_bin_num,title, x_lab , y_lab )
#title = 'Subcutaneous Fat Distribution for Females'
#[mean_sub_f,std_sub_f , median_sub_f,all_good_sub_f] = calculate_stats (female_sub_fat,'subcutaneous_fat females')
#histogram_plotter(female_sub_fat,hist_bin_num,title, x_lab , y_lab )
#
#
##Sex specific Visceral Fat
#[male_vis_fat,female_vis_fat]=sex_sorter(data_field1['sex'],data_field1['visceral_fat'])
#[mean_vis_m,std_vis_m , median_vis_m,all_good_vis_m] = calculate_stats (male_vis_fat,'visceral_fat males')
#title = 'Visceral Fat Distribution for Males'
#x_lab = 'Visceral Fat Level'
#y_lab = 'Number of People'
#histogram_plotter(male_vis_fat,hist_bin_num,title, x_lab , y_lab )
#title = 'Visceral Fat Distribution for Females'
#[mean_vis_f,std_vis_f , median_vis_f,all_good_vis_f] = calculate_stats (female_vis_fat,'visceral_fat females')
#histogram_plotter(female_vis_fat,hist_bin_num,title, x_lab , y_lab )
#
#
#
##Total Data for Visceral Fat
#[mean_vis_tot,std_vis_tot , median_vis_tot,all_good_vis_tot] = calculate_stats (data_field1['visceral_fat'],'visceral_fat total')
#title = 'Total Visceral Fat Distribution'
#x_lab = 'Visceral Fat Level'
#y_lab = 'Number of People'
#histogram_plotter(data_field1['visceral_fat'],hist_bin_num,title, x_lab , y_lab )
#
##Total Data for Subcutaneous Fat
#
#[mean_sub_tot,std_sub_tot, median_sub_tot,all_good_sub_tot] = calculate_stats (data_field1['subcutaneous_fat'],'subcutaneous_fat total')
#title = 'Total Subcutaneous Fat Distribution'
#x_lab = 'Subcutaneous Fat Level'
#y_lab = 'Number of People'
#histogram_plotter(data_field1['subcutaneous_fat'],hist_bin_num,title, x_lab , y_lab )
#

