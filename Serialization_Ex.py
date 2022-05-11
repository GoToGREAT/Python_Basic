#!/usr/bin/env python
# coding: utf-8

# pickle 모듈을 이용한 직렬화/역직렬화

# In[1]:


from emp import Emp


# In[2]:


import pickle


# In[3]:


emp = Emp(11, 'smith', '010-2394-5410')


# In[ ]:





# 객체 직렬화(Object Serialization)

# In[4]:


fw = open('empObj.pickle', 'wb')
pickle.dump(emp, fw)
fw.close()
print('객체 직렬화 성공')


# In[ ]:





# 역직렬화(De-Serialization)

# In[5]:


fr = open('empObj.pickle', 'rb')
emp2 = pickle.load(fr)
fr.close()
for e in emps:
    print(e)


# In[ ]:


emp==emp2


# In[ ]:


emplist = [Emp(11), Emp(12), Emp (13)]


# In[ ]:


fw = open('emplist.pickle', 'wb')
pickle.dump(emplist, fw)
fw.close()
print("리스트 직렬화 완료")


# In[ ]:


fr = open('emplist.pickle', 'rb')
emps = pickle.load(fr)
fr.close()

for e in emps:
    print(e)
print("리스트 역직렬화 성공")


# In[ ]:


# 객체 > 텍스트 파일, 텍스트 > 객체 매핑
# 객체 > 객체, 객체 > 객체


# In[ ]:





# In[ ]:


# 프로그램이 시작되면 메뉴 6개가 표시된다
# 목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x)
# 추가하고 목록보기가 되도록 기능을 작성해보세요.


# In[ ]:


while True:
    print('-----------------------------------------------')
    print('목록(s) 추가(a) 검색(f) 수정(u) 삭제(d) 종료(x)')
    select = input('이용하실 기능을 선택해주세요.')
    if select.upper() == 'S':
        show_list()
        
    elif select.upper() == 'A':
        while True:
            num, name, phone = input('추가하실 사원의 번호, 이름, 전화번호를 입력해주세요.').strip().split()
            if input_emp(num, name, phone):
                show_list()
                break
            else: show_list()
        
    elif select.upper() == 'D':
         num = input('삭제하실 사원의 번호를 입력해주세요.').strip()
         del_emp(num)
            
    elif select.upper() == 'F':
         num = input('찾으실 회원의 번호를 입력해주세요.').strip()
         serch_emp(num) 
        
    elif select.upper() == 'U':
         num = input('수정할 회원의 번호를 입력해주세요.').strip()
         edit_emp(num)       
        
    elif select.upper() == 'X':
        print('종료되었습니다.')
        break
    else: print('메뉴 입력 오류입니다.')     
          
          


# In[ ]:


def show_list():
    fr = open('emplist.pickle', 'rb')
    emps = pickle.load(fr)
    fr.close()
    for e in emps:        
        print(e)


# In[ ]:


def input_emp(num, name, phone):
    overlap = False
    emp = Emp(num, name, phone)
    
    fr = open('emplist.pickle', 'rb')
    emps = pickle.load(fr)
    fr.close()
    
    if emp in emps:
        ovarlap = True
        print('중복된 번호를 입력하셨습니다.')
        return False
    
    if overlap == False:
        emps.append(emp)
        fw = open('emplist.pickle', 'wb')
        pickle.dump(emps, fw)
        fw.close()
        print('입력 성공했습니다.')
        return True
    


# In[ ]:


def serch_emp(num):
    emp = Emp(num)
    find = False
    
    fr = open('emplist.pickle', 'rb')
    emps = pickle.load(fr)
    fr.close()
    
    if emp in emps:
        find = True
        print(emps[emps.index(emp)])
        
    if find==False:
        print('입력하신 번호의 회원이 없습니다.')
    


# In[ ]:


def del_emp(num):
    emp = Emp(num)
    delete = False
    
    fr = open('emplist.pickle', 'rb')
    emps = pickle.load(fr)
    fr.close()
    
    if emp in emps:
        emps.remove(emp)
        fw = open('emplist.pickle', 'wb')
        pickle.dump(emps, fw)
        fw.close()
        delete = True
        print('회원을 삭제했습니다.')
    if delete == False:
        print('입력하신 번호의 회원이 없습니다.')


# In[ ]:


def edit_emp(num):
    emp = Emp(num)
    edit = False
    
    fr = open('emplist.pickle', 'rb')
    emps = pickle.load(fr)
    fr.close()
    
    if emp in emps:
        phone = input('수정하실 전화번호를 입력해주세요.')
        emps[emps.index(emp)].phone = phone
        fw = open('emplist.pickle', 'wb')
        pickle.dump(emps, fw)
        fw.close()
        edit = True
        print('회원을 수정했습니다.')
    if edit == False:
        print('입력하신 번호의 회원이 없습니다.')


# In[ ]:


elist.sort(key==lamda e : e.num)
for e in elist:
    print(e)


# In[ ]:


nums = [3,5,1,4,2]
print(sorted(nums))
print(nums.sort())
print(nums)


# In[ ]:


members.sort(key=lambda e: e.name)


# In[ ]:


for e in members:
    print(e)


# In[ ]:


members.sort(key=lambda e: e.num)


# In[ ]:


byte_arr = pickle.dumps(emplist)
print(byte_arr)


# In[ ]:


strload = pickle.loads(byte_arr)
for e in strload:
    print(e)


# In[ ]:


numbers = [1,10,2,3,4,5]
numbers.sort()
print(numbers)


# In[ ]:


outer_num = 100


# In[ ]:


def value_use():
    print(outer_num+10)


# In[ ]:


value_use()


# In[ ]:


def value_change():
    outer_num = 10
    print(outer_num)
# 파이썬에서 함수 내부에 있는 변수는 지역변수이다.
# 단 선언하지 않은 변수에 대해서(변수 = 10)는 변역변수라고 인식


# In[ ]:


value_change()


# In[ ]:


print(outer_num)


# In[ ]:


def value_change1():
    global outer_num
    outer_num = 10
    print(outer_num)
# global로 인해 함수 내부 변수이지만 변역변수로 바뀜.


# In[ ]:


value_change1()


# In[ ]:


print(outer_num)


# In[ ]:


def print_num():
    print(outer_num)


# In[ ]:


print_num()

