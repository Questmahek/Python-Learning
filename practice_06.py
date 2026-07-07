#slicing#
#str[startindex:endindex:step] #ending idx is not included
#str="bahauddin science college"
#str[0:7] #bahaudi
#str[ :7] #is a same as [0:7]
#str[7: ] #is a same as [7:len(str)]

str="bahauddin science college"
print(str[0:7]) 
print(str[0:len(str)]) 

#slicing ,negative indexing
#str="apple"
#str[-3:-1] #'pl'

str="bahauddin science college"
print(str[-3:-1])   
