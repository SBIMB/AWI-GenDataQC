import numpy as num
import pandas as pd

def tot_values(site_var):
    ''' Records the total number of values for a particular variable at each site '''

    total_val = [len(x) for x in site_var]
    return total_val
    

def null_number(site_var):
    ''' Records the number of instances of null values for a particular variable at each site '''
    
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
    ''' Records the number of instances of zero values for a particular variable at each site '''
    
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
                
def zero_capturing_init(study_var,var,site_ID,file,cohort_id):
     ''' Records the number of instances of zero values for a particular variable at each site and 
     writes to a file the study ID, site ID and cohort ID associted with each zero instance'''
     
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
                file.write(str(x) + "\t\t\t\t" + str(y) +  "\t\t\t\t" + str(z) +'\n')
     file.write('\n')          
     return zero_vals
 
def zero_capturing(study_var,var,site_ID,file,cohort_id, site):
     ''' Records the number of instances of zero values for a particular variable at each site and 
     writes to a file the study ID, site ID ,cohort ID and site number associted with each zero instance'''
     
     size = len(study_var)
     total_vals = tot_values(var)
     file.write('\n'+"Zero Values"+'\n')
     heading = "{0:20} {1:20} {2:20} {3:20}".format("Site", "Site ID","Study ID" ,"Cohort ID")
     file.write( heading +"\n" )
     zero_vals = zero_number(var)
     
     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            
            if temp[j] == 0:
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                line = "{0:20} {1:20} {2:20} {3:20}".format(str(w), str(x),str(y) ,str(z))
                file.write( line +'\n')
     file.write('\n')          
     return zero_vals

def null_capturing_init(study_var,var,site_ID,file,cohort_id):
     ''' Records the number of instances of null values for a particular variable at each site and 
     writes to a file the study ID, site ID and cohort ID associted with each null instance'''
     
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
                file.write(str(x) + "\t\t\t\t" + str(y) +  "\t\t\t\t" +str(z) +'\n')
     file.write('\n') 
     return total_null_number
 
def null_capturing(study_var,var,site_ID,file,cohort_id,site):
     ''' Records the number of instances of null values for a particular variable at each site and 
     writes to a file the study ID, site ID ,cohort ID and site associted with each null instance'''
     
     size = len(study_var)
     total_vals = tot_values(var)
     file.write("Null Values"+'\n')
     heading = "{0:20} {1:20} {2:20} {3:20}".format("Site", "Site ID","Study ID" ,"Cohort ID")
     file.write( heading +"\n" )
     total_null_number =null_number(var)
     
     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            
            if (pd.isnull(temp[j]))== True:
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                line = "{0:20} {1:20} {2:20} {3:20}".format(str(w), str(x),str(y) ,str(z))
                file.write( line +'\n')
     file.write('\n') 
     return total_null_number



def studyID_of_zero(study_var,var):
     ''' Records the study IDs associated with the number of instances of zero values for a particular variable '''
     
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
     ''' Records the site IDs associated with the number of instances of zero values for a particular variable '''
     
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
     ''' Writes to a file the site IDs and study IDs associated with zeros associated with a particular variable'''
     
     site_ID_values = siteID_of_zero(site_ID,var)
     study_ID_values = studyID_of_zero(study_var,var)
     size = len( study_ID_values)
     
     file.write("Zero Values"+'\n')
     file.write("Site ID "+"\t\t\t"+" Study ID" +'\n')
     for i in range(size):
         file.write(site_ID_values[i] + "\t\t\t\t" + study_ID_values[i]+'\n')
         

def cohortID_of_zero(cohort_ID,var):
     ''' Records the cohort IDs associated with the number of instances of zero values for a particular variable '''
     
     size = len(cohort_ID)
     total_vals = tot_values(var)
     cohort_ID = list()
     #site = list()

     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            
            if temp[j] == 0:
                x=cohort_ID[i][j]
                cohort_ID .append(value_checker(x))
                #site.append(site_var[i][j])
     return  cohort_ID
 
     
    
def value_checker(val):
    '''Ensures that no null values get represented'''
    
    x = " "
    if pd.isnull(val):
        return x
    else:
        return val
        

def LLD_inc_zero_capturing_init(site_var, lld,study_var,site_ID,file,cohort_id):
    ''' Records the number values below the lower limit of detection (including zero) for a particular 
     variable at each site and writes to a file the study ID, site ID and cohort ID 
     associted with these values'''
     
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
                file.write(str(x) + "\t\t\t\t" + str(y) +  "\t\t\t\t" +str(z) +'\n')
        num_below_lld.append(count)
        count = 0
    file.write('\n')  
    return num_below_lld


def LLD_inc_zero_capturing(site_var, lld,study_var,site_ID,file,cohort_id , site):
    ''' Records the number values below the lower limit of detection (including zero) for a particular 
     variable at each site and writes to a file the study ID, site ID ,cohort ID and site
     associted with these values as well as the detected value'''
     
    size = len(site_var)
    num_below_lld = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Below the Lower Limit of Detection (including \"0\" )" +'\n')
    heading = "{0:20} {1:20} {2:20} {3:20} {4:20}".format("Site", "Site ID","Study ID" ,"Cohort ID","Recorded Value")
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < lld:
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = "{0:20} {1:20} {2:20} {3:20} {4:20}".format(str(w), str(x),str(y) ,str(z),str(a))
                file.write( line +'\n')
        num_below_lld.append(count)
        count = 0
    file.write('\n')  
    return num_below_lld

def LLD_inc_zero(site_var, lld):
    ''' Records the number of values for a particular variable at each site that are below 
    the lower limit of detection(including zero)'''
    
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


def LLD_exc_zero_capturing_init(site_var, lld,study_var,site_ID,file,cohort_id):
    ''' Records the number of values below the lower limit of detection (excluding zero) for a particular 
     variable at each site and writes to a file the study ID, site ID and Cohort ID 
     associted with these values'''
     
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

def LLD_exc_zero_capturing(site_var, lld,study_var,site_ID,file,cohort_id, site):
    ''' Records the number of values below the lower limit of detection (excluding zero) for a particular 
     variable at each site and writes to a file the study ID, site ID ,cohort ID and site 
     associted with these values as well as the detected value'''
     
    size = len(site_var)
    num_below_lld = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Below Lower Limit of Detection (excluding \"0\" )" +'\n')
    heading = "{0:20} {1:20} {2:20} {3:20} {4:20}".format("Site", "Site ID","Study ID" ,"Cohort ID","Recorded Value")
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < lld and temp[j] != 0 :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = "{0:20} {1:20} {2:20} {3:20} {4:20}".format(str(w), str(x),str(y) ,str(z),str(a))
                file.write( line +'\n')
        num_below_lld.append(count)
        count = 0
    file.write('\n')  
    return num_below_lld





def LLD_exc_zero(site_var, lld):
    ''' Records the number of values for a particular variable at each site that are below 
    the lower limit of detection(excluding zero)'''
    
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
    ''' Records the number of values for a particular variable at each site that are above
    the upper limit of detection'''
    
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


def ULD_capturing_init(site_var, uld,study_var,site_ID,file,cohort_id):
    ''' Records the number of values above the upper limit of detection for a particular 
     variable at each site and writes to a file the study ID, site ID and Cohort ID 
     associted with these values'''
     
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
    
def ULD_capturing(site_var, uld,study_var,site_ID,file,cohort_id,site ):
    ''' Records the number of values above the upper limit of detection for a particular 
     variable at each site and writes to a file the study ID, site ID, cohort ID and site 
     associted with these values and the detected value'''
     
    size = len(site_var)
    num_above_uld= list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values above Upper Limit of Detection" +'\n')
    heading = "{0:20} {1:20} {2:20} {3:20} {4:20}".format("Site", "Site ID","Study ID" ,"Cohort ID","Recorded Value")
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] > uld :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = "{0:20} {1:20} {2:20} {3:20} {4:20}".format(str(w), str(x),str(y) ,str(z),str(a))
                file.write( line +'\n')
        num_above_uld.append(count)
        count = 0
    file.write('\n') 
    return num_above_uld
    
    
    
    


