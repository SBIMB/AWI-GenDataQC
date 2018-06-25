from QC_table import tot_values


def below_LLD_to_con1(site_var, lld, limit):
    
    size = len(site_var)
    end_var= list()
    total_vals = tot_values(site_var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] >= lld and temp[j] < limit:
                count= count + 1
        end_var.append(count)
        count = 0
    return end_var


def above_con1_exc_zero(site_var, limit):
    
    size = len(site_var)
    end_var= list()
    total_vals = tot_values(site_var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j]  <  limit and temp[j] !=0 :
                count= count + 1
        end_var.append(count)
        count = 0
    return end_var

def con1_to_con2(site_var, limit1, limit2):
    
    size = len(site_var)
    end_var= list()
    total_vals = tot_values(site_var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j]  > limit1 and temp[j] < limit2 :
                count= count + 1
        end_var.append(count)
        count = 0
    return end_var


def greater_than_con(site_var, limit):
    
    size = len(site_var)
    end_var= list()
    total_vals = tot_values(site_var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j]  >= limit:
                count= count + 1
        end_var.append(count)
        count = 0
    return end_var

