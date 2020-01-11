#   날짜 : 01월 11일
#   작성자 : 윤찬우
#   프로그램 : Assignment2_02

#   2. 딕셔너리 제시
quizes = {'"파이선을 설치할 때 기본으로 포함되는 그래픽 모듈"' : 'tkinter',
        '"데이터를 저장하는 임시 저장 공간"' : '변수',
        '"작업을 수행하는 문장들의 집합에 이름을 붙인 것"' : '함수',
        '"리스트에서 한 번에 여러 개의 항목을 추출하는 기법"' : '슬라이싱'
}
for q in list(quizes.keys()):
    print('다음은 어떤 단어에 대한 설명일까요?')
    print(q)
    idx = 1
    while True:
        for solutions in list(quizes.values()):
            print('[' + str(idx) + ']' + solutions, end = " ")
            idx += 1
        print()
        idx = 1
        solution = input()
        if solution == quizes[q]:
            print("정답입니다.!")
            break
        print("정답이 아닙니다.")
