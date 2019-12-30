#   날짜 : 12월 30일_01
#   작성자 : 윤찬우
#   프로그램 : 조건문
'''
if 조건식:
    참일때 실행할 문장

#   ex1) 나이를 입력받아 20살 이상이면 성인입니다. 출력
name = int(input("나이 입력 : "))
if name >= 20:
    print("20살 이상이면 성인입니다.")

#   ex2) 학교이름을 입력 받아 국민대학교면 국민대학생입니다. 출력
univ = input("대학교 입력 : ")
if univ == "국민대학교":
    print("국민대학생입니다.")
=====================================================
if else
=====================================================
if 조건식 :
    참일 때 실행될 문장
else :
    거짓일 때 실행될 문장

#   ex3) 나이를 입력받아 20살 이상이면 성인입니다.
#   그렇지 않으면 청소년입니다. 출력

age = int(input("나이 입력 : "))
if name >= 20:
    print("20살 이상이면 성인입니다.")
else:
    print("청소년입니다.")

#   ex4) 학교이름을 입력 받아 국민대학교면 국민대학생입니다.
#   그렇지 않으면 타대학생입니다. 출력
univ = input("대학교 입력 : ")
if univ == "국민대학교":
    print("국민대학생입니다.")
else:
    print("타대학생입니다.")

#   ex5) 아이디(문자열)와 비번(숫자)을 변수로 저장한 후, 사용자가 아이디와 비번을 정확하게
#   입력하면 로그인하셨습니다. 그렇지 않으면 다시 입력하세요. 출력
id = input("아이디 : ")
pw = int(input("패스워드 : "))
if id == "20153202" and pw == 1541:
    print("로그인 하셨습니다")
else:
    print("다시 입력하세요.")

#   ex6) 동전던지기 예제
import random as r

coin = r.randrange(2)
if coin == 0:
    print("앞면")
else:
    print("뒷면")
print("게임 종료")

#   ex7) 동전 던지기
import turtle as t
import random as r

s = t.Screen()
front = "\\Users\\chanwoo\\Desktop\\front.gif"
back = "\\Users\\chanwoo\\Desktop\\back.gif"

s.addshape(front)
s.addshape(back)

t1 = t.Turtle()
coin = r.randrange(2)

if coin == 0:
    t1.shape(front)
else:
    t1.shape(back)

waitkey = t.textinput("waitkey", "wait")

#   ex8) 점수를 입력 받아 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C,
#   그렇지 않으면 F를 출력하는 프로그램
score = int(input("잠수 입력 : "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 80:
    print("C")
else:
    print("F")

#   ex9) 신호등 색상을 입력 받아(R, G, Y), 입력받은 색상이 G 또는 g이면 "건너가세요"
#   R 또는 r이면 멈추세요. Y 또는 y이면 주의하세요.
#   다른 색상을 입력하면 신호등 색상을 입력하세요. 출력하는 프로그램
signal = input("color input : ")
if signal == "R" or signal == "r":
    print("멈추세요.")
elif signal == "G" or signal == "g":
    print("건너가세요.")
elif signal == "Y" or signal == "y":
    print("주의하세요.")
else:
    print("신호등 색상을 입력하세요.")
'''
#   ex10) in 연산자 사용
#   계절 리스트 생성 후, 여름 항목 삭제
#   계절 리스트에 여름 항목이 있으면, 여름입니다. 출력
list = ["봄", "여름", "가을", "겨울"]
del(list[1])
if "여름" in list:
    del("여름입니다.")
print(list)
