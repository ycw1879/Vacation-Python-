#   날짜 : 1월 7일_01
#   작성자 : 윤찬우
#   프로그램 : 

'''
#   ex1) 연도를 나타내는 빈 리스트 생성
years = []

#   2019, 2020, 2021 추가
years.append(2019)
years.append(2020)
years.append(2021)
print(years)

#   2021 삭제
years.pop()
print("삭제 : " ,years)

#   역순
years.reverse()
print("역순 : " , years)

#   정렬
years.sort()
print("정렬 : " , years)

#   맨 앞에 2018 추가
years.insert(0,2018)
print("추가 : " , years)

#---------------------------------
#   2019삭제
#   리스트 항복 전체개수
#   새로운 리스트에 현재 리스트 복사
#   새로운 리스트에 현재 리스트 정렬 후 대입
del(years[1])
print(years)
print(len(years))
new = years.copy()
print(new)
new = sorted(years)
print(new)

#   eX2) 계절을 나타내는 리스트 생성
#겨울 삭제
#정렬
#역순
#마지막에 겨울 추가
#--------------------------------------
#여름삭제
#리스트 항복 전체개수
#새로운 리스트에 현재 리스트 복사
#새로운 리스트에 현재 리스트 정렬 후 대입

season = ["봄","여름","가을","겨울"]
print(season)
season.pop()
print(season)
season.sort()
print(season)
season.reverse()
print(season)
season.insert(3,"겨울")
print(season)

del(season[0])
print(season)
print(len(season))
new_season = season.copy()
print(new_season)
new_season = sorted(season)
print(new_season)

# ex3) 좋아하는 특수문자 While 문으로 5번 출력 (리스트 생성)
list=[]
i=1
while i<=5:
    list.append("☆")
    i = i+1
print(list)

#   ex4) 사용자로부터 5개의 숫자를 입력받아 리스트에 저장하고, 숫자들의 평군을 계산하여
#   출력하는 프로그램
#   hint) 빈 리스트 생성하고 사용자로부터 입력받은 정수를 리스트에 추가한다. (append)
#   리스트의 크기는 len()를 사용한다.
num = []
sum = 0

for i in range(5):
    t = int(input("정수 입력 : "))
    num.append(t)

for i in num:
    sum += i

aver = sum / len(num)
print(aver)

#   ex5) 색상을 리스트에 저장한다.(4개)
#   리스트에 저장된 색상을 하나씩 꺼내어 거북이 색상으로 설정하면서 채워진 사각형을
#   그리는 프로그램
#   함수 사용

import turtle as t
import random as r
t1 = t.Turtle()
t1.shape("turtle")

def Draw_square(x, y, c):
    t1.up()
    t1.goto(x, y)
    t1.down()
    t1.color(c)
    t1.begin_fill()
    for i in range(4):
        t1.fd(100)
        t1.lt(90)
    t1.end_fill()

for z in ['red', 'green', 'blue', 'black']:
    x = r.randint(-100, 100)
    y = r.randint(-100, 100)
    Draw_square(x, y, z)

#   ex6) 학생의 정보(학교, 햑과, 이름)를 나타내는 딕셔너리
kmu = {"학교" : "국민대", "학과" : "컴퓨터공학", "이름" : "윤찬우"}
print(kmu)
#   학번 항목 추가
kmu["학번"] = 20153202
print(kmu)
#   학과 수정
kmu["학과"] = "소프트웨어"
print(kmu)
#   학교 항목 삭제
del(kmu["학교"])
print(kmu)
#   학번, 이름 실제값(value) 출력
print(kmu["학번"])
print(kmu["이름"])
#   학과에 해당하는 값 출력(get())
print(kmu.get("학과"))
#   모든 키값 출력
print(kmu.keys())
#   모든 값 출력(dictionary va~~~)생략
print(list(kmu.values()))
#   in 연산자 사용
print("이름" in kmu)
print("과목" in kmu)

#   ex7) 딕셔너리를 사용해 학생의 이름과 전화번호를 저장한다.
#   학생의 이름과 전화번호를 입력 받아서 딕셔너리에 저장한다.
#   이름을 입력하지 않고 엔터키를 치면 검색보드가 된다.
#   검색 모드에서는 학생들의 이름으로 전화번호를 검색할 수 있도록 한다.
#   hint - 빈 딕셔너리를 생성하고 사용자가 입력하는데로 딕셔너리에 추가한다.
book = {}
while True:
    name = input("(입력모드)이름 입력 : ")
    if name == "":
        break
    number = int(input("(입력모드)전화번호 입력 : "))
    book[name] = number
while True:
    name = input("(검색모드)이름 입력 : ")
    if name in book:
        print(book[name])
    elif name == "":
        break
    else:
        print("없음")
'''
#   ex8) 색상을 리스트에 저장한다.
#   리스트에 저장된 색상을 랜덤하게 꺼내서 해당 색상으로 채워진 별을
#   랜덤한 위치에 그리는 프로그램
#   5번 문제랑 다른점
#   1) 배경색 적용
#   2) 색상 랜덤하게 choice()
import turtle as t
import random as r

colors = ["purple", "pink", "red", "green", "blue", "yellow"]
t.bgcolor("black")
t.Turtle()

def Draw_star(c):
    x = r.randint(-100, 100)
    y = r.randint(-100, 100)
    s = r.randint(50, 200)
    t.color(c)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    for i in range(5):
        t.fd(s)
        t.lt(144)
    t.end_fill()
    
while True:
    star_color = r.choice(colors)
    Draw_star(star_color)
    
