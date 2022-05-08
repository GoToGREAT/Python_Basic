#!/usr/bin/env python
# coding: utf-8

# In[11]:


from emp import Emp


# In[12]:


e1 = Emp('11', 'Smith', '010-3547-6510')
print(e1)

e2 = Emp( '12', 'Blake', '010-3271-1290')
print(e2)


# In[104]:


import random
random.randint(1,10)


# # 파일 다루기

# In[118]:


fstream = open('emp.py', mode = 'r', encoding='utf-8')
data = fstream.read()
print(data)
fstream.close()

# open-close 동시에 하기 // 개발자의 기본


# In[114]:


with open('emp.py', mode='r', encoding='utf-8') as fstream:
    data = fstream.read()
    print(data)


# In[ ]:




