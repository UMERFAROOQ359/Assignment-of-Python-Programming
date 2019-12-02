#!/usr/bin/env python
# coding: utf-8

# In[8]:


person = {
  "first_name": "UMER",
  "last_name": "FAROOQ",
  "age": 26,
  "city": "KARACHI"
}
person.update({"QUALIFICATION": "GRADUATE"})
print(person)


# In[9]:


person = {
  "first_name": "UMER",
  "last_name": "FAROOQ",
  "age": 26,
  "city": "KARACHI"
}
person.update({"QUALIFICATION": "GRADUATE"})
del person["QUALIFICATION"]
print(person)


# In[10]:


cities = {
    'KARACHI': {
        'country': 'PAKSITAN',
        'population': 18,891,076,
        'fact': 'economy',
        },
    'ISLAMABAD': {
        'country': 'PAKISTAN',
        'population': 1,009,832,
        'fact': 'CAPITAL',
        },
    'LAHORE': {
        'country': 'PAKISTAN',
        'population': 11,126,285,
        'fact': 'niceplace',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['fact'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + city + " fact.")


# In[13]:


cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")


# In[14]:


prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")


# In[15]:


def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(title + " is one of my favorite books.")

favorite_book('The Abstract Wild')


# In[ ]:


import random
target_num, guess_num = random.randint(1, 30), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 30 until you get it right : '))
print('Well guessed!')

