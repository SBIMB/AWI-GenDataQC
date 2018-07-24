#All the functions needed to generate QC specific data for listed biomarkers

import numpy as num
import pandas as pd

def tot_values(site_var):
    ''' Records the total number of values for a particular variable at each site '''

    total_val = [len(x) for x in site_var]
    return total_val

def all_values_samefile(study_var,var,site_ID,file,cohort_id, site):
     ''' Records the number of instances of particular variable at each site and 
     writes to a file the study ID, site ID ,cohort ID and site number of the variable. File 
     does not contain different tabs. '''
     
     size = len(study_var)
     total_vals = tot_values(var)
     file.write('\n'+"All Values of the Variable"+'\n')
     heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"+ ","+"Recorded Value" 
     file.write( heading +"\n" )
     
     
     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        for j in range (size_temp): 
            
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) + ','+ str(a)
                file.write( line +'\n')
                
     file.write('\n\n')          
     return total_vals
 
def all_values(study_var,var,site_ID,file,cohort_id, site):
     ''' Records the number of instances of particular variable at each site and 
     writes to a file the study ID, site ID ,cohort ID and site number of the variable.
     File contains different tabs for each of the different conditions of interest. '''
     
     size = len(study_var)
     total_vals = tot_values(var)
     site_values = list()
     study_values = list()
     site_ID_values =list()
     cohort_ID_values = list()
     recorded_values = list()
     
     
     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        for j in range (size_temp): 
            
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
                
                
     data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
     data.to_excel(file , sheet_name='All Values')
     return total_vals
 
def creating_DF_with_values (site_num,siteID,studyID,cohortID,values):
    '''Generates a dataframe which includes sites (number) , site ID, study ID, cohort ID and recorded value. '''
    
    tabled_data = pd.DataFrame({ "Site" : site_num ,
                        "Site ID " : siteID,
                         "Study ID" : studyID,
                         "Cohort ID" : cohortID,
                         "Recorded Value" :values })


    
    return tabled_data 


  

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


                
def zero_capturing_init(study_var,var,site_ID,file,cohort_id):
     ''' Records the number of instances of zero values for a particular variable at each site and 
     Writes to a file the study ID, site ID and cohort ID associted with each zero instance. This 
     file does not contain different tabs for each interest area.'''
     
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
                file.write(str(x) + "\t\t\t" + str(y) +  "\t\t\t" + str(z) +'\n')
     file.write('\n')          
     return zero_vals
 
def zero_capturing_txtdoc(study_var,var,site_ID,file,cohort_id, site):
     ''' Records the number of instances of zero values for a particular variable at each site and 
     writes to a file the study ID, site ID ,cohort ID and site number associted with each zero instance. This 
     file does not contain different tabs for each interest area. Associated formatting included has been 
     optimised for a text file.'''
     
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
 
def creating_DF_without_values (site_num,siteID,studyID,cohortID):
    '''Generates a dataframe which includes sites (number) , site ID, study ID and cohort ID. '''
    
    tabled_data = pd.DataFrame({ "Site" : site_num ,
                        "Site ID " : siteID,
                         "Study ID" : studyID,
                         "Cohort ID" : cohortID })

    return tabled_data 
 
def zero_capturing(study_var,var,site_ID,file,cohort_id, site):
     ''' Records the number of instances of zero values for a particular variable at each site and 
     writes to a file the study ID, site ID ,cohort ID and site number associted with each zero instance. 
     File is structured to have a different tab for each area of interest. '''
     
     size = len(study_var)
     total_vals = tot_values(var)
     zero_vals = zero_number(var)
     site_values = list()
     study_values = list()
     site_ID_values =list()
     cohort_ID_values = list()
     
     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            
            if temp[j] == 0:
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                
     data = creating_DF_without_values(site_values,study_values,site_ID_values,cohort_ID_values)
     data.to_excel(file , sheet_name='Zero Values')    
      
     return zero_vals

def zero_capturing_samefile(study_var,var,site_ID,file,cohort_id, site):
     ''' Records the number of instances of zero values for a particular variable at each site and 
     writes to a file the study ID, site ID ,cohort ID and site number associted with each zero instance. File 
     does not contain different tabs. '''
     
     size = len(study_var)
     total_vals = tot_values(var)
     file.write('\n'+"Zero Values"+'\n')
     heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID" 
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
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z)
                file.write( line +'\n')
     file.write('\n')          
     return zero_vals

def null_capturing_init(study_var,var,site_ID,file,cohort_id):
     ''' Records the number of instances of null values for a particular variable at each site and 
     writes to a file the study ID, site ID and cohort ID associted with each null instance. File 
     does not contain different tabs. '''
     
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
 
def null_capturing_txtdoc(study_var,var,site_ID,file,cohort_id,site):
     ''' Records the number of instances of null values for a particular variable at each site and 
     writes to a file the study ID, site ID ,cohort ID and site associted with each null instance . This 
     file does not contain different tabs for each interest area. Associated formatting included has been 
     optimised for a text file.'''
     
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
 


def null_capturing(study_var,var,site_ID,file,cohort_id,site):
     ''' Records the number of instances of null values for a particular variable at each site and 
     writes to a file the study ID, site ID ,cohort ID and site associted with each null instance. 
     File is structured to have a different tab for each area of interest. '''
     
     size = len(study_var)
     total_vals = tot_values(var)
     total_null_number =null_number(var)
     site_values = list()
     study_values = list()
     site_ID_values =list()
     cohort_ID_values = list()
     
     
     for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            
            if (pd.isnull(temp[j]))== True:
                 site_values .append(value_checker(site[i][j]))
                 study_values.append(value_checker(study_var[i][j]))
                 site_ID_values.append(value_checker(site_ID[i][j]))
                 cohort_ID_values.append(value_checker(cohort_id[i][j]))

     data = creating_DF_without_values (site_values,study_values,site_ID_values,cohort_ID_values)
     data.to_excel(file , sheet_name='Null Values')
     
     return total_null_number
 
def null_capturing_samefile(study_var,var,site_ID,file,cohort_id,site):
     ''' Records the number of instances of null values for a particular variable at each site and 
     writes to a file the study ID, site ID ,cohort ID and site associted with each null instance. File 
     does not contain different tabs. '''
     
     size = len(study_var)
     total_vals = tot_values(var)
     file.write("Null Values"+'\n')
     heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID" 
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
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z)
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
        

def LLQ_inc_zero_capturing_init(site_var, llq,study_var,site_ID,file,cohort_id):
    ''' Records the number of values below the lower limit of detection (including zero) for a particular 
     variable at each site and writes to a file the study ID, site ID and cohort ID 
     associted with these values. File does not contain different tabs.'''
     
    size = len(site_var)
    num_below_llq = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Below the Lower Limit of Detection (including \"0\" )" +'\n')
    file.write("Site ID "+"\t\t\t"+"Study ID" +"\t\t\t"+"Cohort ID" '\n')
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
             if temp[j]< llq and temp[j] >= 0:
                count= count + 1
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                file.write(str(x) + "\t\t\t\t" + str(y) +  "\t\t\t\t" +str(z) +'\n')
        num_below_llq.append(count)
        count = 0
    file.write('\n')  
    return num_below_llq


def LLQ_inc_zero_capturing_txtdoc(site_var, llq,study_var,site_ID,file,cohort_id , site):
    ''' Records the number of values below the lower limit of detection (including zero) for a particular 
     variable at each site and writes to a file the study ID, site ID ,cohort ID and site
     associted with these values as well as the detected value. This 
     file does not contain different tabs for each interest area. Associated formatting included has been 
     optimised for a text file.'''
     
    size = len(site_var)
    num_below_llq = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Below the Lower Limit of Detection (including \"0\" )" +'\n')
    heading = "{0:20} {1:20} {2:20} {3:20} {4:20}".format("Site", "Site ID","Study ID" ,"Cohort ID","Recorded Value")
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
             if temp[j]< llq and temp[j] >= 0:
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = "{0:20} {1:20} {2:20} {3:20} {4:20}".format(str(w), str(x),str(y) ,str(z),str(a))
                file.write( line +'\n')
        num_below_llq.append(count)
        count = 0
    file.write('\n')  
    return num_below_llq


def LLQ_inc_zero_capturing(site_var, llq,study_var,site_ID,file,cohort_id , site):
    ''' Records the number of values below the lower limit of detection (including zero) for a particular 
     variable at each site and writes to a file the study ID, site ID ,cohort ID and site
     associted with these values as well as the detected value. 
     File is structured to have a different tab for each area of interest. '''
     
    size = len(site_var)
    num_below_llq = list()
    total_vals = tot_values(site_var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if  temp[j]< llq and temp[j] >= 0:
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
                
        num_below_llq.append(count)
        count = 0
        
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name='Below LLQ - '+str(llq)) 
    return num_below_llq

def LLQ_inc_zero_capturing_samefile(site_var, llq,study_var,site_ID,file,cohort_id , site):
    ''' Records the number of values below the lower limit of detection (including zero) for a particular 
     variable at each site and writes to a file the study ID, site ID ,cohort ID and site
     associted with these values as well as the detected value.  File 
     does not contain different tabs.'''
     
    size = len(site_var)
    num_below_llq = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Below the Lower Limit of Detection (including \"0\" )" +'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"+ ","+"Recorded Value"
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j]< llq and temp[j] >= 0:
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) + ','+ str(a)
                file.write( line +'\n')
        num_below_llq.append(count)
        count = 0
    file.write('\n')  
    return num_below_llq

def LLQ_inc_zero(site_var, llq):
    ''' Records the number of values for a particular variable at each site that are below 
    the lower limit of detection(including zero)'''
    
    size = len(site_var)
    num_below_llq = list()
    total_vals = tot_values(site_var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
             if temp[j]< llq and temp[j] >= 0:
                count= count + 1
        num_below_llq.append(count)
        count = 0
    return num_below_llq


def LLQ_exc_zero_capturing_init(site_var, llq,study_var,site_ID,file,cohort_id):
    ''' Records the number of values below the lower limit of detection (excluding zero) for a particular 
     variable at each site and writes to a file the study ID, site ID and Cohort ID 
     associted with these values. File does not contain different tabs.'''
     
    size = len(site_var)
    num_below_llq = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Below Lower Limit of Detection (excluding \"0\" )" +'\n')
    file.write("Site ID "+"\t\t\t"+"Study ID" +"\t\t\t"+"Cohort ID" '\n')
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < llq and temp[j] > 0 :
                count= count + 1
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                file.write(x + "\t\t\t\t" + y+  "\t\t\t\t" +z+'\n')
        num_below_llq.append(count)
        count = 0
    file.write('\n')  
    return num_below_llq

def LLQ_exc_zero_capturing_txtdoc(site_var, llq,study_var,site_ID,file,cohort_id, site):
    ''' Records the number of values below the lower limit of detection (excluding zero) for a particular 
     variable at each site and writes to a file the study ID, site ID ,cohort ID and site 
     associted with these values as well as the detected value. This 
     file does not contain different tabs for each interest area. Associated formatting included has been 
     optimised for a text file.'''
     
    size = len(site_var)
    num_below_llq = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Below Lower Limit of Detection (excluding \"0\" )" +'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"+ ","+"Recorded Value"
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < llq and temp[j] > 0 :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = "{0:20} {1:20} {2:20} {3:20} {4:20}".format(str(w), str(x),str(y) ,str(z),str(a))
                file.write( line +'\n')
        num_below_llq.append(count)
        count = 0
    file.write('\n')  
    return num_below_llq



def LLQ_exc_zero_capturing(site_var, llq,study_var,site_ID,file,cohort_id, site):
    ''' Records the number of values below the lower limit of detection (excluding zero) for a particular 
     variable at each site and writes to a file the study ID, site ID ,cohort ID and site 
     associted with these values as well as the detected value. 
     File is structured to have a different tab for each area of interest.'''
     
    size = len(site_var)
    num_below_llq = list()
    total_vals = tot_values(site_var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < llq and temp[j] > 0 :
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))

        num_below_llq.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name='Below LLQ(exc 0) - '+ str(llq))
    return num_below_llq

def LLQ_exc_zero_capturing_samefile(site_var, llq,study_var,site_ID,file,cohort_id, site):
    ''' Records the number of values below the lower limit of detection (excluding zero) for a particular 
     variable at each site and writes to a file the study ID, site ID ,cohort ID and site 
     associted with these values as well as the detected value.  File 
     does not contain different tabs.'''
     
    size = len(site_var)
    num_below_llq = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Below Lower Limit of Detection (excluding \"0\" )" +'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"+ ","+"Recorded Value"
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < llq and temp[j] > 0 :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) + ','+ str(a)
                file.write( line +'\n')
        num_below_llq.append(count)
        count = 0
    file.write('\n')  
    return num_below_llq




def LLQ_exc_zero(site_var, llq):
    ''' Records the number of values for a particular variable at each site that are below 
    the lower limit of detection(excluding zero).'''
    
    size = len(site_var)
    num_below_llq = list()
    total_vals = tot_values(site_var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] < llq and temp[j] > 0 :
                count= count + 1
        num_below_llq.append(count)
        count = 0
    return num_below_llq


def ULQ(site_var, ulq):
    ''' Records the number of values for a particular variable at each site that are above
    the upper limit of detection.'''
    
    size = len(site_var)
    num_above_ulq= list()
    total_vals = tot_values(site_var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] > ulq :
                count= count + 1
        num_above_ulq.append(count)
        count = 0
    return num_above_ulq


def ULQ_capturing_init(site_var, ulq,study_var,site_ID,file,cohort_id):
    ''' Records the number of values above the upper limit of detection for a particular 
     variable at each site and writes to a file the study ID, site ID and Cohort ID 
     associted with these values. File does not contain different tabs.'''
     
    size = len(site_var)
    num_above_ulq= list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values Above the Upper Limit of Detection (excluding \"0\" )" +'\n')
    file.write("Site ID "+"\t\t\t"+"Study ID" +"\t\t\t"+"Cohort ID" +'\n')
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] > ulq :
                count= count + 1
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                file.write(x + "\t\t\t\t" + y+  "\t\t\t\t" +z+'\n')
        num_above_ulq.append(count)
        count = 0
    file.write('\n') 
    return num_above_ulq
    
def ULQ_capturing_txtdoc(site_var, ulq,study_var,site_ID,file,cohort_id,site ):
    ''' Records the number of values above the upper limit of detection for a particular 
     variable at each site and writes to a file the study ID, site ID, cohort ID and site 
     associted with these values and the detected value. This 
     file does not contain different tabs for each interest area. Associated formatting included has been 
     optimised for a text file.'''
     
    size = len(site_var)
    num_above_ulq= list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values above Upper Limit of Detection (excluding \"0\")" +'\n')
    heading = "{0:20} {1:20} {2:20} {3:20} {4:20}".format("Site", "Site ID","Study ID" ,"Cohort ID","Recorded Value")
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] > ulq :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = "{0:20} {1:20} {2:20} {3:20} {4:20}".format(str(w), str(x),str(y) ,str(z),str(a))
                file.write( line +'\n')
        num_above_ulq.append(count)
        count = 0
    file.write('\n') 
    return num_above_ulq
    

    
def ULQ_capturing(site_var, ulq,study_var,site_ID,file,cohort_id,site ):
    ''' Records the number of values above the upper limit of detection for a particular 
     variable at each site and writes to a file the study ID, site ID, cohort ID and site 
     associted with these values and the detected value. 
     File is structured to have a different tab for each area of interest.'''
     
    size = len(site_var)
    num_above_ulq= list()
    total_vals = tot_values(site_var)
    count = 0
    #file.write('\n'+"Values above Upper Limit of Detection (excluding \"0\")" +'\n')
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] > ulq :
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
                
        num_above_ulq.append(count)
        count = 0
        
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name='Above ULQ - ' + str(ulq)) 
    return num_above_ulq

def ULQ_capturing_samefile(site_var, ulq,study_var,site_ID,file,cohort_id,site ):
    ''' Records the number of values above the upper limit of detection for a particular 
     variable at each site and writes to a file the study ID, site ID, cohort ID and site 
     associted with these values and the detected value.  File 
     does not contain different tabs.'''
     
    size = len(site_var)
    num_above_ulq= list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Values above Upper Limit of Detection (excluding \"0\")" +'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"+ ","+"Recorded Value"
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] > ulq :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) + ','+ str(a)
                file.write( line +'\n')
        num_above_ulq.append(count)
        count = 0
    file.write('\n') 
    return num_above_ulq

def replaced_missing_capturing(site_var, replaced_missing,study_var,site_ID,file,cohort_id,site):
    ''' Records the number of values which have had their true null fields replaced with the replaced_missing
    value for a particular variable at each site and writes to a file the study ID, site ID ,cohort ID and site
    associted with these values. File is structured to have a different tab for each area of interest.'''
     
    size = len(site_var)
    num_replaced_missing = list()
    total_vals = tot_values(site_var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] == replaced_missing or temp[j] == str(replaced_missing) :
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                      
        num_replaced_missing.append(count)
        count = 0
    data = creating_DF_without_values (site_values,study_values,site_ID_values,cohort_ID_values)
    data.to_excel(file , sheet_name="True Missing("+str(replaced_missing)+")") 
    return num_replaced_missing

def replaced_missing_capturing_samefile(site_var, replaced_missing,study_var,site_ID,file,cohort_id,site):
    ''' Records the number of values which have had their true null fields replaced with the replaced_missing
    value for a particular variable at each site and writes to a file the study ID, site ID ,cohort ID and site
    associted with these values. File does not contain different tabs.'''
     
    size = len(site_var)
    num_replaced_missing = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Replaced True Missing Values ("+str(replaced_missing)+")"  +'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] == replaced_missing or temp[j] == str(replaced_missing) :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) 
                file.write( line +'\n')
        num_replaced_missing.append(count)
        count = 0
    file.write('\n')  
    return num_replaced_missing

def replaced_branching_capturing(site_var, replaced_branching,study_var,site_ID,file,cohort_id,site):
    ''' Records the number of values which have had their branching derived null fields replaced with the 
    replaced_branching value for a particular variable at each site and writes to a file the study ID, 
    site ID ,cohort ID and site associted with these values. File is structured to have a different tab for each area of interest.'''
     
    size = len(site_var)
    num_replaced_branching = list()
    total_vals = tot_values(site_var)
    count = 0
    #file.write('\n'+"Replaced Branching Missing Values ("+str(replaced_branching)+")"+'\n')
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] == replaced_branching or temp[j] == str(replaced_branching) :
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                
        num_replaced_branching.append(count)
        count = 0
    data = creating_DF_without_values (site_values,study_values,site_ID_values,cohort_ID_values)
    data.to_excel(file , sheet_name="Branching Missing("+str(replaced_branching)+")") 
    return num_replaced_branching

def replaced_branching_capturing_samefile(site_var, replaced_branching,study_var,site_ID,file,cohort_id,site):
    ''' Records the number of values which have had their branching derived null fields replaced with the 
    replaced_branching value for a particular variable at each site and writes to a file the study ID, 
    site ID ,cohort ID and site associted with these values. File 
     does not contain different tabs.'''
     
    size = len(site_var)
    num_replaced_branching = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Replaced Branching Missing Values ("+str(replaced_branching)+")"+'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] == replaced_branching or temp[j] == str(replaced_branching) :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) 
                file.write( line +'\n')
        num_replaced_branching.append(count)
        count = 0
    file.write('\n')  
    return num_replaced_branching
    
def replaced_missing_bio_capturing(site_var, replaced_missing_bio,study_var,site_ID,file,cohort_id,site):
    ''' Records the number of values which have had their branching derived null fields replaced with the 
    replaced_branching value for a particular variable at each site and writes to a file the study ID, 
    site ID ,cohort ID and site associted with these values. File is structured to have a different tab for each area of interest.'''
     
    size = len(site_var)
    num_replaced_missing_bio = list()
    total_vals = tot_values(site_var)
    count = 0
    #file.write('\n'+"Replaced Branching Missing Values ("+str(replaced_branching)+")"+'\n')
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] == replaced_missing_bio_capturing or temp[j] == str(replaced_missing_bio_capturing) :
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                
        num_replaced_missing_bio.append(count)
        count = 0
    data = creating_DF_without_values (site_values,study_values,site_ID_values,cohort_ID_values)
    data.to_excel(file , sheet_name="Branching Missing("+str(replaced_missing_bio)+")") 
    return num_replaced_missing_bio

def replaced_missing_bio_capturing_samefile(site_var, replaced_missing_bio,study_var,site_ID,file,cohort_id,site):
    ''' Records the number of values which have had their branching derived null fields replaced with the 
    replaced_branching value for a particular variable at each site and writes to a file the study ID, 
    site ID ,cohort ID and site associted with these values. File 
     does not contain different tabs.'''
     
    size = len(site_var)
    num_replaced_missing_bio = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Replaced Branching Missing Values ("+str(replaced_missing_bio)+")"+'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] == replaced_missing_bio or temp[j] == str(replaced_missing_bio) :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) 
                file.write( line +'\n')
        num_replaced_missing_bio.append(count)
        count = 0
    file.write('\n')  
    return num_replaced_missing_bio

def replaced_missing_bio_ex_capturing(site_var, replaced_missing_bio_ex,study_var,site_ID,file,cohort_id,site):
    ''' Records the number of values which have had their true null fields replaced with the replaced_missing
    value for a particular variable at each site and writes to a file the study ID, site ID ,cohort ID and site
    associted with these values. File is structured to have a different tab for each area of interest.'''
     
    size = len(site_var)
    num_replaced_missing_bio_ex = list()
    total_vals = tot_values(site_var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] == replaced_missing_bio_ex or temp[j] == str(replaced_missing_bio_ex) :
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                      
        num_replaced_missing_bio_ex.append(count)
        count = 0
    data = creating_DF_without_values (site_values,study_values,site_ID_values,cohort_ID_values)
    data.to_excel(file , sheet_name="True Missing("+str(replaced_missing_bio_ex)+")") 
    return num_replaced_missing_bio_ex

def replaced_missing_bio_ex_capturing_samefile(site_var, replaced_missing_bio_ex,study_var,site_ID,file,cohort_id,site):
    ''' Records the number of values which have had their true null fields replaced with the replaced_missing
    value for a particular variable at each site and writes to a file the study ID, site ID ,cohort ID and site
    associted with these values. File does not contain different tabs.'''
     
    size = len(site_var)
    num_replaced_missing_bio_ex = list()
    total_vals = tot_values(site_var)
    count = 0
    file.write('\n'+"Replaced True Missing Values ("+str(replaced_missing_bio_ex)+")"  +'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] == replaced_missing_bio_ex or temp[j] == str(replaced_missing_bio_ex) :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) 
                file.write( line +'\n')
        num_replaced_missing_bio_ex.append(count)
        count = 0
    file.write('\n')  
    return num_replaced_missing_bio_ex

def countSpecialCodes(site_var, code, codeDescrip, study_var, site_ID, file, cohort_id, site):
    ''' Records the number of values which have had their true null fields replaced with the replaced_missing
    value for a particular variable at each site and writes to a file the study ID, site ID ,cohort ID and site
    associted with these values. File is structured to have a different tab for each area of interest.'''
     
    size = len(site_var)
    num_code = list()
    total_vals = tot_values(site_var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = site_var[i]
        
        for j in range (size_temp): 
            if temp[j] == code or temp[j] == str(code) :
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                      
        num_code.append(count)
        count = 0
    data = creating_DF_without_values (site_values, study_values, site_ID_values,
                                       cohort_ID_values)
    data.to_excel(file , sheet_name=codeDescrip+"("+str(code)+")") 
    return num_code
