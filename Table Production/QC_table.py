import numpy as num


def tot_values(site_var):
    total_val = [len(x) for x in site_var]
    return total_val
    

def null_number(site_var):
    
    null_vals_bool =([num.isnan(x) for x in site_var])
    null_vals_num = list()
    size = len(null_vals_bool)
    count = 0
   
    for i in range(size):
        size_temp = len(null_vals_bool[i])
        temp = null_vals_bool[i]
        
        for j in range (size_temp): 
            if temp[j]==True:
                count= count + 1
        null_vals_num.append(count)
        count = 0
    return null_vals_num


def zero_number(site_var):
    non_zero_values = [num.count_nonzero(x) for x in site_var] 
    total_vals = tot_values(site_var)
    zero_vals =  [a - b for a, b in zip(total_vals,non_zero_values)]
    
    return zero_vals
    



def LLD_inc_zero(site_var, lld):
    
    size = len(site_var)
    num_below_lld = list()
    total_vals = tot_values(site_var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < lld:
                count= count + 1
        num_below_lld.append(count)
        count = 0
    return num_below_lld

def LLD_exc_zero(site_var, lld):
    
    size = len(site_var)
    num_below_lld = list()
    total_vals = tot_values(site_var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < lld and temp[j] != 0 :
                count= count + 1
        num_below_lld.append(count)
        count = 0
    return num_below_lld


def ULD(site_var, uld):
    
    size = len(site_var)
    num_above_uld= list()
    total_vals = tot_values(site_var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] > uld :
                count= count + 1
        num_above_uld.append(count)
        count = 0
    return num_above_uld
    
    
    
    


