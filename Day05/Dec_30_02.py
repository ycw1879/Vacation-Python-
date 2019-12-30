#   날짜 : 12월 30일_02
#   작성자 : 윤찬우
#   프로그램 : 실습

#   ex1) 연속적인 if문 (그래픽 버전)
#   저녁 메뉴 4개 중 하나가 출력되는 프로그램
import turtle as t
import random as r
'''
s = t.Screen()
salmon = "salmon.gif"
fish = "fish.gif"
gimchi = "gimchi.gif"
tomato = "tomato.gif"

s.addshape(salmon)
s.addshape(fish)
s.addshape(gimchi)
s.addshape(tomato)

t1 = t.Turtle()

ranint = randint(0, 3)

if ranint == 0:
    t1.shape(salmon)
elif ranint == 1:
    t1.shape(fish)
elif ranint == 2:
    t1.shape(gimchi)
else:
    t1.shape(tomato)

waitkey = t.textinput("waitkey", "wait")

'''
#   ex2) 혈액형(A, a, B, b, O, o, AB, ab)을 입력 받아
#   A또는 a이면 "A형", B또는 b이면 "B형"
#   O또는 o이면 "O형", AB 또는 ab이면 "AB형"을 출력하는 프로그램
signal = input("blood input : ")
if signal == "A" or signal == "a":
    print("A형")
elif signal == "B" or signal == "b":
    print("B형")
elif signal == "O" or signal == "o":
    print("O형")
elif signal == "AB" or signal == "ab":
    print("AB형")
else:
    print("없는 혈액형입니다.")

#   ex3) 좋아하는 과일 리스트(3개)를 생성 후, "망고"가 있는지 판별하는 프로그램
#   in연산자 사용
list = ["사과","딸기","포도"]
if "망고" in list:
    print("망고 있습니다.")
else:
    print("망고 없습니다.")
