##문자열 출력
# print('ㄴㅇㄻㄴㅇㄹ')

##간단한 연산
# print(10+20)


##내장모듈 사용
# import keyword #내장모듈
# print(keyword.kwlist) #명령어 목록


##여러개 동시에 출력
# print('테스트', 100, 10)


##줄바꿈
# print('123')
# print() #줄 바꿈
# print('456')

# #자료형 확인
# print(type('1000'))
# print(type(1000))
# print(type(True))

# #문자열 너무 길어져 줄바꿈으로 정리하고 싶을때 \하고 엔터치기 (안하면 오류남)
# print('aaaaaaaaaaaaaaaaaaaa\
#       bbbbbbbbbbbbbbbbbbbbbb\
#       cccccccccccccccccccccc\
#       ')

# #문자열 연산자
# print('안녕'+'하세요')
# print('안녕'+1) #오류남
# print('안녕'*3)
# print('안녕'+'하세요'*3)
# print(('안녕'+'하세요')*3)


#문자열 연산자 인덱싱
# print('안녕하세요'[0]) #안
# print('안녕하세요'[4]) #요
# print('안녕하세요'[-1]) #요
# print('안녕하세요'[-5]) #안
# print('안녕'+'하세요'[0]) #안녕하
# print('안녕'+'하세요'[2]) #안녕요
# print(('안녕'+'하세요')[2]) #하
# print('안녕하세요'[10]) #범위 벗어나서 오류


# #문자열 범위 선택 연산자(슬라이싱) [:]
# print('안녕하세요'[0:3]) #안녕하  0~3번쨰까지
# print('안녕하세요'[0:0]) #null
# print('안녕하세요'[-5:-1]) #안녕하세 
# print('안녕하세요'[-1:]) #요  뒤에꺼 생략하면 끝까지
# print('안녕하세요'[:]) #안녕하세요  앞뒤 생략하면 처음부터 끝까지


#문자열 길이
# print(len('12345')) # 5출력


# # 원의 둘레, 넓이 구하기
# pi = 3.14159265
# r=10
# print('원주율 =', pi)
# print('반지름 =', r)
# print('원의 둘레 =', 2*pi*r)
# print('원의 넓이 =', pi*r*r)


# #입력받기
# string = input('나이를 입력하세요') # 입력 받은거 string라는 변수에 저장
# print(string) # string변수 출력
# print(type(string)) # 입력 받은건 무조건 문자로됨
# num = int(string) # 숫자로 변경
# print(type(num)) # 타입출력
# print(num*num) # 숫자로 바꿔서 *연산 가능


# # fromat()함수
# a=input('> 1번째 숫자: ') #입력 받아서 변수 a에 저장
# b=input('> 2번째 숫자: ') #입력 받아서 변수 b에 저장
# print() #줄 띄우기
# print("{} + {} = {}".format(a, b, int(a)+int(b))) # 3 + 4 = 7

# #fromat()함수 응용 (정수를 특정 칸에 출력)
# output_a = "{:d}".format(52)
# output_b = "{:5d}".format(52)
# output_c = "{:10d}".format(52)
# output_d = "{:05d}".format(52)
# output_e = "{:05d}".format(-52)
# print('a:',output_a) #a: 52
# print('b:',output_b) #b:    52
# print('c:',output_c) #c:         52
# print('d:',output_d) #d: 00052
# print('e:',output_e) #e: -0052

# #fromat()함수 응용 (기호 붙여 출력)
# output_f = "{:+d}".format(52)
# output_g = "{:+d}".format(-52)
# output_h = "{: d}".format(52)
# output_i = "{: d}".format(-52)
# print('f:',output_f) #f: +52    양수면 +기호 붙이기
# print('g:',output_g) #g: -52    음수 그대로  
# print('h:',output_h) #h:  52    띄어쓰기하면 양수일때 한칸 띄어서 출력 (음수랑 같은 칸에 출력하는 효과)
# print('i:',output_i) #i: -52    음수는 그대로

# #조합해보기
# output_j = "{:+5d}".format(52)
# output_k = "{:+5d}".format(-52)
# output_l = "{:=+5d}".format(52)
# output_m = "{:=+5d}".format(-52)
# output_n = "{:+05d}".format(52)
# output_o = "{:+05d}".format(-52)
# print('j:',output_j) #j:   +52
# print('k:',output_k) #k:   -52
# print('l:',output_l) #l: +  52
# print('m:',output_m) #m: -  52
# print('n:',output_n) #n: +0052
# print('o:',output_o) #o: -0052


# # 다양한 형태의 부동수수점 출력
# output_a="{:f}".format(52.273)
# output_b="{:15f}".format(52.273)
# output_c="{:+15f}".format(52.273)
# output_d="{:+015f}".format(52.273)
# print('a:',output_a) #a: 52.273000
# print('b:',output_b) #d:       52.273000
# print('c:',output_c) #c:      +52.273000
# print('d:',output_d) #d: +0000052.273000


# # 소수점 아래 자릿수 지정하기
# output_a="{:15.3f}".format(52.273)
# output_b="{:15.2f}".format(52.273)
# output_c="{:15.1f}".format(52.273)
# print('a:',output_a) #a:          52.273
# print('b:',output_b) #b:           52.27
# print('c:',output_c) #c:            52.3


# # 소수점 뒤쪽 0지우기
# output_a = 52.0
# output_b = "{:g}".format(output_a)
# print(output_a) #52.0
# print(output_b) #52


# #대소문자 바꾸기 upper(), lower()
# a = "aaaaaaaaaaAAAAAAAAaaaaaaaaaaaaa"
# print(a.upper()) #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# print(a.lower()) #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


# #문자열 양옆의 공백 제거
# s = """
#       안녕
# 문자열 함수를 알아보자 
# """
# print(s) 
# #
# #       안녕
# # 문자열 함수를 알아보자
# print(s.strip())
# # 안녕
# # 문자열 함수를 알아보자


# #문자열의 구성 파악하기
# # isalnum()은 숫자와 알파벳으로 구성돼있는지 
# print('1234asdf'.isalnum()) # True
# print('1111'.isalnum()) # True
# print('1111!!!!'.isalnum()) # False


# #문자열 찾기
# # .find(), .rfind
# a = '안녕안녕하세요'.find('안녕')
# print(a) # 0
# b = '안녕안녕하세요'.rfind('안녕')
# print(b) # 2


# # 문자열과 in 연산자 (문자열 내부에 어떤 문자열이 있는지 확인)
# print('안녕' in '안녕하세요') # True
# print('잘자' in '안녕하세요') # False


# # 문자열 자르기 split()
# a = "10 20 30 40 50".split(" ")
# print(a) # ['10', '20', '30', '40', '50'] 리스트로 나옴
# print(a[1]) # 20






# 3장 조건문

# #비교연산자
# print(10 == 1000) # False
# print(10 != 1000) # True
# print(10 < 1000) # True
# print(10 > 1000) # False
# print(10 <= 1000) # True
# print(10 >= 1000) # False


# #논리연산자 not, and, or
# print(not True) # False
# print(not False) # True


# #if조건문
# if True: # {}가 없고 :씀
#   print('True입니다 1') # if 안에 들어오는건 tab으로 구분함, 띄어쓰기는 4번
#   print('True입니다 2')
#   print('True입니다 3')


# #elif문 이용한 띠 계산
# str = input('태어난 년도 입력: ')
# year = int(str) % 12
# if year == 0:
#   print('원숭이띠') 
# elif year == 1:
#   print('닭띠') 
# elif year == 2:
#   print('개띠') 
# elif year == 3:
#   print('돼지띠') 
# elif year == 4:
#   print('쥐띠') 
# elif year == 5:
#   print('소띠') 
# elif year == 6:
#   print('뱀띠') 
# elif year == 7:
#   print('토끼띠') 
# elif year == 8:
#   print('용띠') 
# elif year == 9:
#   print('뱀띠') 
# elif year == 10:
#   print('말띠') 
# elif year == 11:
#   print('양띠')
# else: 
#   print('띠 없음')
# print('종료') 


# #날짜/시간 출력하기
# import datetime
# now = datetime.datetime.now()
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(
#   now.year,
#   now.month,
#   now.day,
#   now.hour,
#   now.minute, 
#   now.second
# ))


# # 오전/오후 구분하기
# import datetime 
# now = datetime.datetime.now()
# if now.hour < 12:
#   print('지금은 {}시로 오전임'.format(now.hour))
# else: 
#   print('지금은 {}시로 오후임'.format(now.hour))


# # 계절구분
# import datetime
# now = datetime.datetime.now()
# if 3<=now.month<=5:
#   print('{}월로 봄입니다'.format(now.month))
# elif 6<=now.month<=8:
#   print('{}월로 여름입니다'.format(now.month))
# elif 9<=now.month<=11:
#   print('{}월로 가을입니다'.format(now.month))
# elif 12<=now.mㅜonth<=2:
#   print('{}월로 겨울입니다'.format(now.month))


# # in으로 홀짝 구분
# num = input('숫자 입력')
# last_str = num[-1]
# if last_str in '02468':
#   print('짝수')
# if last_str in '13579':
#   print('홀수')   


# #숫자의 마지막 자리로 홀짝 구하기
# num = input('숫자 입력')
# last_str = num[-1]
# last_num = int(last_str)
# if last_num % 2 == 0:
#   print('짝수입니다')
# else:
#   print('홀수입니다')

##elif로 학점 계산
# score = float(input('학점 입력: '))
# if score == 4.5: 
#   print('신')
# elif score >= 4.2:
#   print('고수')
# elif score >= 3.5:
#   print('중상')
# elif score >= 2.8:
#   print('중')
# elif score >= 2.3:
#   print('중하')
# elif score >= 1.75:
#   print('하')
# elif score >= 1.0:
#   print('음...')
# elif score >= 0.5:
#   print('놀러다님')
# elif score > 0:
#   print('미생물')
# elif score == 0:
#   print('왜 다니는거지')

## if문에 0과 빈 문자열 넣기
# print("if문에 0넣기")
# if 0: 
#   print('0은 트루')
# else: 
#   print('0은 펄스')
# print()
# print("if문에 \'\'넣기")
# if '': 
#   print("\'\'은 트루")
# else: 
#   print('\'\'은 펄스')


# #pass키워드 그냥 넘어가고 싶을때 or 미구현일때 사용
# num = input('정수 입력: ')
# num = int(num)
# if num > 0:
#   #양수일 때 미구현입니다
#   pass
# else: 
#   #음수일 때 미구현입니다
#   pass

# #리스트 안 리스트 넣기
# alist = [333, "하이", False]
# blist = [alist, "리스트안 리스트 넣기"]
# print(alist)
# print(blist)

alist = [1,2,3,4,5,6,7]
print(alist[1:4]) #[2, 3, 4]
print(alist[4:]) #[5, 6, 7]





