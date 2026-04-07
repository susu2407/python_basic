# 02_operators.py                # 연산자 정리
# ========== 산술 연산자 ==================================================
# - 숫자 연산용
num1 = 10
num2 = 3

print(num1 + num2)   # 13
print(num1 - num2)   # 7
print(num1 * num2)   # 30
print(num1 / num2)   # 3.3333333333333335 (실수)
print(num1 // num2)  # 3 (몫)
print(num1 % num2)   # 1 (나머지)
print(num1 ** num2)  # 1000 (거듭제곱)


# ========== 비교 연산자 ==================================================
# - 조건문에서 많이 사용
val1 = 5
val2 = 10

print(val1 == val2)   # False
print(val1 != val2)   # True
print(val1 > val2)    # False
print(val1 < val2)    # True
print(val1 >= 5)      # True
print(val2 <= 5)      # False


# ========== 논리 연산자 ==================================================
# - 조건을 조합할 때 사용
bool_a = True
bool_b = False

print(bool_a and bool_b)  # False
print(bool_a or bool_b)   # True
print(not bool_a)         # False


# ========== 멤버 연산자 ==================================================
# - 시퀀스 자료형(문자열, 리스트 등)에 값이 있는지 확인
# - in, not in
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)     # True
print("kiwi" not in fruits)  # True


# ========== 식별 연산자 ==================================================
# - 변수의 주소(객체 동일성) 확인
# - is, is not
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 is list2)     # False, 다른 객체
print(list1 == list2)     # True, 값은 같음
print(list1 is list3)     # True, 같은 객체
print(list1 is not list2) # True










