#!/usr/bin/env python
# coding: utf-8

# In[1]:


# mysql
import pymysql


# In[2]:


from User import User


# In[3]:


from UserDAO import UserDAO


# In[ ]:


while True:
    print('-----------------------------------------------')
    print('목록(s) 추가(a) 검색(f) 수정(u) 삭제(d) 종료(x)')
    userChoice = input('사용하실 기능을 입력해주세요 : ')
    if userChoice.upper() == 'S':     
        UserDAO.UserList()
    elif userChoice.upper() == 'A':
        while True:
            uid, phone, email = input('추가하실 사원의 아이디, 전화번호, 이메일을 입력해주세요.').strip().split()
            print(uid, phone, email)
            if UserDAO.UserDuplicateinspection(uid):
                UserDAO.UserInput(UserDAO.GetUserNum(), uid, phone, email)
                break
            else:
                UserDAO.UserList()
                
    elif userChoice.upper() == 'F':
        uid = input('검색 할 uid 또는 사원 번호를 입력해주세요.').strip()
        UserDAO.FindUser(uid)
        
    elif userChoice.upper() == 'U':
        uid = input('수정 할 uid를 입력해주세요.').strip()
        print(UserDAO.FindUser(uid))
        if UserDAO.FindUser(uid):
            phone, email = input ('수정 할 전화번호와 이메일을 입력하세요.').strip().split()        
            UserDAO.EditUser(uid, phone, email)
            
    elif userChoice.upper() == 'D':
         num = int(input('삭제하실 사원의 번호를 입력해주세요.').strip())
         UserDAO.DelUser(num)
        
    elif userChoice.upper() == 'X':          
        print('종료되었습니다.')
        break
                       
    else: print('메뉴 입력 오류입니다.')


# In[1]:


GetUserNum()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




