# 04_functions.py                # 함수, lambda
"""
◆ 함수 정의 (Function Definition)
: 함수 정의는 특정 작업을 수행하는 코드를 하나로 묶어서 이름을 붙이는 것.
-> “이름을 부르면 실행되는 코드 묶음”

def : 함수를 직접 만들 때 사용하는 키워드
def 함수이름(매개변수):
    실행코드

◆ 매개변수 (Parameter)
: 함수에 입력으로 전달되는 값을 받아서 처리하기 위한 변수
-> “함수 안에서 사용하는 입력값 자리”

◆ 반환값 (Return Value)
: 함수가 실행된 결과로 돌려주는 값
-> “함수가 계산하고 나서 밖으로 내보내는 결과”

----------------------------------------------------------------
(예시)
아래 코드 중
def add(x,y):
    return x + y
add(3, 5)
에서:

add             → 함수 이름
def             → 함수를 정의한다는 키워드
a, b            → 매개변수(parameter, 변수)
3, 5            → 인자(argument, 실제 값)
return a + b    → 함수가 수행할 작업
return ...      → 결과(...부분)를 돌려주는 키워드
a + b           → 반환값(함수가 실행 후 돌려주는 결과)

-> 즉, "두 숫자를 더하는 기능을 가진 함수"를 만든 것

---------------------------------------------------------------
◆ 내장 함수 (Built-in Function)
: 파이썬에 이미 만들어져 있어서 바로 사용할 수 있는 함수
  즉, 우리가 직접 def로 만들지 않아도 됨

print   # 출력
len     # 길이
sum     # 합계
def     # 함수
pass    # 아무 동작도 하지 않고 그냥 넘어가는 코드 (일단 비워두기)


"""



# 함수 (-> 재사용) =======================
def func(x):
    pass        # pass : 아무 동작도 하지 않고 그냥 넘어가는 코드 (일단 비워두기)

def add(x,y):
    return x + y

def sub(x,y):   # (큰 값 - 작은 값) 리턴
    if x > y:
        return x - y
    return y - x

def mul(x,y):   # x 곱 y
    return x * y

def bigger(x,y):# x, y 둘 중에서 큰 값 리턴
    if x > y:
        return x
    return y

x = 3
y = 5

print(add(x,y))
print(sub(x,y))
print(mul(x,y))
print(bigger(x,y))

# =======================

def test(x, y, z=10):
    return x * y + z

print(
    test(mul(x, y),     # x * y = 3 * 5 = 15
         bigger(x, y)   # x < y -> y = 5
        )               # x * y + z = 15 * 5 + 10 = 85
    )

print(test(z=3, x=5, y=20)) # 5 * 20 + 3 = 103

# =======================

while True:
    print("==========메뉴==========")
    print("다음 번호 중 입력하시오.\n1. 덧셈\n2. 뺄셈\n3.곱셈\n4.큰 값 출력\n5.종료")

    menu = int(input("메뉴 선택:"))
    if menu == 5:
        break

    x = int(input("첫번째 수: "))
    y = int(input("두번째 수: "))
    
    if menu == 1:
        print(add(x, y))
    elif menu == 2:
        print(sub(x, y))
    elif menu == 3:
        print(mul(x, y))
    elif menu == 4:
        print(bigger(x, y))
    elif menu == 5:
        break
        
        


# =============== lambda =================================================
"""
◆ lambda (람다 함수)
: 이름 없이 간단하게 만드는 함수
-> “짧게 한 줄로 쓰는 함수”

< 기본 형태 >
lambda 매개변수: 반환값

< 특징 >
- 이름이 없음 (익명 함수)
- 한 줄로만 작성 가능
- return 키워드 없이 자동 반환
- 간단한 함수에 적합

< 언제 쓰면 좋을까? >
- 짧고 간단한 기능일 때
- 한 번만 사용할 때
- 코드 줄이 줄어들 때
❌ 복잡한 로직 → 일반 함수가 더 좋음

"""

# (예시) =======================
# 일반함수
def get_min(a, b):
    if a < b:
        return a
    else:
        return b

# 람다식
get_min_lam = lambda a, b: a if a < b else b

print(get_min(3, 7))      # 3
print(get_min_lam(3, 7))  # 3


#(예시2) lambda + sort 같이 쓰기    (sort : 기본-오름차순 정렬)
data = [(1, 3), (2, 1), (3, 2)]

data.sort(key=lambda x: x[1])

'''
의미:
(숫자1, 숫자2) 형태 데이터
x = ( x[0], x[1] ) 형태 데이터 이므로,
두 번째 값 기준으로 정렬한다.


결과: 
[(2, 1), (3, 2), (1, 3)]

'''


# ===== 계산기를 함수로 만들어 보자 ========
# ===== 계산기를 클래스로 만들어 보자 ======


