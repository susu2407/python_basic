# 01_variables_and_types.py      # 변수와 자료형

# ========== 숫자형 (Integer, Float)  ========================================
""" 
10 (값=데이터)
= (대입 연산자) -> 대입 = 저장(★多) = 할당 이라고 표현한다.
a 를 변수 라고 부른다.
따라서 a = 10 을 해석하면, 10을 a에 대입/저장/할당 한다.
"""

# 변수 선언 =========
a = 5       # 숫자 데이터
b = -10     # 음수
c = 0       # 음수, 0, 양수의 숫자 데이터 -> 정수(integer) 
d = 1.23    # 실수 (float)
e = -1.23   # 실수 (float)

print(a)    # 5
print(b)    # -10

# 연산 ===============
print("a+b =", a+b)     # a+b = -5
print("a-b =", a-b)     # a-b = 15
print("a*b =", a*b)     # a*b = -50
print("a/b =", a/b)     # a/b = -0.5    (몫)
print("a//b =", a//b)   # a//b = -1     (몫, 정수자리까지 반올림)
print("a%3 =", a%b)     # a%3 = -5      (나머지)
print("a**2 =", a**2)   # a**2 = 25     (거듭제곱)

# 복합 연산자 ========
a = a + 1
print("a + 1 =", a)     # a + 1 = 6
a += 1
print("a +=", a, "\n")  # a += 7 


# ========== 숫자형 (Complex 복소수)  ========================================
'''
Complex (복소수)
    : 실수(real)와 허수(imaginary)로 이루어진 숫자 자료형

형태
    : a + bj ( j는 허수 단위)


complex(실수, 허수)
    → 복소수를 만드는 함수


'''
# 기본사용
c1 = 3 + 4j
c2 = complex(1, 2)  # 1 + 2j
c3 = complex(3, 4)  # 3 + 4j

print(c1 == c3)  # true
print(c1.real)   # 실수 부분
print(c1.imag)   # 허수 부분

# 연산
print(c1 + c2)
print(c1 * c2)


# =========== 문자열 (string) ==============================================

x = ' "Hello world!" '
y = 'Nice to meet you'
z = "안녕하세요!"
xx = """Hello
WA
o
r
l
d
!
"""
print(x)
print(y)
print(z)
print(xx)

# 문자열 반복 =======
print(x*3)

# 문자열 연결 =========
print("hello" + "coding" + "world")     # 출력 : hellocodingworld

s1 = "coding"
s2 = "!!!"

print("hello %s world" % "coding")      # 출력 : hello coding world
print("hello %s world" % s1)            # 출력 : hello coding world
print("hello %s world %s" % (s1, s2))   # 출력 : hello coding world !!!

print("hello %s world %d" % (s1, 30))   # 출력 : hello 30 world !!!


# 인덱싱과 슬라이싱 ==========
text = "Python"

print(text[0])   # 'P'
print(text[-1])  # 'n'
print(text[0:4]) # 'Pyth', 끝 인덱스 미포함

# ※(주의) text[0] = "J" ❌, 리스트와 달리 값을 직접 변경할 수 없으므로, 새 문자열 생성이 필요


# 문자열 슬라이싱 심화========

print(text[::2])  # 'Pto', 2칸씩 건너뛰기
print(text[::-1]) # 'nohtyP', 뒤집기



# 논리형 (Boolean) ========================================================
t = True
f = False

print(type(a))  # <class 'int'>
print(type(x))  # <class 'str'>
print(type(t))  # <class 'bool'>
print(type(f))  # <class 'bool'>

# a = 5
# c = 0  이므로 
print(a > c)      # True
print(a == c)     # False
print(a != c)     # True



# 리스트 (List) =============================================================
list1 = [1, 0.7, 'hello', True, [1,2,3]]

list1[1] = "2.5"    # f[인덱스] : 인덱스 위치의 값 변경

print(list1[0])     # 인덱스 값 출력
print(list1[-1])    # 뒤에서 첫 번째 출력
print(list1[1:3])   # 1부터 2까지 출력 - 슬라이싱: [시작:끝] → 끝은 포함되지 않음
print(list1[0:-2:2])# 0부터 -2까지 2씩 뛰어서 출력

#list1.append(100)   # append(값) : 끝에 추가
#list1.insert(0,"f") # insert(인덱스, 값) : 인덱스 위치에 값을 삽입, 기존 값들은 뒤로 밀림
#list1.remove(0.7)   # remove(값) : 배열에서 '값'과 동일한 값이 제거
#list1.pop(0)        # pop(인덱스) : '인덱스' 위치의 값을 제거하고, 그 제거된 값을 반환하는 메서드
#list1.pop()         # pop() : 리스트의 가장 마지막 요소를 제거하고 반환
#list1.extend(f)     # extend(iterable) : 리스트 끝에 iterable 전체 항목 추가. append와 달리 전체를 펼쳐서 추가함

#print("list1[1] =", list1[1])
#print("list1.append(100) =", list1)
#print("list1.insert(0,"list1") =", list1)
#print("list1.remove(0.7) =", list1)
#print("list1.pop(0) =", list1.pop(0), "\n그래서 list1 =", list1)
#print("list1.extend(list1) =", list1)
#print("len(list1) =", len(list1))        # len : 리스트 길이 : 리스트 원소의 개수


list2 = [1, 2, 3]
list3 = [4, 5]

print(list2 + list3)   # [1, 2, 3, 4, 5]
print(list2 * 2)    # [1, 2, 3, 1, 2, 3]

# + → 연결
# * → 반복


numbers = [3, 1, 4, 1, 5]
numbers.sort()       # [1, 1, 3, 4, 5]
numbers.reverse()    # [5, 4, 3, 1, 1]

# sort() → 오름차순 정렬
# reverse() → 순서 뒤집기
# index(value) → 값의 위치
# count(value) → 값 개수 세기
# clear() → 전체 삭제


# ========== Tuple (튜플) ================================================
'''
Tuple (튜플)
    : 변경 불가능한(immutable) 리스트
'''
t = (1, 2, 3)   # 튜플 생성

print(t[0])   # 접근 가능
# t[0] = 10 ❌ (수정 불가)

# 언패킹 ===============
a, b, c = (1, 2, 3)
print(a, b, c)


# ========== 딕셔너리 자료형 (사전) dictionary ===========================

# key : value

# 키 중복 X
d = {'name':'권지용',
      'age':'3N살', 
      'color':'red', 
      'heigh':168}

d['number'] = "010-0000-0000"   # 추가

print(d)            # {'name': '권지용', 'age': '3N살', 'color': 'red', 'heigh': 168, 'number': '010-0000-0000'}
print(d['name'])    # 권지용
print(d['color'])   # red

d['age']=20                     # 수정
print(d)            # {'name': '권지용', 'age': 20, 'color': 'red', 'heigh': 168, 'number': '010-0000-0000'}

print(d.keys())     # dict_keys(['name', 'age', 'color', 'heigh', 'number'])
for k in d.keys():
    print(k)
''' 출력 결과 :
name
age
color
heigh
number
'''

print(d.values())   # dict_values(['권지용', 20, 'red', 168, '010-0000-0000'])
for v in d.values():
    print(v)
'''출력 결과:
권지용
20
red
168
010-0000-0000
'''

for k, v in d.items():
    print(k, v)
'''출력 결과:
name 권지용
age 20
color red
heigh 168
number 010-0000-0000
'''

# 사전(Dictionary)에 키 또는 값이 있는지 찾을 때에
print(d.get('weight'))          # None
print(d.get('weight'),
      "해당 데이터는 없습니다.") # None 해당 데이터는 없습니다.



# 리스트, 딕셔너리 -> for문 =============

# 1. 점수 5개 입력받기
scores = []
for i in range(5):
    score = int(input("점수 입력: "))
    scores.append(score)                # append : 새로운 항목을 맨 뒤에 추가

# 2. 성적 총점 계산
total = 0
for i in range(len(scores)):
    total += scores[i]

# 3. 성적 평균 계산 (총점/len(scores))
avg = total / len(scores)

# 4. 80점 이상의 개수 계산
count = 0
for c in scores:
    if c >= 80:
        count += 1

# 최종 결과 출력
print(f"총점: {total}, 평균: {avg}")
print(f"80점 이상의 개수: {count}")


# ==========  세트 (Set) =================================================
'''
Set (세트)
    : 중복 제거 + 순서 없음
'''
s = {1, 2, 3, 3}
print("set 실행 =", s)   # set 실행 = {1, 2, 3}

s.add(4)      # 추가
s.remove(2)   # 삭제

print("set 실행 =", s)   # set 실행 = {1, 3, 4}


a = {1, 2, 3}
b = {3, 4, 5}
5
print(a & b)  # 교집합 -> 결과 : {3}
print(a | b)  # 합집합 -> 결과 : {1, 2, 3, 4, 5}
print(a - b)  # 차집합 -> 결과 : {1, 2}


# 예시
numbers = [1, 1, 2, 3, 3]
print(list(set(numbers)))   # [1, 2, 3]


# ==========  자료형 변환 (Type Casting) =========================================
print(int("10"))
print(float("3.14"))
print(str(100))
print(bool(0))     # False
print(bool(1))     # True

print(list("abc"))   # ['a', 'b', 'c']

int("10")    # 가능
# int("abc") ❌ 에러

