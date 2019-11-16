#!/usr/bin/env python
# coding: utf-8

# In[1]:


sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")


# In[2]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[3]:


n = len([10, 20, 30]) 
print("The length of list is: ", n) 


# In[4]:


def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


# In[5]:


def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))


# In[7]:


test_list = [1,  1,  2,  3,  5,  8, 13, 21, 34, 55, 89] 
  
k = 4
    
print ("The list : " + str(test_list)) 
  
# using naive method  
# to get numbers > k 
count = 0
for i in test_list : 
    if i > k : 
        count = count + 1
        print ("The numbers less than 5 : " + str(count)) 


# In[ ]:




