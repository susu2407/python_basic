# 03_control_statements.py       # 제어문 (조건문, 반복문)

# =============== 조건문⭐ =============================================
'''
< 구조 >
'조건'이 참True이면 '실행할 코드1'가 실행된다.

if 조건:
    실행할 코드1

    
if 조건:
    실행할 코드1
else:
    실행할 코드2

    
if 조건1:
    실행1
elif 조건2:
    실행2
elif 조건3:
    실행3
else:
    실행4


< 조건에 사용할 수 있는 것들 >
1. 비교 연산자
== : 같다
!= : 다르다
> : 크다
< : 작다
>= : 이상
<= : 이하

2. 논리 연산자
and : 둘 다 참
or : 하나 이상 참
not : 결과의 반대

★들여쓰기(indent) 매우 중요!

'''
x = 10
y = 3
z = 7


if x > 5:
    print("x는 5보다 크다.")


if y > 5:
    print("y는 5보다 크다.")
else:
    print("y는 5보다 작다.")


if z > 10:
    print("z는 10보다 크다.")
elif z == 10:
    print("z는 10이다.")
elif z > 5:
    print("z는 10보다 작고 5보다 크다.")
else:
    print("z는 5보다 작다.")


score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")


# and 예시) ===============
if x > 5 and x < 10:
    print("x는 5보다 크고 10보다 작다.")
 

# not 예시) ===============
is_logged_in = True

message = "로그인 필요" if not is_logged_in else "환영합니다"

print(message)



'''
< 한 줄 조건문(삼항 조건문) > ===============
    : if문을 한 줄로 간단하게 표현한 것이다.
      조건에 따라 값을 바로 선택할 때 많이 사용함.

<구조>
값1 if 조건 else 값2

(의미)
    조건이 참   -> 값1
    조건이 거짓 -> 값2
'''
a = 50

#일반 if문
if a > 30:
    result = "크다"
else:
    result = "작다"

# 한 줄 조건문(삼항 조건문)
result = "크다" if a > 30 else "작다"

print(result)


# =============== 반복문 ⭐ =============================================
'''
< for문 : 횟수가 정해져 있는 경우 > ================

for i in range(범위값):
    코드1


< while문 : 횟수가 정해져 있지 않은 경우 > ===============

while 조건식:
    코드1

(※주의) 무한 반복될 수 있음. -> break문 사용하기.
'''



