#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Thread, Runnable, run()
# Process : 현재 실행 중인 프로그램
# Process 안에서 동시에 실행 가능한 소규모 Process


# In[2]:


# 함수, 메소드, run()


# In[3]:


import threading
import time
import datetime


# In[4]:


def t1(name):
    while True:
        print(name, datetime.datetime.now())
        time.sleep(1)


# In[5]:


t1('sangyeol babo')


# In[ ]:


def t2(name):
    i = 0
    while True:
        i += 1
        print(name, i)
        time.sleep(1)


# In[ ]:


t2('handsome sy')


# In[ ]:


# 객체의 멤버 메소드를 쓰레드의 타겟으로 설정하는 예
th1 = threading.Thread(target=t1, args=('name',))
th1.daemon = True
th1.start()

th2 = threading.Thread(target=t2, args=('name',))
th2.daemon = True
th2.start()


# In[ ]:


import threading
import datetime
import time

# 가상의 CPU 역할을 하는 클래스 정의
class MyGame (threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        print(name, 'instanciated')
        self.daemon = True
    def run(self):
        while True:
            print(datetime.datetime.now())
            time.sleep(1)
my_thread = MyGame('game thread')
my_thread.start()


# In[10]:


def t3(name, i):
    while True:
        i -= 1
        print(name, i)
        time.sleep(1)
        if i == 0:
            print(name, '종료되었습니다.')
            break
            
def t4(name, i):
    while True:
        i -= 1
        print(name, i)
        time.sleep(1)
        if i == 0:
            print(name, '종료되었습니다.')
            break


# In[13]:


a = int(input('t3 숫자를 입력해주세요.'))
th3 = threading.Thread(target=t3, args=('t3',a))
th3.daemon = True
th3.start()

b= int(input('t4 숫자를 입력해주세요.'))
th4 = threading.Thread(target=t4, args=('t4',b))
th4.daemon = True
th4.start()


# In[ ]:




