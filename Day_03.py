#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Collection
#- list, tuple, dictionary, set
#- list : 순서유지, 중복허용
#- tuple : 순서유지, 중복허용, 수정/삭제 안됨
#- dictionary : key, value가 쌍으로 저장
#- set : 중복불허


# In[ ]:


# 프로그램이 시작되면, 아래처럼 메뉴 목록을 제시한다.
# 추가(a), 검색(f), 목록(s), 수정(u), 삭제(d), 종료(x):
# 추가는 사원의 번호 이름 전화를 입력 받음
# 한 개의 기능을 수행한 후에는 다시 원래의 메뉴 목록이 표시
# 사원 정보는 keycode
# 검색은 이름으로 검색, 대소문자 구분 없이 검색된 사원 정보가 화면에 표시된다.
emp = []
empno = []


# In[13]:


while True:
    print()
    userinput = input("추가(a), 검색(f), 목록(s), 수정(u), 삭제(d), 종료(x):")
    if userinput == 'a':
            while True:
                (num, name, phone) = input('번호, 이름, 전화').split()
                empno.append(num)                
                if len(list(empno)) == len(set(empno)):
                    emp.append({'num':num, 'name':name, 'phone':phone})
                    if len(list(emp)) > 0:
                        for e in emp:
                            print(f"{e['num']}\t{e['name']}\t{e['phone']}")
                    else:  print(f"{'num':num, 'name':name, 'phone':phone}")        
                    break
                else:
                    empno.remove(num)
                    print('중복된 번호를 입력하셨습니다. 다시 입력해주세요.')
                    print()
            continue
            
    elif userinput == 'f':
        want = input('찾으실 회원이름을 입력해주세요.')
        notfind = True        
        for e in emp:
            if e['name'].upper() == want.upper():
                print(f"{e['num']}\t{e['name']}\t{e['phone']}")
                notfind = False
        if notfind:
            print('찾으시는 회원번호는 존재하지 않습니다.')
                
    elif userinput == 's':
         print(f"'번호'\t'이름'\t'전화'")
         for e in emp:
            print(f"{e['num']}\t{e['name']}\t{e['phone']}")
         continue    
        
    elif userinput == 'u':
        want = input('수정할 회원번호를 입력해주세요.')
        notfind = True        
        for e in emp:
            if e['num'] == want:
                print('현재 회원 정보입니다')
                print(f"{e['num']}\t{e['name']}\t{e['phone']}")
                (name, phone) = input('수정 할 이름, 번호를 입력해주세요.').split()
                e['name'] = name
                e['phone'] = phone
                print(f"{e['num']}\t{e['name']}\t{e['phone']}")
                notfind = False
        if notfind:
            print('찾으시는 회원 번호가 없습니다.')
        continue
        
    elif userinput == 'd':
        want = input('삭제할 회원번호를 입력해주세요.')
        notfind = True
        for e in emp:
            if e['num'] == want:
                notfind = False
                print('정말 삭제하시겠습니까?')
                a = input("정말 삭제하시려면 '삭제'를 입력해주세요.")
                if a == '삭제':
                    emp.remove(e)
                    print('삭제되었습니다.')
        if notfind:
            print('찾으시는 회원 번호가 없습니다.')
        continue      
 
    elif userinput == 'x':
        print("프로그램이 종료되었습니다.")
        break


# In[ ]:


# 중복인지 아닌지를 검사해서 그 결과를 리턴하는 함수 작성

def is_duplicate_name(name):
    for e in emp:
        if e['name'] == name:
            return True
    return False

def is_duplicate_num(num):
    for e in emp:
        if e['num'] == num:
            return True
    return False

def is_duplicate_phone(phone):
    for e in emp:
        if e['phone'] == phone:
            return True
    return False


# In[ ]:


# 목록보기 함수

def emp_list():
    for e in emp:
        print(f"{e['num']}\t{e['name']}\t{e['phone']}")


# In[ ]:


# 검색기능 : 이름을 파라미터로 받아서 해당 사원의 정보를 검색하고 리턴한다.
# - 검색결과가 없는 경우에는 None을 리턴

def find_emp_name(name):
    for e in emp:
        if e['name'] == name:
            return print(f"{e['num']}\t{e['name']}\t{e['phone']}")
    return print('찾으시는 회원정보가 없습니다.') 
    # return None   
    
def find_emp_num(num):
    for e in emp:
        if e['num'] == num:
            return True
    return False

def find_emp_phone(phone):
    for e in emp:
        if e['phone'] == phone:
            return print(f"{e['num']}\t{e['name']}\t{e['phone']}")
    return print('찾으시는 회원정보가 없습니다.') 
        


# In[14]:


# 수정기능
def update_emp(num, name, phone):
    for e in emp:
            if e['num'] == num:
                e['name'] = name
                e['phone'] = phone
                print(f"{e['num']}\t{e['name']}\t{e['phone']}")
                return True
    return False 

def update_emp_teacher(new_phone):
    num, name, phone = new_phone
    updated = False
    for e in emp:
        if e['num'] == num:
                e['name'] = name
                e['phone'] = phone
                updated = True
    return updated        
        


# In[15]:


# 삭제 기능
def delete_emp(num):
    del_emp = False
    for e in emp:
        if e['num'] == num:
            print('정말 삭제하시겠습니까?')
            a = input("정말 삭제하시려면 '삭제'를 입력해주세요.")
            if a == '삭제':
                emp.remove(e)
                del_emp = True
                print('삭제되었습니다.')
    if del_emp == False:
        print('찾으시는 회원 번호가 없습니다')


# In[16]:


# 함수 적용

while True:
    print()
    userinput = input("추가(a), 검색(f), 목록(s), 수정(u), 삭제(d), 종료(x):")
    if userinput == 'a':
            while True:
                (num, name, phone) = input('번호, 이름, 전화').split()               
                if is_duplicate_num(num) != True:
                    emp.append({'num':num, 'name':name, 'phone':phone})
                    print('입력 성공') 
                    break
                else:
                    empno.remove(num)
                    print('중복된 번호를 입력하셨습니다. 다시 입력해주세요.')
                    print()
            continue
            
    elif userinput == 'f':
        want = input('찾으실 회원이름을 입력해주세요.')
        find_emp_name(want)
        continue 
        
    elif userinput == 's':
         print(f"'번호'\t'이름'\t'전화'")
         emp_list()
         continue    
        
    elif userinput == 'u':
        want = input('수정할 회원번호를 입력해주세요.')
        notfind = True
        if find_emp_num(want):
            (name, phone) = input('수정 할 이름, 번호를 입력해주세요.').split()
            update_emp(want, name, phone)
        else:
            print('찾으시는 회원 번호가 없습니다.')
        continue
        
    elif userinput == 'd':
        want = input('삭제할 회원번호를 입력해주세요.')
        delete_emp(want)
        continue      
 
    elif userinput == 'x':
        print("프로그램이 종료되었습니다.")
        break


# In[17]:


import pizza

pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# In[18]:


import mymodule as mm

mm.show('Smith', 'Ward', 'King')


# In[ ]:





# # 클래스 실습
# * 클래스와 인스턴스
# * 초기자, _init_()
# * 인스턴스 메소드 : 인스턴스에 포함된 메소드

# In[20]:


class Emp:
    def __init__(self, num, name, phone): #self=java의 this
        self.num = num
        self.name = name
        self.phone = phone
        
    def __str__(self): #자바의 tostring
        return f"{self.num}\t{self.name}\t{self.phone}"
    
    def __eq__(self, other):
        return self.num == other.num
    
    def edit(self, name, phone):
        self.name = name
        self.phone = phone


# In[21]:


e1 = Emp('11', 'Smith', '010-3547-6510')
print(e1)

e2 = Emp( '12', 'Blake', '010-3271-1290')
print(e2)


# In[22]:


emp_list = [e1, e2]
for e in emp_list:
    print(e)


# In[ ]:


while True:
    print()
    userinput = input("추가(a), 검색(f), 목록(s), 수정(u), 삭제(d), 종료(x):")
    if userinput == 'a':
            while True:
                (num, name, phone) = input('번호, 이름, 전화').split()
                e = Emp(num, name, phone)
                if duplicate_list(e) == False:
                    emp_list.append(e)
                    print('입력 성공') 
                    break
                else:
                    print('중복된 번호를 입력하셨습니다. 다시 입력해주세요.')
                    print()
            continue
            
    elif userinput == 'f':
        want = input('찾으실 회원번호를 입력해주세요.')
        serch_list(want)            
        continue 
        
    elif userinput == 's':
         print(f"'번호'\t'이름'\t'전화'")
         show_list()
         continue    
        
    elif userinput == 'u':
        want = input('수정할 회원번호를 입력해주세요.')
        e = serch_list(want)
        if e is not None:
            (name, phone) = input('수정 할 이름, 번호를 입력해주세요.').split()
            e.edit(name, phone)
        continue
        
    elif userinput == 'd':
        want = input('삭제할 회원번호를 입력해주세요.')
        del_emp(want)
        continue      
 
    elif userinput == 'x':
        print("프로그램이 종료되었습니다.")
        break


# In[33]:


# 중복검사
def duplicate_list(en):
    for e in emp_list:
        if e.name == en.name:
            return True
        if e.num == en.num:
            return True
    return False  

# 목록보기
def show_list():
    for e in emp_list:
        print(e)
        
# 검색
def serch_list(num):
    find = False
    for e in emp_list:
        if e.num == num :
            find = True
            print(e)
            return e
    if find == False:
        print('일치하는 회원이 없습니다.')
        return None

            
# 삭제
def del_emp(en):
    find = False
    for e in emp_list:
        if e.num == en:
            find = True
            emp_list.remove(e)
            print('삭제에 성공했습니다.')            
    if find == False:
        print('일치하는 회원이 없습니다.')


# In[25]:


e2.__eq__(e1)
e2 == e1


# In[ ]:




