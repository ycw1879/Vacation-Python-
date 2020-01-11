#   날짜 : 01월 10일_01
#   작성자 : 윤찬우
#   프로그램 : 파일 I/O_02
'''
파일 입출력

'''
'''
#   rstip()
#   lstrip()
#   split()
#   replace("","")

#   ex1) 텍스트 파일을 읽어서 출력하는 프로그램 : read()
#   1.
info = open("info.txt","r")
#   2.
print(info.read())
#   3.
info.close()

#   ex2) 텍스트 파일을 읽어서 출력하는 프로그램 : readlines()
info = open("info.txt","r")
print(info.readlines())
info.close()

#   ex3) 텍스트 파일을 읽어서 출력하는 프로그램 : readline()
info = open("info.txt","r")
print(info.readline())
info.close()

#   ex4) 텍스트 파일을 읽어서 출력하는 프로그램 : readline()

info = open("info.txt","r")
line = info.readline()
while line != "":
    print(line)
    line = info.readline()
info.close()

#========== strip() ==========
name = " Yoon ChanWoo "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

#========== replace("a", "b") ==========
name = " 윤찬우 "
print(name)
name = name.replace(name, "Yoon")
print(name)

#   ex5) 전체 데이터 출력
info = open("info.txt", "r")
line = info.readline().rstrip()
while line != "":    
    print(line)
    line = info.readline()
info.close()

#   ex6) 전체 데이터 출력(가장 많이 사용되는 방법)
#   파일에서 문자열을 읽을 때 for문을 사용해서 파일 객체에 대해 반복해도 된다.
info = open("info.txt", "r")
for line in info:
    one = line.strip()
    print(one)
info.close()

#   ex7)
#   1.과목이름과 학기가 출력 되는 프로그램(2줄까지만)
#   2.파일 전체 출력(리스트 형태)
#   3.파일 첫줄만 출력
#   4.readline()함수로 파일 전체 출력
info = open("practice.txt", "r")
all_read = info.read()
print(all_read)
info.close
info = open("practice.txt", "r")
line = info.readline()
print(line)
info = open("practice.txt", "r")
lines = info.readlines()
print(lines)
info = open("practice.txt", "r")
for lines in info:
    print(lines.strip())
info.close()

#==================write()==================
#   ex8) 파일에 데이터 쓰기
score = open("score.txt", "w")
print(score.write("윤찬우 : 90\n"))
print(score.write("구민재 : 80\n"))
print(score.write("김민재 : 70\n"))
print(score.write("장지은 : 90\n"))
score.close()

#   ex9) 8번 예제에 학생 한명 추가
score = open("score.txt", "a")
print(score.write("김종현 : 80\n"))
score.close()

#==================split()==================
#   공백문자를 이용해 문자열에서 단어를 분리한다.
#   ex10) 파일을 읽어와서 공백문자로 단어를 분리하는 프로그램
fruits = open("list.txt", "r")
for i in fruits:
    list = i.split()
    for j in list:
        print(j)
fruits.close()
'''
#   ex11) 파일 복사
#   시스템 모듈(shutil) 포함시킨 후에 copy()함수를 사용한다.
import shutil
shutil.copy("info.txt", "temp.txt")

#   ex12) 파일 복사
file1 = input("입력할 파일은?")
file2 = input("출력할 파일은?")
shutil.copy(file1, file2)






