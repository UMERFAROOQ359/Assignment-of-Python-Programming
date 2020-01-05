#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Advantages of OOP: It provides a clear modular structure for programs which makes it good for defining abstract datatypes 
  #  in which implementation details are hidden. Objects can also be reused within an across applications. 
   # The reuse of software also lowers the cost of development.


# In[2]:


# Advantages of OOP: It provides a clear modular structure for programs which makes it good for defining abstract 
#datatypes in which implementation details are hidden. Objects can also be reused within an across applications. 
#The reuse of software also lowers the cost of development.


# In[4]:


#A function is a piece of code that is called by name. It can be passed data to operate on (i.e. the parameters) and can optionally return data (the return value). All data that is passed to a function is explicitly passed.
#A method is a piece of code that is called by a name that is associated with an object.


# In[5]:


#Objects and Classes
#Object-oriented programming is modeled on how, in the real world, objects are often made up of many kinds of smaller objects. \
#This capability of combining objects, however, is only one very general aspect of object-oriented programming. 
#Object-oriented programming provides several other concepts and features to make creating and using objects easier 
#and more flexible, and the most important of these features is classes.
Attributes
Attributes are the individual things that differentiate one object from another and determine the appearance, 
state, or other qualities of that object. Let's create a theoretical class called Motorcycle. A motorcycle class
might include the following attributes and have these typical values:

Color: red, green, silver, brown
Style: cruiser, sport bike, standard
Make: Honda, BMW, Bultaco
    Behavior
A class's behavior determines how an instance of that class operates; for example, how it will "react" if asked to do something by another class or object or if its internal state changes. Behavior is the only way objects can do anything to themselves or have anything done to them. For example, to go back to the theoretical Motorcycle class, here are some behaviors that the Motorcycle class might have:

Start the engine
Stop the engine
Speed up
Change gear
Stall


# In[6]:


import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())


# In[ ]:




