#   날짜 : 1월 7일_01
#   작성자 : 윤찬우
#   프로그램 : 

#   ex1)
def Abstract():
        print('************************')
        print('0. 종료')
        print('1. 재고 추가')
        print('2. 재고 삭제')
        print('************************')
        
dic = {"우유" : 1, "종이컵" : 2, "책" : 5, "커피음료" : 7, "콜라" : 4, "펜" : 3}
while True:
    print("# 재고 목록 #")
    for k, v in sorted(dic.items()):
        print(k, v)
    Abstract()
    order = int(input("무엇을 하시겠습니까? : "))

    if order == 1:
        name = input("물거의 이름을 입력하시오 : ")
        number = int(input("몇개를 추가하시겠습니까? : "))
        dic[name] = dic[name] + number
    elif order == 2:
        name = input("물거의 이름을 입력하시오 : ")
        number = int(input("몇개를 삭제하시겠습니까? : "))
        dic[name] -= number
    elif order == 0:
        break
    else:
        continue
    
#   ex2)
dic = {}
dic["겨울"] = "winter"
dic["봄"] = 'spring'
dic["여름"] = 'summer'
word = input("단어 입력")
print(dic[word])

#   ex3)
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
    x = r.randint(-300, 200)
    y = r.randint(-300, 200)
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
    
