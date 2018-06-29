from QC_table import tot_values
from QC_table import value_checker
from QC_table import creating_DF_without_values
from QC_table import creating_DF_with_values

def greater_than_con_sex(study_var,var,site_ID,file,cohort_id, site,limit,sex):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  > limit:
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
                
        end_var.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name = sex + ' Values < ' + str(limit)) 
    return end_var



def con1_to_con2_sex(study_var,var,site_ID,file,cohort_id, site,limit1,limit2,sex):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()

   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  >= limit1 and temp[j] <= limit2 :
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
                
        end_var.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name = str(limit1) +' <= ' + sex + ' Values <= ' + str(limit2)) 
    return end_var

def not_con1_exc_zero_sex(study_var,var,site_ID,file,cohort_id,site, limit,sex):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j] > 0 and temp[j] < limit:
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
        end_var.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name='0 < ' + sex + ' Values < '+ str(limit)) 
    return end_var

def not_con1_inc_zero_sex(study_var,var,site_ID,file,cohort_id,site, limit,sex):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j] >= 0 and temp[j] < limit:
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
        end_var.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name='0 <= ' + sex + ' Values < '+ str(limit)) 
    return end_var


def below_con1_exc_zero_sex(study_var,var,site_ID,file,cohort_id,site, limit,sex):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j] > 0 and temp[j] <= limit:
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
        end_var.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name='0 < ' + sex + ' Values <= '+ str(limit)) 
    return end_var

def below_con1_inc_zero_sex(study_var,var,site_ID,file,cohort_id,site, limit,sex):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j] >= 0 and temp[j] <= limit:
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
        end_var.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name='0 <= ' + sex + ' Values <= '+ str(limit)) 
    return end_var

def below_LLQ_to_con1(study_var,var,site_ID,file,cohort_id, site,llq,limit):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j] >= llq and temp[j] <= limit:
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
        end_var.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name='LLQ =< Values <= '+ str(limit)) 
    return end_var

def below_LLQ_to_con1_samefile(study_var,var,site_ID,file,cohort_id, site,llq,limit):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    file.write('\n'+'LLQ =< Values <= '+ str(limit)+'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"+ ","+"Recorded Value" 
    file.write( heading +"\n" )
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j] >= llq and temp[j] <= limit:
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) + ','+ str(a)
                file.write( line +'\n')
        end_var.append(count)
        count = 0
    file.write('\n\n')
    return end_var

def below_LLQ_to_con1_original(var,llq,limit):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j] >= llq and temp[j] < limit:
                count= count + 1
        end_var.append(count)
        count = 0
    return end_var

def above_con1_exc_zero_original(var, limit):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  <= limit and temp[j] >0 :
                count= count + 1
        end_var.append(count)
        count = 0
    return end_var




def above_con1_exc_zero(study_var,var,site_ID,file,cohort_id, site,limit):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  <= limit and temp[j] >0 :
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
                
        end_var.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name='Values <= '+ str(limit) +" (exc 0) ") 
    return end_var

def above_con1_exc_zero_samefile(study_var,var,site_ID,file,cohort_id, site,limit):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    file.write('\n'+'Values <= '+ str(limit) +" (exc 0) "+'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"+ ","+"Recorded Value" 
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  <= limit and temp[j] >0 :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) + ','+ str(a)
                file.write( line +'\n')
        end_var.append(count)
        count = 0
    file.write('\n') 
    return end_var


    
def con1_to_con2(study_var,var,site_ID,file,cohort_id, site,limit1,limit2):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()

   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  > limit1 and temp[j] < limit2 :
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
                
        end_var.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name = str(limit1) + ' < Values < ' + str(limit2)) 
    return end_var

def con1_to_con2_samefile(study_var,var,site_ID,file,cohort_id, site,limit1,limit2):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    file.write('\n'+str(limit1) + ' < Values < ' + str(limit2)+'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"+ ","+"Recorded Value" 
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  > limit1 and temp[j] < limit2 :
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) + ','+ str(a)
                file.write( line +'\n')
                
        end_var.append(count)
        count = 0
    file.write('\n')
    return end_var




def con1_to_con2_original(var, limit1, limit2):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  > limit1 and temp[j] < limit2 :
                count= count + 1
        end_var.append(count)
        count = 0
    return end_var


    
def greater_than_con(study_var,var,site_ID,file,cohort_id, site,limit):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    site_values = list()
    study_values = list()
    site_ID_values =list()
    cohort_ID_values = list()
    recorded_values = list()
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  >= limit:
                count= count + 1
                site_values .append(value_checker(site[i][j]))
                study_values.append(value_checker(study_var[i][j]))
                site_ID_values.append(value_checker(site_ID[i][j]))
                cohort_ID_values.append(value_checker(cohort_id[i][j]))
                recorded_values.append(value_checker(temp[j]))
                
        end_var.append(count)
        count = 0
    data = creating_DF_with_values (site_values,study_values,site_ID_values,cohort_ID_values,recorded_values)
    data.to_excel(file , sheet_name = 'Values >= ' + str(limit)) 
    return end_var



def greater_than_con_samefile(study_var,var,site_ID,file,cohort_id, site,limit):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
    file.write('\n'+'Values >= ' + str(limit)+'\n')
    heading = "Site"+","+"Site ID "+","+"Study ID" +","+"Cohort ID"+ ","+"Recorded Value" 
    file.write( heading +"\n" )
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  >= limit:
                count= count + 1
                w = value_checker(site[i][j])
                x= value_checker(study_var[i][j])
                y = value_checker(site_ID[i][j])
                z = value_checker(cohort_id[i][j])
                a = value_checker(temp[j])
                line = str(w) +','+ str(x) + ',' + str(y)+ ',' + str(z) + ','+ str(a)
                file.write( line +'\n')
        end_var.append(count)
        count = 0
    file.write('\n\n')  
    return end_var



def greater_than_con_original(var, limit):
    
    size = len(var)
    end_var= list()
    total_vals = tot_values(var)
    count = 0
   
    for i in range(size):
        size_temp = total_vals[i]
        temp = var[i]
        
        for j in range (size_temp): 
            if temp[j]  >= limit:
                count= count + 1
        end_var.append(count)
        count = 0
    return end_var




