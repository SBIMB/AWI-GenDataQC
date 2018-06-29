#File containing all the general sorting functions for division into site and sex based distributions


def sex_sorter(sex_var, var ):
    '''Sorts a specified data field into different sexes'''
    
    male= list()
    female= list()
    tot_Values = sex_var.shape[0]
    for i in range(tot_Values):
     
        if sex_var[i] ==0:
            female.append(var[i])
        
        elif sex_var[i] ==1:
            male.append(var[i])
        
        #else:
            #raise ValueError('Invalid sex specified in row ' + str(i)+ ' of sex column')
            #print('problem')
    return male,female



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
  

def getNum_sites_negVals(sites,branching,missing):
    '''Determines how many sites are represented in the .csv file read and returns the values necessary
    for indexing the table '''
    
    values = list()
    size = len(sites)
    
    for i in range(size):
        if sites[i] ==1:
            values.append(i+1)
            
    return values

def getNum_sites(sites):
    '''Determines how many sites are represented in the .csv file read and returns the values necessary
    for indexing the table '''
    
    values = list()
    size = len(sites)
    
    for i in range(size):
        if sites[i] ==1:
            values.append(i+1)
            
    return values


def populate_sites(sites,init_data):
    '''Populates the final data field for each site based on how many sites are represented '''
    size = len(init_data)
    data = list()
    for i in range(size):
        if sites[i]==1:
            data.append(init_data[i])
    return data

    
def site_and_sex_sorter(site_var,sites_m,sites_f, var,sex_var):
    '''Sorts a specified data field into both different sexes as well as seperate sites'''
    
    site_1_m= list()
    site_2_m= list()
    site_3_m= list()
    site_4_m= list()
    site_5_m= list()
    site_6_m= list()
    
    site_1_f = list()
    site_2_f = list()
    site_3_f = list()
    site_4_f = list()
    site_5_f = list()
    site_6_f = list() 
    
    tot_Values = site_var.shape[0]
   
    for i in range(tot_Values):
     
        if site_var[i] ==1:
            if sex_var[i] == 0:
                site_1_f.append(var[i])
                sites_f[0]=1
            elif sex_var[i] == 1:
                site_1_m.append(var[i])
                sites_m[0]=1
        
        elif site_var[i]==2:
            if sex_var[i] == 0:
                site_2_f.append(var[i])
                sites_f[1]=1
            elif sex_var[i] == 1:
                site_2_m.append(var[i])
                sites_m[1]=1

             
        elif site_var[i] ==3:
            if sex_var[i] == 0:
                site_3_f.append(var[i])
                sites_f[2]=1
            elif sex_var[i] == 1:
                site_3_m.append(var[i])
                sites_m[2]=1

             
        elif site_var[i] ==4:
            if sex_var[i] == 0:
                site_4_f.append(var[i])
                sites_f[3]=1
            elif sex_var[i] == 1:
                site_4_m.append(var[i])
                sites_m[3]=1
            
        elif  site_var[i]==5:
            if sex_var[i] == 0:
                site_5_f.append(var[i])
                sites_f[4]=1
            elif sex_var[i] == 1:
                site_5_m.append(var[i])
                sites_m[4]=1

                    
        elif site_var[i] ==6:
            if sex_var[i] == 0:
                site_6_f.append(var[i])
                sites_f[5]=1
            elif sex_var[i] == 1:
                site_6_m.append(var[i])
                sites_m[5]=1

       # else:
            #print('problem')
            #raise ValueError('Invalid site specified in row ' + str(i)+ ' of site column')
            
    init_data_females = list([site_1_f, site_2_f, site_3_f, site_4_f, site_5_f, site_6_f])
    
  
    sites_true = siteCompare_out(sites_m,sites_f)
  
    data_females = populate_sites (sites_true, init_data_females)
    init_data_males = list([site_1_m, site_2_m, site_3_m, site_4_m, site_5_m, site_6_m])
    
    data_males = populate_sites (sites_true, init_data_males)

    return  data_females, data_males

def siteCompare_out(site_m,site_f):
   '''Compares the two sites and takes the bigger of the two as the overall number
   of sites represented by the dataset. This function doesn't return the actual sites value but rather a 1 for a site 
   being present and a 0 if the site is absent'''
   
   if site_m.count(1) > site_f.count(1) :
      return site_m
   else:
       return site_f
    


def siteCompare(site_m,site_f):
   '''Compares the two sites and takes the bigger of the two as the overall number
   of sites represented by the dataset. Returns the sites' actual value'''
   
   if site_m.count(1) > site_f.count(1) :
      return getNum_sites(site_m)
   else:
       return getNum_sites(site_f)
    