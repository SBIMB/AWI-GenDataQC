import numpy as num


def site_sorter(site_var, var,sites):
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
            sites[0]=1
        
        elif site_var[i]==2:
            site_2.append(var[i])
            sites[1]=1
             
        elif site_var[i] ==3:
            site_3.append(var[i])
            sites[2]=1
             
        elif site_var[i] ==4:
            site_4.append(var[i])
            sites[3]=1
             
        elif  site_var[i]==5:
            site_5.append(var[i])
            sites[4]=1
             
        elif site_var[i] ==6:
            site_6.append(var[i])
            sites[5]=1
             
       # else:
            #print('problem')
            #raise ValueError('Invalid site specified in row ' + str(i)+ ' of site column')
            
    init_data = list([site_1, site_2, site_3, site_4, site_5, site_6])
    data = populate_sites (sites, init_data)
    getNum_sites(sites)
    
    return data



def getNum_sites(sites):
    values = list()
    size = len(sites)
    for i in range(size):
        if sites[i] ==1:
            values.append(i+1)
           
        
    return values


def populate_sites(sites,init_data):
    size = len(init_data)
    data = list()
    for i in range(size):
        if sites[i]==1:
            data.append(init_data[i])
    return data

def min_per_site(all_sites):
    size = len(all_sites)
    minimum_total =list()
    
    for i in range(size):
        minimum = num.nanmin(all_sites[i])
        minimum = round(minimum ,2)
        minimum_total.append(minimum)
        
    return  minimum_total


def max_per_site(all_sites):
    size = len(all_sites)
    maximum_total =list()
    
    for i in range(size):
        maximum = num.nanmax(all_sites[i])
        maximum = round(maximum ,2)
        maximum_total.append(maximum)
        
    return  maximum_total

def mean_per_site(all_sites):
    size = len(all_sites)
    mean_total =list()
    
    for i in range(size):
        mean = num.nanmean(all_sites[i])
        mean = round(mean ,2)
        mean_total.append(mean)
        
    return  mean_total

def median_per_site(all_sites):
    size = len(all_sites)
    median_total =list()
    
    for i in range(size):
        median = num.nanmedian(all_sites[i])
        median = round( median ,2)
        median_total.append(median)
        
    return median_total

def standard_dev_per_site(all_sites):
    size = len(all_sites)
    standard_dev_total =list()
    
    for i in range(size):
        standard_dev = num.nanstd(all_sites[i])
        standard_dev = round(standard_dev ,2)
        standard_dev_total.append(standard_dev)
        
    return   standard_dev_total