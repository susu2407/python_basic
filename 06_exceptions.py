#  06_exceptions.py               # 예외 처리
'''
예외 처리 (Exception Handling) ============================================
1. 개념
    프로그램 실행 중 발생하는 오류를 처리하여
    프로그램이 비정상 종료되지 않도록 하는 것

2. 구조
    try:
        실행 코드
    except:
        예외 발생 시 실행   


'''
# 특정 예외 처리
try:
    num = int(input("숫자 입력: "))
    print(10 / num)

except ValueError:
    print("숫자를 입력하세요")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")


# 예외 객체 사용
try:
    num = int(input("숫자 입력: "))

except ValueError as e:
    print("에러 메시지:", e)


# else & finally
try:
    num = int(input("숫자 입력: "))
except ValueError:
    print("숫자 입력 필요")
else:
    print("정상 입력:", num)
finally:
    print("항상 실행")

'''
try         # 실행
except      # 오류처리
else        # 오류 없을 때
finally     # 무조건 실행
'''

# ========== 강제로 예외 발생 (raise)============================================
#   : 개발자가 직업 예외를 발생시키는 것

# 기본 형태
age = -1

if age < 0:
    raise ValueError("나이는 0 이상이어야 합니다")


# 함수에서 활용 ★★★
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("잔액 부족")
    return balance - amount


# 예시 =================================
while True:
    try:
        num = int(input("숫자 입력: "))
        print(10 / num)
        break
    except ValueError:
        print("숫자를 입력하세요")
    except ZeroDivisionError:
        print("0은 입력할 수 없습니다")


# 사용자 정의 검증 + raise
def check_score(score):
    if score < 0 or score > 100:
        raise ValueError("점수는 0~100 사이여야 합니다")
    return score

try:
    check_score(150)
except ValueError as e:
    print(e)



"""
### 정리

try-except = 오류 대응

raise = 일부러 오류 발생

목적 = 프로그램 안정성

"""