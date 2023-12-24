#!/usr/bin/env python
# coding: utf-8

# ### data types

# #### data types

# ##### data types

# ## data types

# # data types

# In[2]:


x=10
type(x)


# In[3]:


x=10.5
type(x)


# In[4]:


x="nikita"
type(x)


# In[6]:


y=True
type(y)


# In[8]:


y="true"
type(y)


# In[9]:


## variables


# ## variables

# In[10]:


names="a","b"


# In[11]:


names="a","b"
names


# In[12]:


2names="a","b"
2names


# In[13]:


n2ames="a","b"
n2ames


# ##### variable name should not start with number

# In[15]:


names_list="A","B","C"
names_list


# ##### the only allowed special charcter is underscore

# In[17]:


name="nikita"
age=21
income=20000
print(name)
print(age)
print(income)


# ## list

# ##### elements in list are sepereted by comma and enclosed in square brackets
# ##### list is hetrogenous->multiple data types
# ##### list can have duplicates
# ##### list is mutable->make change

# In[19]:


sample_list=[1,2,3,4,-1,"hii",5]
sample_list


# In[20]:


type(sample_list)


# In[24]:


sample_list[4]


# In[25]:


sample_list[0]=100
sample_list


# In[1]:


book_list=["python","R","DS"]
print(book_list)
type(book_list)


# In[2]:


novels=["lord of ring","harry potter","esha"]
library=book_list+novels
library


# In[3]:


novels.append("jumanji")
novels


# ## TUPLES

# ##### 1)container object
# ##### 2)heterogenous->allow mutiple data types
# ##### 3)can have duplicates
# ##### 4)immutable->cannot make change
# ##### 5)elements are sepereted by commma,enclosed in parenthesis or withoutany brackets

# In[5]:


sample_tuples=(1,6,2,3,8,3,"hi")
sample_tuples


# In[7]:


type(sample_tuples)


# In[8]:


sample_tuples[1]


# ##### tuple is immutable->cannot make change

# In[11]:


sample_tuple2=1,2,34,6,7,"hii"
sample_tuple2


# In[12]:


type(sample_tuple2)


# In[13]:


print(sample_tuples)
print(sample_tuple2)


# In[15]:


sample_tuples[1]


# ## dictionary

# ##### key-value pair
# ##### {}
# ##### indexing-square bracket
# ##### mutable

# In[16]:


dict_1={'name':"arun","hobbies":["painting","playing","cooking"],1:23}
dict_1


# ## SET

# ##### set does not allow duplicates
# ##### we cannot retrive the set using index
# ##### set is mutable
# ##### set has {}
# ##### orderd-first place

# In[7]:


sample_set={1,2,3,4,5,6,7,8,"hii","ds","hello",-1,10.4,2,3,4,5}
sample_set


# In[10]:


sample_set.add(100)
sample_set


# In[ ]:




