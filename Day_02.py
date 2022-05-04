#!/usr/bin/env python
# coding: utf-8

# In[11]:


#임의의 정수 10개 추출하고
#내림차순으로 정렬하고,
#화면에 표시
#오름차순으로 정렬
#맨 마지막에 있는 정수 1개 삭제
#중간에 위치한 수를 추출하여 화면에 표시
#중간에 수가 없다면 중간 양쪽에 있는 수의 평균 값 표시

import random

random_ten = []

for _ in range(0, 10):
 random_ten.append(int(random.randint(1,31)))

random_ten.sort(reverse=True)
print(random_ten)

random_ten.sort()
print(random_ten)

del random_ten[9]
# random_ten.pop()도 가능
print(random_ten)



#print(random_ten[int(len(random_ten)/2)])
print(random_ten[4])
print((random_ten[3]+random_ten[5])/2)


# In[9]:


#  모듈을 사용하겠다.
import random as rd


# In[10]:


# 임포트 하지 않았지만 사용 가능한 것 확인
rd.randint(0,5)


# In[16]:


# range(1,6)은 하나의 오브젝트이다.
alist = list(range(1,6))
print(alist)

even_numbers = list(range(2,11,2)) #start(시작숫자), stop(종료숫자), step(2씩 커져라) 
print(even_numbers)


# In[18]:


squares = [value**2 for value in range(1,11)]
print(squares)


# In[19]:


#1~10 사이의 정수 중에서 짝수만 선택하여 리스트의 원소에 저장하고 홀수는 0으로 변경하여 저장한 후
#리스트의 모든 원소를 화면에 표시해보세요.

tenlist = []

for i in range(1,11,2):    
    tenlist.append(0)
    tenlist.append(i+1)

print(tenlist)


# In[21]:


#listcomprehension
nums = [v if v%2==0 else 0 for v in range(1,11)]
print(nums)


# In[25]:


print(squares)

print(squares[:-3])
print(squares[-3:])
print(squares[1:3])


# In[31]:


copy = squares # Shallow Copy(얕은 복사)
print('squares', squares)
print('copy ', copy)

copy[0] = 3
print('squares', squares)
print('copy ', copy)


# In[32]:


copy2 = squares[:] #Deep Copy
print('squares', squares)
print('copy2 ', copy2)

copy[0] = 7
print('squares', squares)
print('copy2 ', copy2)


# In[33]:


dimensions =(200,5) # 튜플:리스트방식과 같지만 자료 변경이 안됨.
print(dimensions[0])
print(dimensions[1])


# In[34]:


dimensions[0] = 250 # 오류 발생


# In[40]:


a, b = dimensions
print(a,b)

print(type(a))
a=250
print(a)


# In[50]:


# 무작위 정수 10개 준비
# 처음 3개를 추출하여 튜플에 저장
# 튜플 내용 화면에 표시

tenlist = []
for _ in range(0,10):
    tenlist.append(rd.randint(1,100))

showlist = (tenlist[0], tenlist[1], tenlist[2])
print(showlist)

hilist = [rd.randint(1,100) for v in range(0,10)]
print(hilist)


# In[62]:


# 키보드에서 아이디, 암호를 입력 받아서 로그인하는 기능 구현
# 미리 uid, pwd 이스트를 생성해놓고 몇개의 정보를 준비함
# uid, pwd에는 아이디는 모두 대문자로 준비함
# 로그인에 성공할 때까지 반복해서 시도(3번까지) 할 수 있도록 함.
# 결국 로그인에 성공하면 '로그인 성공', 아니면 '로그인 실패' 표시


uidlist = ['AAA', 'BBB', 'CCC']
pwdlist = ['111', '222', '333']

Failed = 0

for _ in range(0,3):
    uid = (input('아이디를 입력하시오 : ')).upper()
    pwd = input('비밀번호를 입력하시오 : ')

    try :
        idx = uidlist.index(uid)
        if pwdlist[idx]==pwd:
            print('로그인 성공')
            break
    except ValueError as e:
        Failed = Failed+1
        print('아이디와 비밀번호를 확인해주세요.')
        print('')
        if Failed == 3:
            print('로그인 실패')


# In[77]:


'd' in ['a', 'b', 'c']


# In[70]:


# 파이썬 날짜 다루기

#import datetime
#today = datetime.date.today()

import datetime
from datetime import date
today = date.today() # 둘 다 가능

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday()) # 월(0), 화(1), 수(2).....
print(today.isoweekday()) #iso에서는 월(1), 화(2), 수(3)....


# In[72]:


if today.isoweekday() == 1:
    Dayoftheweek = '월'
elif today.isoweekday() == 2:
    Dayoftheweek = '화'
elif today.isoweekday() == 3:
    Dayoftheweek = '수'
elif today.isoweekday() == 4:
    Dayoftheweek = '목'
elif today.isoweekday() == 5:
    Dayoftheweek = '금'
elif today.isoweekday() == 6:
    Dayoftheweek = '토'
elif today.isoweekday() == 7:
    Dayoftheweek = '일'    


# In[73]:


# 오늘 날짜 출력하기
print(f'{today.year}년 {today.month}월 {today.day}일 {Dayoftheweek}요일')


# In[76]:


dayoftheweek = ('월화수목금토일')

# 오늘 날짜 출력하기
print(f'{today.year}년 {today.month}월 {today.day}일 {dayoftheweek[today.weekday()]}요일')


# In[79]:


# 키보드에서 아이디, 암호를 입력 받아서 로그인하는 기능 구현
# 미리 uid, pwd 이스트를 생성해놓고 몇개의 정보를 준비함
# uid, pwd에는 아이디는 모두 대문자로 준비함
# 로그인에 성공할 때까지 반복해서 시도(3번까지) 할 수 있도록 함.
# 결국 로그인에 성공하면 '로그인 성공', 아니면 '로그인 실패' 표시
# try except 대신 boolean 값으로 찾아보기


uidlist = ['AAA', 'BBB', 'CCC']
pwdlist = ['111', '222', '333']

Failed = 0

for _ in range(0,3):
    uid = (input('아이디를 입력하시오 : ')).upper()
    pwd = input('비밀번호를 입력하시오 : ')
    
    if uid in uidlist:
        idx = uidlist.index(uid)
        if pwdlist[idx]==pwd:
            print('로그인 성공')
            break
    Failed = Failed+1
    print('아이디와 비밀번호를 확인해주세요.')
    print('')
    if Failed == 3:
          print('로그인 실패')


# In[83]:


users = [{}, {}, {}] # {}이게 JAVA의 map형식이다 : pyyhon에서는 딕셔너리라고 한다.

print(type(users)) #list
print(type(users[0])) #dict


# In[112]:


# 키보드에서 3인의 회원정보를 입력받는다.
# 번호 이름 전화
# 입력을 마치면, 입력된 모든 정보를 리스트로 화면에 표시

users =[]
for _ in range(3):
    (num, name, phone) = input('번호, 이름, 전화').split()
    users.append({'num':num, 'name':name, 'phone':phone})

print(users)


# In[121]:


# 동일 의미
for user in users:
    s = f"{user['num']}\t{user['name']}\t{user['phone']}"
    print(s)
print()    
for i in users:
    s = f"{i['num']}\t{i['name']}\t{i['phone']}"
    print(s)   


# In[132]:


users[0]['phone'] = 111
print(users)


# In[133]:


del users[2]['phone']


# In[137]:


print(users)


# In[140]:


for user in users:
    s = f"{user['num']}\t{user['name']}\t{user.get('phone','전화기 분실')}"
    print(s)   


# In[141]:


# 위의 리스트에 몇 사람 정보를 저장한다.
# 키보드에서 회원번호를 입력하여 해당 회원을 검색하고 그 결과를 화면에 표시한다.

emp = []
emp.append({'num': '1', 'name': 'a', 'phone': 111})
emp.append({'num': '2', 'name': 'b', 'phone': '012'})
emp.append({'num': '3', 'name': 'c', 'phone': '013'})
print(emp)


# In[158]:


want = input('찾으실 회원번호를 입력해주세요.')

find = False
for i in emp:
    if i['num'] == want :
        print(f"{i['num']}\t{i['name']}\t{i['phone']}")   
        find = True
        break;
if find == False:
    print('입력하신 회원번호는 없습니다.')


# In[156]:


want = input('찾으실 회원번호를 입력해주세요.')

find = False

for i in emp:
    if i['num'] == want:       
        print(i)
        find = True
        break;

if find == False:       
    print('입력하신 회원번호는 없습니다.')


# In[ ]:


# list, set, dictionary
# list : 순서유지, 중복허용
# set : 순서없음, 중복불허
# dictionary : key, value 쌍으로 저장


# In[164]:


print(set([3,1,1,1,1,2]))
len(set([3,1,1,1,1,2]))


# In[162]:


#1~10 사이의 정수 중에서 임의로 한개를 추출하여 중복되지 않도록 7개를 추출하려고 한다.

a = []

while True:
    a.append(rd.randint(1,10))
    if len(set(a))== 7:
        break
        
print(set(a))