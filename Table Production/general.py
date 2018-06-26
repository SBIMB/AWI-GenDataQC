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

    
    

