#!/usr/bin/env python
# coding: utf-8

# In[7]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


# In[8]:


def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


# In[9]:


# Python program to print Even Numbers in a List 
  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93] 
num = 0
  
# using while loop         
while(num < len(list1)): 
      
    # checking condition 
    if num % 2 == 0: 
       print(list1[num], end = " ") 
      
    # increment num   
    num += 1


# In[10]:


def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('aza')) 


# In[11]:


def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(9))


# In[12]:


# This loop will go on until the budget is integer or float 
while True: 
	try: 
		bg = float(input("Enter your budget : ")) 
		# if budget is integer or float it will be stored 
		# temporarily in variable 's' 
		s = bg 
	except ValueError: 
		print("PRINT NUMBER AS A AMOUNT") 
		continue
	else: 
		break

# dictionary to store product("name"), quantity("quant"), 
# price("price") with empty list as their values 
a ={"name":[], "quant":[], "price":[]} 

# converting dictionary to list for further updation 
b = list(a.values()) 

# variable na value of "name" from dictionary 'a' 
na = b[0] 

# variable qu value of "quant" from dictionary 'a' 
qu = b[1] 

# variable pr value of "price" from dictionary 'a' 
pr = b[2] 

# This loop terminates when user select 2.EXIT option when asked 
# in try it will ask user for an option as an integer (1 or 2) 
# if correct then proceed else continue asking options 
while True: 
	try: 
		ch = int(input("1.ADD\n2.EXIT\nEnter your choice : ")) 
	except ValueError: 
		print("\nERROR: Choose only digits from the given option") 
		continue
	else: 
		# check the budget is greater than zero and option selected 
		# by user is 1 i.e. to add an item 
		if ch == 1 and s>0:	 

			# input products name				 
			pn = input("Enter product name : ") 
			# input quantity of product 
			q = input("Enter quantity : ") 
			# input price of the product 
			p = float(input("Enter price of the product : ")) 

			if p>s: 
				# checks if price is less than budget 
				print("\nCAN, T BUT THE PRODUCT") 
				continue

			else: 
				# checks if product name already in list 
				if pn in na: 
					# find the index of that product 
					ind = na.index(pn) 

					# remove quantity from "quant" index of the product 
					qu.remove(qu[ind]) 

					# remove price from "price" index of the product 
					pr.remove(pr[ind]) 

					# insert new value given by user earlier 
					qu.insert(ind, q) 

					# insert new value given by user earlier 
					pr.insert(ind, p) 

					# subtracting the price from the budget and assign 
					# it to 's' sum(pr) is because pr = [100, 200] if 
					# budget is 500 then s = bg-sum(pr) = 200 
					# after updating for same product at index 0 let 
					# pr = [200, 200] so s = 100 
					s = bg-sum(pr) 

					print("\namount left", s) 
				else: 
					# append value of in "name", "quantity", "price" 
					na.append(pn) 

					# as na = b[0] it will append all the value in the 
					# list eg: "name":["rice"] 
					qu.append(q) 

					# same for quantity and price 
					pr.append(p)	 

					# after appending new value the sum in price 
					# as to be calculated 
					s = bg-sum(pr) 

					print("\namount left", s) 

		# if budget goes zero print "NO BUDGET" 
		elif s<= 0: 
			print("\nNO BUDGET") 
		else: 
			break

# will print amount left in variable 's' 
print("\nAmount left : Rs.", s) 

# if the amount left equals to any amount in price list 
if s in pr: 
	# then printing the name of the product which can buy 
	print("\nAmount left can buy you a", na[pr.index(s)]) 

print("\n\n\nGROCERY LIST") 

# print final grocery list 
for i in range(len(na)): 
	print(na[i], qu[i], pr[i]) 


# In[ ]:




