#!/usr/bin/env python
# coding: utf-8

# In[1]:


#-*- coding: utf-8 -*-  #동작 안함.


# # 파일 다루기
# 1. 파일 열기 : open()
# 2. CRUD      : read, write, readlines
# 3. 파일 닫기 : close()
# 

# In[14]:


open('emp.py', 'r') # 열리긴하지만 리턴이 없음. / r = '읽기 모드'


# In[15]:


fobj = open('emp.py', 'r')
print(type(fobj)) # io.TextIOWrapper
print(dir(fobj))  # leterator, __next__, 반복문에 적용 가능
fobj.close()


# In[16]:


fobj = open('emp.py', 'r', encoding='UTF-8') # 한글 주석으로 인코딩 필요
for data in fobj:
    print(data)
fobj.close()


# In[1]:


fobj = open('emp.py', 'r', encoding='UTF-8')
for data in fobj:
    print(data, end="")
fobj.close()


# In[2]:


fobj = open('emp.py', 'r', encoding='UTF-8')
for data in fobj:
    print(data.rstrip()) #끝 빈칸 없애기
fobj.close()


# In[4]:


from collections.abc import Iterable, Iterator

nums = [1,2,3]
dir(nums)
# dir(fobj)에서 보인 __next__가 없다.

isinstance(nums, Iterable) # True, __getitem__()

nums.__iter__()

isinstance(nums, Iterator)   # False


# In[5]:


print(nums.__getitem__(0))
print(nums[0])


# In[23]:


itr = nums.__iter__()

isinstance(itr, Iterator)   # True


# In[25]:


# nums.__iter__()
iter(nums)


# In[26]:


isinstance(fobj, Iterable)   # True
isinstance(fobj, Iterator)   # True


# In[7]:


fobj = open('emp.py', 'r', encoding='UTF-8')
fdata = fobj.read()
type(fdata)   #  str


# In[29]:


fobj = open('emp.py', 'r', encoding='UTF-8')
datalist = fobj.readlines()
type(datalist)  # list

for line in datalist:
    print(line.rstrip())
    
fobj.close()


# In[8]:


fobj = open('emp.py', 'r', encoding='UTF-8')
print(fobj.__next__().rstrip()) # 한 줄씩 읽는 방법
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
print(fobj.__next__().rstrip())
fobj.close()


# In[9]:


fobj = open('emp.py', 'r', encoding='UTF-8')
#fobj.__next__()
print(next(fobj).rstrip()) # 한 줄씩 읽는 방법
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
print(next(fobj).rstrip())
fobj.close()


# In[25]:


with open('emp.py', 'r', encoding='UTF-8') as fobj:
    for line in fobj:
        print(line.rstrip())
        
print(type(line)) # str
print(line) # 1줄만 나옴


# In[24]:


def show_list(emps):
    for emp in emps:
        print(emp)


# In[52]:


emplist = []

def show_emplist():
    from emp import Emp
    fobj = open('emps.txt', 'r')    
    for data in fobj:
        list =  data.strip().split()
        emplist.append(Emp(list[0], list[1], list[2]))
    fobj.close()
    for e in emplist:
        print(e)


# In[53]:


show_emplist () # emplist 생성


# In[54]:


for e in emplist:
    print(e)


# In[48]:


# 파일에 한 행 추가
fobj = open('emps.txt', 'w') # w : 쓰기 모드  // 기존 파일 정보 날려버리고 작성
fobj.write("11 King 010-2147-5201\n")
fobj.write("12 Suzan 010-3697-2145\n")
fobj.write("13 Blake 010-8520-1250\n")
fobj.write("14 Hello 010-1234-5678\n")
fobj.close()


# In[59]:


from emp import Emp

def load_emps():
    emps = []
    with open('emps.txt', 'r') as fobj:
        for line in fobj:
            num,name,phone = line.strip().split()
            emps.append( Emp(num,name=name,phone=phone) )
    return emps


# In[60]:


def save_emp(emp):
    line = "{} {} {}".format(emp.num, emp.name, emp.phone)
    with open('emps.txt', 'a') as fobj:
        fobj.write(line + '\n')


# In[61]:


show_list(load_emps())


# In[62]:


# 키보드에서 num,name,phone 을 입력받아서 emps.txt 에 한 행으로 추가
# 목록보기 기능을 실행하면 추가된 정보가 표시되어야 함
num,name,phone = input('번호 이름 전화:').strip().split()  # 키보드에서 한 사원정보를 입력 받는다
save_emp(Emp(num,name=name,phone=phone))    # 사원정보를 파일에 저장
show_list(load_emps())   # 저장된 데이터 확인, 목록를 화면에 표시한다


# In[63]:


# 키보드에서 num,name,phone 을 입력받아서 emps.txt 에 한 행으로 추가
# 목록보기 기능을 실행하면 추가된 정보가 표시되어야 함
num,name,phone = input('번호 이름 전화:').strip().split()  # 키보드에서 한 사원정보를 입력 받는다
save_emp(Emp(num,name,phone))    # 사원정보를 파일에 저장
show_list(load_emps())   # 저장된 데이터 확인, 목록를 화면에 표시한다


# In[ ]:


# 키보드에서 입력된 사원번호를 키워드로 emps.txt 에서 검색하여
# 검색된 사원정보를 화면에 표시한다
# find_emp(emp)  : Emp객체 리턴
# [Emp, Emp, ...]

nums = [3,4,5]
5 in nums
10 in nums   # 10==3,  10==4,  10==5

emp in emps  # emp==emps[0],  emp==emps[1], ....


# In[64]:


# 파일 데이터를 로드
emplist = load_emps()
# 위에서 로드된 리스트로부터 키보드에서 입력된 사원번호의 Emp객체의 포함여부 확인
sNum = input('검색하려는 사원의 번호:')
emp = Emp( sNum.strip() )

found = None
if emp in emplist:
    found = emplist[emplist.index(emp)]
    
if found:
    print(found)
else:
    print('검색실패')


# In[65]:


def find_emp_t(emp):
    found = None
    if emp in load_emps():
        found = emplist[emplist.index(emp)]
    return found


# In[66]:


sNum = input('검색하려는 사원의 번호:')
emp = Emp( sNum.strip() )
found = find_emp_t(emp)
if found:
    print(found)
else:
    print('검색실패')


# In[71]:


emplist = load_emps()
show_list(emplist)

e = Emp('11')
e in emplist


# In[ ]:


num, phone = input('사원번호 전화:').strip().split()
key = Emp(num, phone=phone)
print(key)


# In[ ]:


def overwrite(emplist):
    try:
        with open('emps.txt', 'w') as fobj:
            for emp in emplist:
                line = "{} {} {}".format(emp.num, emp.name, emp.phone)
                fobj.write(line + '\n')
        return True
    except:
        return False


# In[ ]:


def update_emp(key):
    updated = False
    emplist = load_emps()
    if key in emplist:
        emplist[emplist.index(key)].phone = key.phone
        updated = overwrite(emplist)
    return updated


# In[ ]:


if update_emp(key):
    print('수정성공')
else:
    print('수정실패')
    
show_list(load_emps())   


# In[ ]:


def delete_emp(key):
    deleted = False
    emplist = load_emps()
    if key in emplist:
        emplist.remove(key)
        deleted = overwrite(emplist)
    return deleted


# In[ ]:


# 로드, 리스트에서 삭제대상 찾아서 삭제, 수정된 리스트로 파일 덮어쓰기
sNum = input('삭제할 사원번호:')
key = Emp(sNum.strip())


# In[ ]:


deleted = delete_emp(key)
if deleted:
    print('삭제 성공')
else:
    print('삭제 실패')


# In[ ]:


emp = Emp(15, 'Scott', '000-1111-2222')
with open('empObj.pickle', 'wb') as fw:
    pickle.dump(emp, fw)


# In[ ]:


def show_txt ():
    fobj = open('emps.txt', 'r')
    for i in fobj:
        print(i, end = "")
    fobj.close()


# In[ ]:


# 파일에 한 행 추가
def save_emp(emp):
    fobj = open('emps.txt', 'a') # a : 마지막에 데이터 추가 모드
    fobj.write("15 syeol baboo\n")
    fobj.close()


# In[ ]:


def find_emp(name):
    find = False
    for e in emplist:
        if e.name.upper() == name.upper():
            find = True
            print(e)
            return e
    if find==False:
        print('찾으시는 이름이 없습니다.')


# In[ ]:


find_emp("Hellㅁ")


# In[ ]:


def find_emp_num(num):
    nemp = Emp(num.strip())
    find = emplist[emplist.index(nemp)]
    if find:
        print('찾았습니다.')
    else : print('못 찾았습니다.')
    return find


# In[ ]:


find_emp_num(input('찾으실 번호를 입력해주세요. : '))


# In[ ]:


num = input('수정할 번호를 입력해주세요.')
if find_emp_num(num):
    name, phone = input('수정하실 이름과 전화번호를 입력해주세요.').split()
    for e in emplist:
        if e.num == num:
            e.name = name
            e.phone = phone
            print('수정이 완료되었습니다.')
else: print('찾으시는 회원번호가 없습니다.')   


# In[ ]:


num = input('삭제할 번호를 입력해주세요.')
if find_emp_num(num):
    for e in emplist:
        if e.num == num:
            emplist.remove(e)
            print('삭제 완료되었습니다.')
else: print('찾으시는 회원번호가 없습니다.')   


# In[ ]:





# # 객체 직렬화(Serialization)
# 메모리상에 저장된 객체를 파일이나 네트워크로 전송할 때 필요함

# In[6]:


emp = Emp(15, 'Scott', '000-1111-2222')
with open('empObj.pickle', 'wb') as fw:
    pickle.dump(emp, fw)


# In[ ]:




