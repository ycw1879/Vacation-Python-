#   날짜 : 01월 09일_02
#   작성자 : 윤찬우
#   프로그램 : 파일 I/O
'''
#   ex1) 파일 읽어오기
info = open('C:\\Users\\USER\\Desktop\\kim.txt','r')
lines = info.read()
print(lines)
info.close()

#   ex2) 파일에 쓰기
#   이름과 주소 정보를 파일에 쓰는 예제
info = open('C:\\Users\\USER\\Desktop\\kim.txt','w')
info.write("김민재 중국 청도출신 폭격기\n")
info.close()
'''
#   ex3) 파일에 추가: write()
#   기존 파일에 쓰기
info = open('C:\\Users\\USER\\Desktop\\kim.txt','a')
info.write("살인범 김민재 여자애들은 민재만 보면 끔뻑 죽어버리지")
info.close()

