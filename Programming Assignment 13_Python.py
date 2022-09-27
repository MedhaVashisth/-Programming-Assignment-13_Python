#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)

print(result_list)


# In[2]:


row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)


# In[4]:


phrase = input("Input words: ")

phrase_list = phrase.split(",")
phrase_list.sort()
print((', ').join(phrase_list))


# In[5]:


phrase = input("Type in: ")
phrase_splited = phrase.split(' ')

word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))


# In[6]:


phrase = input("Type in: ")
phrase = list(phrase)

l, d = 0, 0
for i in phrase:
    if i.isalpha():
        l = l + 1
    if i.isdigit():
        d = d + 1
    else:
        pass

print("Letters:", l)
print("Digits:", d)


# In[9]:


import re

passwords = input("Type in: ")
passwords = passwords.split(",")

accepted_pass = []
for i in passwords:
    
    if len(i) < 6 or len(i) > 12:
        continue

    elif not re.search("([a-z])+", i):
        continue

    elif not re.search("([A-Z])+", i):
        continue

    elif not re.search("([0-9])+", i):
        continue

    elif not re.search("([!@$%^&])+", i):
        continue

    else:
        accepted_pass.append(i)

print((" ").join(accepted_pass))


# In[ ]:




