#   날짜 : 1월 13일
#   작성자 : 윤찬우
#   프로그램 : 예제
'''
#   ex1) 딕셔너리에 과일 이름과 수량을 저장(3개)한다.
#   pickle 모듈을 사용해서 이진파일 객체를 쓰고 읽는 프로그램을 작성한다.
import pickle as p
fruits = {'수박' : 3, '딸기' : 5, '자몽' : 5}
file = open("fruits.b",'wb')
p.dump(fruits, file)
file.close()

file = open("fruits.b", "rb")
print(p.load(file))
file.close()

#   ex2) 학생 3명에 대한 딕셔너리 생성
#   key, value
#   이름, 학생 3명의 이름
#   학과, 학생 3명의 학과
#   학번, 학생 3명의 학번

stu = {'이름' : ['구민재', '김민재', '윤찬우'], '학과' : ['소프트웨어', '소프트웨어', '컴퓨터공학'], '학번' : [20150001, 20150002, 20150003]}
file = open("fruits.b",'wb')
p.dump(stu, file)
file.close()

file = open("stu.p", "rb")
print(p.load(file))
file.close()
'''
#   ex3) 문자열 암호화
text = "윤찬우" # 평문
encrypt = "" # 암호문
for i in text:
    x = ord(i) # 문자의 코드값을 구한다.
    x += 1 # 코드값 1증가
    c = chr(x) # 증가된 코드값에 해당하는 문자를 계산한다.
    encrypt += c # 암호문에 추가한다.
print(encrypt)

#   ex4) 문자열 복호화
text = ""
for i in encrypt:
    x = ord(i) - 1
    c = chr(x)
    text += c
print(text)

#   ex5) 이름을 입력하는 입력박스를 작성한다.
from tkinter import*
w = Tk()
name = Label(w, text = "이름")
name_input = Entry(w)
name.pack()
name_input.pack()




