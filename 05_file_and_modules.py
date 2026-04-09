# 05_file_and_modules.py         # 파일 입출력, 모듈

# 파일입출력
# open() → 파일 생성 및 열기
# close() →  파일 닫기
# write()→  파일에 저장 
# with open() → 파일 열고 자동 닫기
# =======================

import os

print("os.getcwd() = ", os.getcwd())    # os.getcwd() 는 어디에 저장되어 있는지 보여줌

f = open("new_text.txt", "w")   
f.close()                       # open 파일 열기 -> close  (close하지 않아도 오류가 생기지는 않지만, 데이터 누수 방지 차원에서 하는 것을 습관화 하자.)

# 기본 구조
f = open("test1.txt", "w")
f.write("내용")
f.close()

# with 사용하면자동으로 close() 해줌
with open("test2.txt", "w") as f:
    f.write("내용")

# =======================
#(연습) 입력 → 파일 저장(write) → 파일 읽기 → split → 계산
# 1. 5명의 학생의 이름과 성적(국,영,수)을 입력받아서
# 2. 텍스트 파일(scores.txt)에 저장하시고
# 3. 텍스트 파일에서 읽어와서 해당 학생의 성적 평균, 최고 성적을 새 파일에 저장

# items() → 딕셔너리 꺼내기
# 문자열.split() → 문자열을 쪼개는 함수
# .2f → 소수점 2자리, 반올림

# 1.
student = {}

for i in range(5):
    name = input("이름 입력: ")
    kor = int(input("국어 성적: "))
    eng = int(input("영어 성적: "))
    math = int(input("수학 성적: "))

    score = {'kor' : kor, 'eng' : eng, 'math' : math}
    student[name] = score

print(student) # 확인  

# 2.
# 딕서너리.ver
with open("scores.txt", "w") as f:
     for name, scores in student.items():
        f.write(f"{name} {scores['kor']} {scores['eng']} {scores['math']}\n")


# 3.
result = []

with open("scores.txt", "r") as f:
    for line in f:
        data = line.split()
        
        name = data[0]
        kor = int(data[1])
        eng = int(data[2])
        math = int(data[3])
        
        avg = (kor + eng + math) / 3
        max_score = max(kor, eng, math)
        
        result.append(f"{name} 평균:{avg:.2f} 최고점:{max_score}\n")

# 결과 저장
with open("result.txt", "w") as f:
    f.writelines(result)

