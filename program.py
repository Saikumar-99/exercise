#!/usr/bin/env python
# coding: utf-8

# In[59]:


dict={}


# In[60]:


def create(key,value):
    if key in dict:
        print("error-key already exists")
    else:
        if(key.isalpha()):
            if len(key)<=32:
                dict[key]=value
            else:
                print("error-value should be less than 32characters")
        else:
            print("error-Invalid key..key should be in characters")


# In[61]:


def read(key):
    if key not in dict:
        s="error-key not exist..Enter a valid key"
    else:
        b=dict[key]
        s=str(key)+":"+str(dict[key])
    return s


# In[62]:


def delete(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=dict[key]
        del dict[key]
        print("key is successfully deleted")


# In[63]:


def change(key,value):
    b=dict[key]
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        dict.update({key:value})


# In[64]:


create("sai",30)


# In[65]:


create("kumar",60)


# In[66]:


read("sai")


# In[67]:


read("ram")


# In[68]:


create("sai",50)


# In[69]:


change("sai",55)


# In[70]:


read("sai")


# In[71]:


delete("sai")


# In[72]:


print(dict)


# In[ ]:




