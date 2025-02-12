
global_var = 5

def my_function():
    local_var = 7
    print("Inside function:")
    print(local_var ,"is a local variable")  
    print(global_var, "is a globle variable")  
my_function()
print("Outside function:")
print(global_var)



