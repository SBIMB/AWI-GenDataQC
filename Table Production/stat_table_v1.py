#All the functions needed to generate statistic specific data for listed biomarkers

import numpy as num
from QC_table import tot_values

def min_per_site_v1(all_sites, below_spec, above_spec, branching,missing, 
                 missing_bio, missing_bio_ex):
    '''Returns the minimum value for a particular variable at each site excluding the 
    inserted values for branching and missing values. '''
    
    size = len(all_sites)
    minimum_total =list()
    
    for i in range(size):
        x = list(filter(lambda x : x!=below_spec and x!=above_spec and 
                        x != (branching) and x!= missing and
                        x!=missing_bio and x!=missing_bio_ex, all_sites[i]))
        minimum = num.nanmin(x)
        minimum = round(minimum ,2)
        minimum_total.append(minimum)
        
    return  minimum_total

def remove_inserted_values_v1(all_sites,branching,missing):
    '''Original logic for removing the inserted values for branching and missing values. '''
    
    size = len(all_sites)
    new_site_var = list(all_sites)
    total_vals = tot_values(all_sites)
    
    for i in range(size):
        
        size_temp = total_vals[i]
        temp = all_sites[i]
       
        for j in range (size_temp): 
           if temp[j] == branching or temp[j] == str(branching) or temp[j] == missing or temp[j] == str(missing) :
             new_site_var.remove(temp[j])
     
    return new_site_var

def min_per_site_noneg_v1(all_sites):
    '''Original function to return the minimum value for a particular variable at each site. 
    Does not exclude the inserted values for branching and missing values.'''
    
    size = len(all_sites)

    minimum_total =list()
    
    for i in range(size):
        minimum = num.nanmin(all_sites[i])
        minimum = round(minimum ,2)
        minimum_total.append(minimum)
        
    return  minimum_total
    
 

def max_per_site_v1(all_sites, below_spec, above_spec, branching,missing, 
                 missing_bio, missing_bio_ex):
    '''Returns the maximum value for a particular variable at each site excluding the 
    inserted values for branching and missing values. '''
    
    size = len(all_sites)
    maximum_total =list()
    
    for i in range(size):
        x = list(filter(lambda x : x!=below_spec and x!=above_spec and 
                        x != (branching) and x!= missing and
                        x!=missing_bio and x!=missing_bio_ex, all_sites[i]))
        maximum = num.nanmax(x)
        maximum = round(maximum ,2)
        maximum_total.append(maximum)
        
    return  maximum_total

def max_per_site_nonegs_v1(all_sites):
    '''Original function to return the maximum value for a particular variable at each site. 
    Does not exclude the inserted values for branching and missing values'''
    
    size = len(all_sites)
    maximum_total =list()
    
    for i in range(size):
        maximum = num.nanmax(all_sites[i])
        maximum = round(maximum ,2)
        maximum_total.append(maximum)
        
    return  maximum_total

def mean_per_site_v1(all_sites, below_spec, above_spec, branching,missing, 
                 missing_bio, missing_bio_ex):
    '''Returns the mean value for a particular variable at each site excluding the 
    inserted values for branching and missing values.'''
    
    size = len(all_sites)
    mean_total =list()
    
    for i in range(size):
        x = list(filter(lambda x : x!=below_spec and x!=above_spec and 
                        x!= (branching) and x!= missing and 
                        x!=missing_bio and x!=missing_bio_ex, all_sites[i]))
        mean = num.nanmean(x)
        mean = round(mean ,2)
        mean_total.append(mean)
        
    return  mean_total

def mean_per_site_nonegs_v1(all_sites):
    '''Original function to return the mean value for a particular variable at each site. Does 
    not exclude the inserted values for branching and missing values. '''
    
    size = len(all_sites)
    mean_total =list()
    
    for i in range(size):
        mean = num.nanmean(all_sites[i])
        mean = round(mean ,2)
        mean_total.append(mean)
        
    return  mean_total


def median_per_site_v1(all_sites, below_spec, above_spec, branching,missing, 
                 missing_bio, missing_bio_ex):
    '''Returns the median value for a particular variable at each site excluding the 
    inserted values for branching and missing values.'''
    
    size = len(all_sites)
    median_total =list()
    
    for i in range(size):
        x = list(filter(lambda x : x!=below_spec and x!=above_spec and 
                        x != (branching) and x!= missing and 
                        x!=missing_bio and x!=missing_bio_ex, all_sites[i]))
        median = num.nanmedian(x)
        median = round( median ,2)
        median_total.append(median)
        
    return median_total

def median_per_site_nonegs_v1(all_sites):
    '''Original function to return the median value for a particular variable at each site. 
    Does not exclude the inserted values for branching and missing values.'''
    
    size = len(all_sites)
    median_total =list()
    
    for i in range(size):
        median = num.nanmedian(all_sites[i])
        median = round( median ,2)
        median_total.append(median)
        
    return median_total

def std_dev_per_site_v1(all_sites, below_spec, above_spec, branching,missing, 
                 missing_bio, missing_bio_ex):
    '''Returns the standard deviation for a particular variable at each site excluding the 
    inserted values for branching and missing values.'''
    
    size = len(all_sites)
    standard_dev_total =list()
    
    for i in range(size):
        x = list(filter(lambda x : x!=below_spec and x!=above_spec and 
                        x != (branching) and x!= missing and 
                        x!=missing_bio and x!=missing_bio_ex, all_sites[i]))
        standard_dev = num.nanstd(x)
        standard_dev = round(standard_dev ,2)
        standard_dev_total.append(standard_dev)
        
    return   standard_dev_total

def std_dev_per_site_nonegs_v1(all_sites):
    '''Original function to return the standard deviation for a particular variable at each site.
     Does not exclude the inserted values for branching and missing values.'''
    
    size = len(all_sites)
    standard_dev_total =list()
    
    for i in range(size):
        
        standard_dev = num.nanstd(all_sites[i])
        standard_dev = round(standard_dev ,2)
        standard_dev_total.append(standard_dev)
        
    return   standard_dev_total








