#   날짜 : 01월 09일_01
#   작성자 : 윤찬우
#   프로그램 : 윈도우 프로그래밍
'''
#   ex1) 좋아하는 계절을 나타내는 체크버튼(4개)를 생성한 후 체크버튼을 선택할 때마다
#   레이블에 선택한 계절이 출력되게 하는 프로그램.
from tkinter import *
w = Tk()
w.title("오늘의 연습")

w.geometry("400x400")
w.resizable(width = True, height = True)

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()

def CheckSeason():
    str = ""
    if v1.get() == 1:
        str += "봄\n"
    if v2.get() == 1:
        str += "여름\n"
    if v3.get() == 1:
        str += "가을\n"
    if v4.get() == 1:
        str += "겨울\n"
    if str == "":
        str = "X"
    lb5.configure(text = str)

lb1 = Checkbutton(w, text = "봄", variable = v1, command = CheckSeason)
lb2 = Checkbutton(w, text = "여름", variable = v2, command = CheckSeason)
lb3 = Checkbutton(w, text = "가을", variable = v3, command = CheckSeason)
lb4 = Checkbutton(w, text = "겨울", variable = v4, command = CheckSeason)
lb5 = Label(w, text = "X", font = ("맑은 고딕", 25))

lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()
lb5.pack()

#   ex2) 본인의 학교를 선택하는 라디오 버튼 3개를 생성한 후, 해당 학교이름을 메시지 박스로
#   출력하는 프로그램
from tkinter import *

w2 = Tk()
w2.title("연습2")
w2.geometry("400x400")
w2.resizable(width = False, height = True)

var = IntVar()

def RadioCheck():
    if var.get() == 1:
        messagebox.showinfo("","국민대학교입니다")
    if var.get() == 2:
        messagebox.showinfo("","서울대학교입니다")
    if var.get() == 3:
        messagebox.showinfo("","배재대학교입니다")

ra1 = Radiobutton(w2, text = "국민대학교", command = RadioCheck, value = 1, variable = var)
ra2 = Radiobutton(w2, text = "서울대학교", command = RadioCheck, value = 2, variable = var)
ra3 = Radiobutton(w2, text = "배재대학교", command = RadioCheck, value = 3, variable = var)

ra1.pack()
ra2.pack()
ra3.pack()

#   ex2) 본인의 학교를 선택하는 라디오 버튼 3개를 생성한 후, 해당 학교이름을 메시지 박스로
#   출력하는 프로그램
from tkinter import *

w2 = Tk()
w2.title("연습2")
w2.geometry("400x400")
w2.resizable(width = False, height = True)

var = IntVar()

def RadioCheck():
    str = ""
    if var.get() == 1:
        str = "국민대학교입니다"
    if var.get() == 2:
        str = "서울대학교입니다"
    if var.get() == 3:
        str = "배재대학교입니다"
    la1.configure(text = str)
    

ra1 = Radiobutton(w2, text = "국민대학교", command = RadioCheck, value = 1, variable = var)
ra2 = Radiobutton(w2, text = "서울대학교", command = RadioCheck, value = 2, variable = var)
ra3 = Radiobutton(w2, text = "배재대학교", command = RadioCheck, value = 3, variable = var)
la1 = Label(w2, text = "X", font = ("맑은 고딕", 25), fg = "blue")

ra1.pack()
ra2.pack()
ra3.pack()
la1.pack()
'''
#   ex3)
from tkinter import *

w3 = Tk()
w3.title("연습3")
w3.resizable(width = False, height = False)

img1 = PhotoImage(file = "k.png")
img2 = PhotoImage(file = "s.png")
img3 = PhotoImage(file = "b.png")

def func():
    if var == 1:
        la.configure(image = img1)
    elif var == 2:
        la.configure(image = img2)
    elif var == 3:
        la.configure(image = img3)

var = IntVar()
la1 = Label(w3, text = "학교를 선택하세요", font = ("맑은 고딕", 25), fg = 20)
univ1 = Radiobutton(w3, text = "국민대학교", value = 1, variable = var)
univ2 = Radiobutton(w3, text = "서울대학교", value = 2, variable = var)
univ3 = Radiobutton(w3, text = "배재대학교", value = 3, variable = var)
bu = Button(w3, text = "사진보기", command = func)
la = Label(w3)

la1.pack()
univ1.pack()
univ2.pack()
univ3.pack()
bu.pack()
la.pack()
