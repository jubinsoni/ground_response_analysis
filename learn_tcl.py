import os


#in init list we will store input from user
init = [1000,5.0e-2,3,5.0e2,6.759,6.0,6.01]

args_init = []

args_init=['{:.3f}'.format(x) for x in init]
    



args = "" 
for i in range(len(args_init)):
    args = args +" " + args_init[i]
    
    
    
str_1 = "opensees learn_tcl.tcl"

str_1 = str_1 + " " + args 
os.system(str_1)

file = open('sample.txt', 'r') 
print file.read() 
file.close()