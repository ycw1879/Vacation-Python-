#   날짜 : 01월 08일
#   작성자 : 윤찬우
#   프로그램 : 윈도우 프로그래밍
'''
#   ex1) 윈도우 창 생성
from tkinter import *
from tkinter import messagebox

def myimg():
    messagebox.showinfo("0108","두번 콩콩이")

w = Tk() # 객체 생성
w.title("윈도우 프로그래밍") # 윈도우 창 이
# w.geometry("400x400") # 크기 조절
w.resizable(width = False, height = False) # 크기 조절 고정

lb1 = Label(w,text = "컴퓨터 프로그래밍", font = ("맑은 고딕", 25), fg = "blue")
lb1.pack() # 해당 레이블 저장

lb2 = Label(w,text = "컴퓨터 공학", font = ("맑은 고딕", 25), fg = "black")
lb2.pack() # 해당 레이블 저장

lb3 = PhotoImage(file = "dog.gif")
dog1 = Label(w, image = lb3)
dog1.pack(side = RIGHT)

lb4 = PhotoImage(file = "dog2.gif")
dog2 = Label(w, image = lb4)
dog2.pack()

bu = Button(w, text = "종료", fg = "red", bg = "pink", command = quit)
bu.pack()

bu2 = Button(w, image = lb3, command = myimg)
bu2.pack()
'''
#   ex2) 학교명을 체크하고 버튼을 클릭하면 메세지박스가 뜨는 프로그램
#   학교명을 체크하고 버튼을 클릭하면 메시지박스가 뜨는 프로그램
#   grid함수 사용
from tkinter import *
from tkinter import messagebox

w = Tk()
w.title("2019")
w.geometry("200x200")
def click():
    str=""
    if Var1.get() == 1:
        str = str + "국민대 당첨"
    if Var2.get() == 1:
        str = str + "상명대 당첨"
    if str == "":
        str = "선택되지 않음"
    messagebox.showinfo("Button Clicked", str)
Var1 = IntVar()
Var2 = IntVar()
cb1 = Checkbutton(w, text = "국민대", variable = Var1)
cb2 = Checkbutton(w, text = "상명대", variable = Var2)
bu = Button(w, text = "수강과목", command = click)
cb1.grid(row = 1, column = 1)
cb2.grid(row = 2, column = 1)
bu.grid(row = 3, column = 2)
