#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user 
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")


# In[3]:


test_list = [ 1, 6, 3, 5, 3, 4 ] 
  
print("Checking if 4 exists in list ( using loop ) : ") 
  
# Checking if 4 exists in list  
# using loop 
for i in test_list: 
    if(i == 4) : 
        print ("Element Exists") 
  
print("Checking if 4 exists in list ( using in ) : ") 
  
# Checking if 4 exists in list  
# using in 
if (4 in test_list): 
    print ("Element Exists")


# In[4]:


d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


# In[5]:


def returnSum(myDict): 
      
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i] 
      
    return sum
  
# Driver Function 
dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :", returnSum(dict)) 


# In[1]:


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)


# In[ ]:




