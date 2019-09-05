## 1. Interfering with the Built-in Functions ##

def max(a_list):
    a_string="No max value returned"
    return a_string

a_list = [1, 8, 10, 9, 7]
print(max(a_list))
max_val_test_0=max(a_list)
print(max_val_test_0)

del max
print(max(a_list))



## 3. Default Arguments ##

# INITIAL CODE
def open_dataset(file_name='AppleStore.csv'):
    
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    return data

apps_data=open_dataset()
print(apps_data[1:5])

## 4. The Official Python Documentation ##

one_decimal=round(3.43,1)
two_decimals=round(0.23321,2)
five_decimals=round(921.2225227,5)

## 5. Multiple Return Statements ##

# INITIAL CODE
def open_dataset(file_name='AppleStore.csv',header_exist=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    if header_exist:
        return data[1:]
    else:
        return data
    
apps_data=open_dataset('AppleStore.csv')
print(apps_data)

## 6. Returning Multiple Variables ##

# INITIAL CODE
def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0], data[1:]  #data[0]is the header
    else:
        return data
        
all_data=open_dataset("AppleStore.csv")
header=list(all_data[0])
apps_data=list(all_data[1])
print(header)
print(apps_data)

## 7. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
apps_data,header=open_dataset("AppleStore.csv")

## 8. Functions — Code Running Quirks ##

def print_constant():
    x=3.14
    print(x)
    
print_constant()
print(x)

## 9. Scopes — Global and Local ##

e = 'mathematical constant'
a_sum = 1000
length = 50

def exponential(x):
    e=2.72
    print(e)
    return e**x

def divide():
    print(a_sum)
    print(length)
    return a_sum/length #should be wrong because of type 

result=exponential(5)
print(result)
result_2=divide()
print(result_2)