import numpy as num
import pandas as pd

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

#
#def zero_capturing(study_var,var,site_ID,file):
#    #def studyID_of_zero(study_var,var,site_var):
#     size = len(study_var)
#     total_vals = tot_values(var)
#     file.write("Zero Values"+'\n')
#     file.write("Site ID "+"\t\t\t"+"Study ID" +'\n')
#     
#     for i in range(size):
#        size_temp = total_vals[i]
#        temp = var[i]
#        
#        for j in range (size_temp): 
#            
#            if temp[j] == 0:
#                x=study_var[i][j]
#                y = site_ID[i][j]
#                file.write(x + "\t\t\t\t" + y+'\n')
                
def zero_capturing(study_var,var,site_ID,file,cohort_id):
    #def studyID_of_zero(study_var,var,site_var):
     size = len(study_var)
     total_vals = tot_values(var)
     file.write('\n'+"Zero Values"+'\n')
     file.write("Site ID "+"\t\t\t"+"Study ID" +"\t\t\t"+"Cohort ID" '\n')
     zero_vals = zero_number(var)
     
     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            
            if temp[j] == 0:
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                file.write(x + "\t\t\t\t" + y+  "\t\t\t\t" +z+'\n')
     file.write('\n')          
     return zero_vals

def null_capturing(study_var,var,site_ID,file,cohort_id):
    #def studyID_of_zero(study_var,var,site_var):
     size = len(study_var)
     total_vals = tot_values(var)
     file.write("Null Values"+'\n')
     file.write("Site ID "+"\t\t\t"+"Study ID" +"\t\t\t"+"Cohort ID" '\n')
     total_null_number =null_number(var)
     
     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            
            if (pd.isnull(temp[j]))== True:
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                file.write(x + "\t\t\t\t" + y+  "\t\t\t\t" +z+'\n')
     file.write('\n') 
     return total_null_number


def studyID_of_zero(study_var,var):
    #def studyID_of_zero(study_var,var,site_var):
     size = len(study_var)
     total_vals = tot_values(var)
     study = list()
     #site = list()

     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            
            if temp[j] == 0:
                x=study_var[i][j]
                study.append(value_checker(x))
                #site.append(site_var[i][j])
     return study
 
def siteID_of_zero(site_ID,var):
    #def studyID_of_zero(study_var,var,site_var):
     size = len(site_ID)
     total_vals = tot_values(var)
     site_id = list()
     #site = list()

     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            
            if temp[j] == 0:
                x=site_ID[i][j]
                site_id .append(value_checker(x))
                #site.append(site_var[i][j])
     return  site_id 
 
def zeros_to_file(study_var,var,site_ID,file):
     site_ID_values = siteID_of_zero(site_ID,var)
     study_ID_values = studyID_of_zero(study_var,var)
     size = len( study_ID_values)
     
     file.write("Zero Values"+'\n')
     file.write("Site ID "+"\t\t\t"+" Study ID" +'\n')
     for i in range(size):
         file.write(site_ID_values[i] + "\t\t\t\t" + study_ID_values[i]+'\n')
         

def cohortID_of_zero(cohort_ID,var):
    #def studyID_of_zero(study_var,var,site_var):
     size = len(cohort_ID)
     total_vals = tot_values(var)
     site_id = list()
     #site = list()

     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            
            if temp[j] == 0:
                x=cohort_ID[i][j]
                site_id .append(value_checker(x))
                #site.append(site_var[i][j])
     return  site_id 
 
     
    
def value_checker(val):
    x = " "
    if pd.isnull(val):
        return x
    else:
        return val
        

def LLD_inc_zero_capturing(site_var, lld,study_var,site_ID,file,cohort_id):
    
    size = len(site_var)
    num_below_lld = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Below the Lower Limit of Detection (including \"0\" )" +'\n')
    file.write("Site ID "+"\t\t\t"+"Study ID" +"\t\t\t"+"Cohort ID" '\n')
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < lld:
                count= count + 1
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                file.write(x + "\t\t\t\t" + y+  "\t\t\t\t" +z+'\n')
        num_below_lld.append(count)
        count = 0
    file.write('\n')  
    return num_below_lld

#def studyID_of_zero(study_var,var,site_var):
#     size = len(study_var)
#     total_vals = tot_values(var)
#     file.write('\n'+"Zero Values"+'\n')
#     file.write("Site ID "+"\t\t\t"+"Study ID" +"\t\t\t"+"Cohort ID" '\n')
#     zero_vals = zero_number(var)
#     
#     for i in range(size):
#        size_temp = total_vals[i]
#        temp = var[i]
#        
#        for j in range (size_temp): 
#            
#            if temp[j] == 0:
#                x= value_checker(study_var[i][j])
#                y = value_checker(site_ID[i][j])
#                z = value_checker(cohort_id[i][j])
#                file.write(x + "\t\t\t\t" + y+  "\t\t\t\t" +z+'\n')
#     file.write('\n')          
#


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


def LLD_exc_zero_capturing(site_var, lld,study_var,site_ID,file,cohort_id):
    
    size = len(site_var)
    num_below_lld = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Below Lower Limit of Detection (excluding \"0\" )" +'\n')
    file.write("Site ID "+"\t\t\t"+"Study ID" +"\t\t\t"+"Cohort ID" '\n')
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < lld and temp[j] != 0 :
                count= count + 1
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                file.write(x + "\t\t\t\t" + y+  "\t\t\t\t" +z+'\n')
        num_below_lld.append(count)
        count = 0
    file.write('\n')  
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


def ULD_capturing(site_var, uld,study_var,site_ID,file,cohort_id):
    
    size = len(site_var)
    num_above_uld= list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Above the Upper Limit of Detection (excluding \"0\" )" +'\n')
    file.write("Site ID "+"\t\t\t"+"Study ID" +"\t\t\t"+"Cohort ID" '\n')
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] > uld :
                count= count + 1
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                file.write(x + "\t\t\t\t" + y+  "\t\t\t\t" +z+'\n')
        num_above_uld.append(count)
        count = 0
    file.write('\n') 
    return num_above_uld
    
    
    
    


