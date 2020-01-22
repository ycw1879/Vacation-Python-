# 작성자 : 윤찬우
'''
#   1. pickle 쓰고, 읽기
import pickle as p

file = open("test.dat",'wb')
p.dump(10, file)
p.dump(30.13, file)
p.dump([10, 20, 30, 40, 50], file)
file.close()

file = open("test.dat", "rb")
for i in range(3):
    print(p.load(file))
file.close()

#   2. 암호화, 복호화
text = "윤찬우" 
encrypt = "" 
for i in text:
    x = ord(i) 
    x += 1
    c = chr(x) 
    encrypt += c 
print(encrypt)
text = ""
for i in encrypt:
    x = ord(i) - 1
    c = chr(x)
    text += c
print(text)
'''
#   3. 계산기
from tkinter import*

def plus():
    update("plus")

def minus():
    update("minus")

def reset():
    update('reset')

w = Tk()
total = 0
sum = Label(w)
sum.grid(row = 0, column = 1, columnspan = 2)

la = Label(w, text = "현재 합계 : ")
la.grid(row = 0, column = 0)

entry = Entry(w)
entry.grid(row = 1, column = 0, columnspan = 3)

bu1 = Button(w, text = "더하기(+)", command = plus)
bu2 = Button(w, text = "빼기(-)", command = minus)
bu3 = Button(w, text = "초기화(C)", command = reset)

bu1.grid(row = 2, column = 0)
bu2.grid(row = 2, column = 1)
bu3.grid(row = 2, column = 2)

def update(a):
    global total
    if a == "plus":
        total += int(entry.get())
    elif a == "minus":
        total -= int(entry.get())
    else:
        total = 0
    sum['text'] = str(total)
