#!/usr/bin/env python
# coding: utf-8

# # Declaring a tuple

# In[14]:


tpl = ("My", "name", "is", "Chitrakshi", "Gosain", ".")
tpl1 = (1, 2, [3, 4], {5, 6, 5})


# # Implementing various methods of 'Tuple' object

# # -> Count

# In[15]:


# Returns the number of times the specified element appears in the tuple
# Syntax: tuple.count(element)
# 'element' - the element to be counted
# This method returns the number of times 'element' appears in the tuple
# This method returns 0 for non-existing elements


# In[16]:


tpl.count("My")


# In[17]:


tpl.count(">")


# In[18]:


tpl1.count({5, 6, 5})


# In[19]:


tpl1.count([3, 4])


# # -> Index

# In[20]:


# Returns the index of the specified element in the tuple
# Syntax: tuple.index(element, start, end)
# 'element' - the element to be searched
# 'start' (optional) - start searching from this index
# 'end' (optional) - search the element up to this index
# This method returns the index of the first occurenece of the given element in the tuple
# This method returns a 'ValueError' exception for non-existing elements


# In[21]:


tpl.index("My")


# In[22]:


tpl.index(".")


# In[23]:


tpl.index(">")


# In[24]:


tpl1.index({5, 6, 5})


# In[25]:


tpl1.index([3, 4])

