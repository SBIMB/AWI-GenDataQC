#Storage for original instnces of the below named functions before modification  


#def all_values(study_var,var,site_ID,file,cohort_id, site):
#     ''' Records the number of instances of particular variable at each site and 
#     writes to a file the study ID, site ID ,cohort ID and site number of the variable'''
#     
#     size = len(study_var)
#     total_vals = tot_values(var)
#     site_values = list()
#     study_values = list()
#     site_ID_values =list()
#     cohort_ID_values = list()
#     recorded_values = list()
#     
#     
#     for i in range(size):
#        size_temp = total_vals[i]
#        temp = var[i]
#        for j in range (size_temp): 
#            
#                site_values .append(value_checker(site[i][j]))
#                study_values.append(value_checker(study_var[i][j]))
#                site_ID_values.append(value_checker(site_ID[i][j]))
#                cohort_ID_values.append(value_checker(cohort_id[i][j]))
#                recorded_values.append(value_checker(temp[j]))
#                
#                
#     data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
#     data.to_excel(file , sheet_name='All Values')
#     return total_vals
# 
#def creating_DF_without_values (site_num,siteID,studyID,cohortID):
#    tabled_data = pd.DataFrame({ "Site" : site_num ,
#                        "Site ID " : siteID,
#                         "Study ID" : studyID,
#                         "Cohort ID" : cohortID })
#
#    return tabled_data 

#def LLQ_inc_zero_capturing(site_var, llq,study_var,site_ID,file,cohort_id , site):
#    ''' Records the number of values below the lower limit of detection (including zero) for a particular 
#     variable at each site and writes to a file the study ID, site ID ,cohort ID and site
#     associted with these values as well as the detected value'''
#     
#    size = len(site_var)
#    num_below_llq = list()
#    total_vals = tot_values(site_var)
#    count = 0
#    site_values = list()
#    study_values = list()
#    site_ID_values =list()
#    cohort_ID_values = list()
#    recorded_values = list()
#   
#    for i in range(size):
#        size_temp = total_vals[i]
#        temp = site_var[i]
#        
#        for j in range (size_temp): 
#            if temp[j]< llq and temp[j] >= 0:
#                count= count + 1
#                site_values .append(value_checker(site[i][j]))
#                study_values.append(value_checker(study_var[i][j]))
#                site_ID_values.append(value_checker(site_ID[i][j]))
#                cohort_ID_values.append(value_checker(cohort_id[i][j]))
#                recorded_values.append(value_checker(temp[j]))
#                
#        num_below_llq.append(count)
#        count = 0
#        
#    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
#    data.to_excel(file , sheet_name='Below LLQ(inc 0)') 
#    return num_below_llq
