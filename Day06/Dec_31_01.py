#   날짜 : 12월 31일_01
#   작성자 : 윤찬우
#   프로그램 : 반복문
'''
for 변수명 in  range(반복횟수):
    반복실행할 문장
    
for 변수명 in 리스트:
    반복실행할 문장

#   ex1) 본인 이름 5번 반복 출력(for문)
for i in range(5):
    print("윤찬우")

#   ex2) 계절리스트 생성 후 항목 출력(for문)
for i in["봄", "여름", "가을", "겨울"]:
    print(i)
    
#   ex3) 1부터 10까지 홀수만 출력(for)
for i in range(1, 11, 2):
    print(i,end=" ")

#   ex4) 사각형 그리기(for)
import turtle as t
t.Turtle()
t.bgcolor("black")
t.color("white")
for i in range(4):
    t.fd(100)
    t.lt(360/4)

#   ex5) 1부터 10까지의 합을 구하는 프로그램 (for)
psum = 0
for i in range(1, 11):
    psum += i
print(psum)

#   ex5-2) 1부터 10까지의 곱을 구하는 프로그램(for)
msum = 1
for i in range(1, 11):
    msum *= i
print(msum)

#   ex6) 학생 5명의 성적을 입력 받아 합을 구하는 프로그램 (for)
sumGrade = 0
for i in range(5):
    sumGrade += int(input("성적 입력 : "))
print(sumGrade)

#   ex7) 점수를 입력 받아, 1부터 입력받은 정수까지의 합을 구하는 프로그램(for)
sum = 0
num = int(input("사이즈 입력 : "))
for i in range(1, num + 1):
    sum += i
print(sum)

#   ex8) 출력할 단을 입력받아 해당 구구단을 출력하는 프로그램
dan = int(input("단 입력 : "))

for i in range(1,10):
    print(dan, "X", i, "=", dan * i)
    
#   ex9) 전체 구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print(i,"X",j,"=",i*j)
    print("")

#   ex10) 학생들의 성적을 입력 받아 성적이 0과 같으면 누적된 합을 구하는 프로그램
sumGrade = 0
for i in range(100):
    x = int(input("성적 입력 : "))
    sumGrade += x
    if x == 0:
        break
print(sumGrade)

#   ex10-2) 평균~
sumGrade = 0
for i in range(100):
    x = int(input("성적 입력 : "))
    if x == 0:
        sumGrade //= i
        break
    sumGrade += x
print(sumGrade)

#   ex10-3) 성적이 음수이면 누적된 합을 구하는 프로그램
for i in range(100):
    x = int(input("성적 입력 : "))
    if x <= 0:
        break
    sumGrade += x
print(sumGrade)

#   ex11) 혈액형을 입력 받아 A이면 A형 출력, B이면 B형 출력, O이면 O형 출력
#   AB이면 AB형 출력, 그렇지 않으면 다시 혈액형을 입력 받는 프로그램
for i in range(100):
    blood = input("혈액형 입력 : ")
    if blood == "A":
        print("A형")
        break
    elif blood == "B":
        print("A형")
        break
    elif blood == "B":
        print("A형")
        break
    elif blood == "B":
        print("A형")
        break
    else:
        print("다시 입력")
        continue

#=============================While==============================
#   ex12) 본인이름 5번 출력
cnt = 0
while cnt < 5:
    print("윤찬우")
    cnt += 1
    
#   ex13) 1부터 10까지의 곱
ret = 1
multi = 1
while multi <= 10:
    ret *= multi
    multi += 1
print(ret)

#   ex14) 단을 입력받아 해당 구구단 출력
k = 1
dan = int(input("단 입력 : "))
while k < 10:
    print(dan, "X", k, "=", dan * k)
    k += 1
    
#   ex15) 암호가 python가 같으면 로그인 성공, 같지 않으면 암호를 계속 입력받는 프로그램
pw = ""
while pw != "python"
    pw = input("암호입력 : ")
print("로그인 성공")
'''
#   ex16) 성적을 입력 받아 평균을 구하는 프로그램(음수를 입력하면 종료)
sum = 0
while True:
    x = int(input("성적 입력 : "))
    if x < 0:
        break
    sum += x
print(sum)

#   ex17)혈액형을 입력 받아 A이면 A형 출력, B이면 B형 출력, O이면 O형 출력
#   AB이면 AB형 출력, 그렇지 않으면 다시 혈액형을 입력 받는 프로그램
while True:
    blood = input("혈액형 입력 : ")
    if blood == "A":
        print("A형")
        break
    elif blood == "B":
        print("A형")
        break
    elif blood == "B":
        print("A형")
        break
    elif blood == "B":
        print("A형")
        break
    else:
        print("다시 입력")
        continue

#   중간고사
'''
유형 : 빈칸 채우기(코드 채우기 break, continue 등), 출력 결과 읽기, 소스코드 일부분 비워둔 삘이 터틀이지않을까? 채우기
'''
