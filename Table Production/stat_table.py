import numpy as num

def min_per_site(all_sites):
    '''Returns the minimum value for a particular variable at each site '''
    
    size = len(all_sites)
    minimum_total =list()
    
    for i in range(size):
        minimum = num.nanmin(all_sites[i])
        minimum = round(minimum ,2)
        minimum_total.append(minimum)
        
    return  minimum_total


def max_per_site(all_sites):
    '''Returns the maximum value for a particular variable at each site '''
    
    size = len(all_sites)
    maximum_total =list()
    
    for i in range(size):
        maximum = num.nanmax(all_sites[i])
        maximum = round(maximum ,2)
        maximum_total.append(maximum)
        
    return  maximum_total

def mean_per_site(all_sites):
    '''Returns the mean value for a particular variable at each site '''
    
    size = len(all_sites)
    mean_total =list()
    
    for i in range(size):
        mean = num.nanmean(all_sites[i])
        mean = round(mean ,2)
        mean_total.append(mean)
        
    return  mean_total

def median_per_site(all_sites):
    '''Returns the median value for a particular variable at each site '''
    
    size = len(all_sites)
    median_total =list()
    
    for i in range(size):
        median = num.nanmedian(all_sites[i])
        median = round( median ,2)
        median_total.append(median)
        
    return median_total

def standard_dev_per_site(all_sites):
    '''Returns the standard deviation for a particular variable at each site '''
    
    size = len(all_sites)
    standard_dev_total =list()
    
    for i in range(size):
        standard_dev = num.nanstd(all_sites[i])
        standard_dev = round(standard_dev ,2)
        standard_dev_total.append(standard_dev)
        
    return   standard_dev_total









