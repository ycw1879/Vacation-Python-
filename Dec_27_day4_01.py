#   날짜 : 12월 27일
#   작성자 : 윤찬우
#   프로그램 : 터틀그래픽

import turtle as t

#   ex1) 반지름(50) 을 입력 받아 원을 그리는 프로그램
t.bgcolor("black")          # 배경색
t.speed(0)                  # 속도 설정(0이 제이 빠르고 1은 느리다 점점느리다)
t.shape("turtle")           # 모양 설정
t.color("#D5D5D5")          # 선 색상
t.fillcolor("#5CD1E5")      # 면 색상 ("blue")
t.begin_fill()              # 색상 채우기 시작
t.circle(50)                # 원 그리기
t.end_fill()                # 색상 채우기 끝
#t.ht()                      # 거북이 숨기기
#t.st()                      # 거북이 나타내기
t.color("red")
t.fillcolor("green")
t.up()                      # 펜 들기
t.fd(200)                   # 보는 방향으로 전진
t.down()                    # 펜 내리기
t.begin_fill()
t.lt(90)                    # 보는 방향에서 왼쪽으로 각도 틀기
t.fd(100)                   # 보는 방향으로 전진
t.lt(90)                    # 보는 방향에서 왼쪽으로 각도 틀기
t.fd(100)                   # 보는 방향으로 전진
t.lt(90)                    # 보는 방향에서 왼쪽으로 각도 틀기
t.fd(100)                   # 보는 방향으로 전진
t.lt(90)                    # 보는 방향에서 왼쪽으로 각도 틀기
t.end_fill()
t.up()
t.rt(90)
t.fd(200)
t.down()
t.begin_fill()
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.end_fill()
t.fillcolor("yellow")
t.up()
t.goto(-100, 100)
t.down()

n = 5
for i in range(n):
    t.fd(100)
    t.lt(144)


t.up()
t.goto(0, -200)
#t.home()

t.down()
r = t.textinput("원그리기","반지름 입력 : ")
t.circle(int(r))

name = t.textinput("이름 입력란", "이름 : ")
t.write("안녕하세요?"+name+"님")

t.up()
t.goto(-100, -100)
t.down()
univ = t.textinput("","학교 이름 : ")
t.write("안녕하세요"+univ+"입니다.")
just = t.textinput("","그냥입력해")
