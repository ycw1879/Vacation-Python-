#   윤찬우
'''
#   1번
import shutil
file_name = input("파일 이름을 입력하세요: ")
file = open(file_name,"r")
cnt = 0
for i in file:
    cnt += len(i.strip().replace(" ",""))
print("파일 안에는 총",cnt,"개의 글자가 있습니다.")
file.close()

#   2번
import shutil
input_name = input("파일 이름을 입력하세요: ")
input_file = open(input_name, "r")
output_file = open("temp.txt", "w")
delete = input("삭제할 문자열을 입력하시오: ")
for i in input_file:
    j = i.replace(delete,"")
    output_file.write(j)
input_file.close()
output_file.close()

#   3번
import shutil
input_name = input("입력 파일 이름: ")
output_name = input("출력 파일 이름: ")
input_file = open(input_name, "r")
output_file = open(output_name, "w")
sum = 0.0
total_cnt = 0
result = 0.0
for i in input_file:
    j = i.strip()
    sum += float(j)
    total_cnt += 1
result = sum / float(total_cnt)
output_file.write("합계="+str(sum)+"\n")
output_file.write("평균="+str(result)+"\n")
input_file.close()
output_file.close()
'''
#   딕셔너리를 파일에 저장하기 위해서 pickle 모듈을 사용한다.
#   dump(): 딕셔너리 전달
#   load():

import pickle as p # pickle 모듈에 포함
stu = {"이름":"윤찬우", "학과":"컴퓨터공학", "학번":20153202} # 학생정보 딕셔너리 생성
file = open("stu.p","wb") # 바이너리 모드로 읽기 # 읽을때는 rb 쓸때는 wb b는 byte라는 의미
p.dump(stu, file) # dump함수로 딕셔너리를 파일에 전달
file.close()

file = open("stu.p","rb")
print(p.load(file))
file.close()





