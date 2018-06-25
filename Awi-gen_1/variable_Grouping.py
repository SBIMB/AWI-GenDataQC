import pandas as pd
from plotters  import histo_shape_plotter

def site_sorter(site_var, var):
    '''Sorts a specified data field into the different sites'''
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
            print('problem')
            #raise ValueError('Invalid site specified in row ' + str(i)+ ' of site column')
    return site_1,site_2,site_3,site_4,site_5,site_6


def sex_sorter(sex_var, var ):
    '''Sorts a specified data field into different sexes'''
    male= list()
    female= list()
    tot_Values = sex_var.shape[0]
    for i in range(tot_Values):
     
        if sex_var[i] ==0:
            female.append(var[i])
        
        elif sex_var[i] ==1:
            male.append(var[i])
        
        else:
            #raise ValueError('Invalid sex specified in row ' + str(i)+ ' of sex column')
            print('problem')
    return male,female

def box_plotter_var_site(s1,s2,s3,s4,s5,s6):
    '''Generates variables from sites for box plotter'''
    DF_site1 = pd.DataFrame(s1).assign(Site = 1)
    DF_site2 = pd.DataFrame(s2).assign(Site = 2)
    DF_site3 = pd.DataFrame(s3).assign(Site = 3)
    DF_site4 = pd.DataFrame(s4).assign(Site = 4)
    DF_site5 = pd.DataFrame(s5).assign(Site = 5)
    DF_site6 = pd.DataFrame(s6).assign(Site = 6)
    
    data = pd.concat([DF_site1,DF_site2, DF_site3 , DF_site4 , DF_site5,DF_site6],sort=True)
    
    return  data


    
def box_plotter_var_sex(male, female):
    '''Generates variables from sexes for box plotter'''
    DF_male  = pd.DataFrame(male).assign(Sex="Male")
    DF_female  = pd.DataFrame(female).assign(Sex = "Female")
    data = pd.concat([DF_male ,DF_female])    
    return data


def histo_shape_plotter_sites(s1,s2,s3,s4,s5,s6 ,hist_bin,x_lab,y_lab, var_type ,col ):
    
    title = 'Site 1 ' + var_type
    histo_shape_plotter(s1,hist_bin,title, x_lab , y_lab,col )
    title = 'Site 2 ' + var_type
    histo_shape_plotter(s2,hist_bin,title, x_lab , y_lab,col )
    title = 'Site 3 ' + var_type
    histo_shape_plotter(s3,hist_bin,title, x_lab , y_lab,col )
    title = 'Site 4 ' + var_type
    histo_shape_plotter(s4,hist_bin,title, x_lab , y_lab,col )
    title = 'Site 5 ' + var_type
    histo_shape_plotter(s5,hist_bin,title, x_lab , y_lab,col )
    title = 'Site 6 ' + var_type
    histo_shape_plotter(s6,hist_bin,title, x_lab , y_lab,col )
    
def histo_shape_plotter_sex(male, female,hist_bin,x_lab,y_lab, var_type ,col ):
    title = var_type + ' for Males'
    histo_shape_plotter(male ,hist_bin,title, x_lab , y_lab,col )
    title = var_type + ' for Females'
    histo_shape_plotter(female ,hist_bin,title, x_lab , y_lab,col )
   
    


    

    
    
    
    
    