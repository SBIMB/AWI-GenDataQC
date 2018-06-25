import pandas as pd
import numpy 
import matplotlib as mpl

data_field1 = pd.read_csv("/Users/taliya/Desktop/AWI-GEN/AWI-GenDataQC/Test Data.csv")
column_Names =list( data_field1)
column_access = data_field1[column_Names[4]]  #eventually put this into a loop with each column being accessed 



def missing(data):
     return sum(data.isnull())
 
 
def sig_missing(list_val):
    
    s =list_val.size
   
    for i in range(s):
        if list_val[i] > 0.0:
            print(str(list_val.index[i])+ "\t\t\t".rjust(9) + str(list_val[i]) )
            
             

data_missing=data_field1.apply(missing, axis=0) #axis=0 defines that function is to be applied on each colum
print ("Missing values per column:")
print()
sig_missing(data_missing)

#def outliers(val1, val2):









#print(column_access)



#def missing(col):
   # missing_data =()
  #  for element in range(0,5):
    #    if col[element]== "NaN":
    #        missing_data = missing_data + 3
            
    
   # return missing_data

#def missing(col):
   # missing_data =[0]
    #for element in range(0,8):
       #if col[int(element)].isnull():
           #print("empty")
           #missing_data = missing_data + 5
            
    
    #return missing_data