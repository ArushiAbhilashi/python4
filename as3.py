#!/usr/bin/env python
# coding: utf-8

# # finding index of a substring 

# In[22]:


str1="what we think,we become; we are python programmers"
index=0
while(index<len(str1)):
    index=str1.find("we",index)
    if index == -1:
            break
    print('we found at', index)
    index += 2 #length of "we" is 2
    


# # islower() and isupper() functions:- 

# In[24]:


a="string"
print(a.isupper())


# In[31]:


b="string"
print(b.islower())


# In[ ]:


c="strING"
print(c.isupper())


# In[32]:


a="we123"
print(a.islower())


# In[33]:


x="123we"
print(x.islower())


# In[28]:


y=DYT**@#$
print(y.islower()) #doesnt work for special characters.


# In[29]:


num=123
print(num.islower())


# In[30]:


q = get_ipython().getoutput('@@#%$%$')
print(q.isupper())


# islower() and isupper() functions are valid only for strings and alphanumeric values but not for numbers and special characters





