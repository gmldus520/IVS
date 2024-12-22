
'''
12/16 오전
'''
# print('조희연', 29) // 문자와 숫자 동시출력(콤마는 스페이스 역할)

# print('hello world', end = ' ') // end는 한줄에 print를 여러 번
# print('next line')

# print('hello world\nnext line') //\n은 한줄 줄바꿈

# print('###', end = ' ')
# print('###')
# print('#7#', end = ' ')
# print('#3#')
# print('###', end = ' ')
# print('###')

# print('안녕 나는 \'희연\'이야')

# PI = 3.14
# PI = '삼점일사'

# print(PI)

# from math import pi
# pi = 3.14
# print(pi)

# a = 20

# print(a)
# print(str(a) + '값') //권장하지 않음
# print(f'{a}값') //f-string 권장

# name = '조희연'
# age = 29
# area = '서대문구'

# print(f'저는 {name}이고, 나이는 {age}이고, {area}에 살고 있습니다.')

# PI = 3.14159

# print(f'소수 3자리: {PI:.3f}')

# a = 10.25
# b = 20.31
# sum_value = a + b

# print(f'a와 b를 합치면 {sum_value:.1f}이 됩니다.')

# a = 10
# print(id(a))
# a = 50
# print(id(a))

# a = 3
# a = 3.1
# a = 3 + 2j
# a = True
# a = None
# print(type(a))

# a = int('3')
# print(a)
# print(type(a))

# a = float('3.14')
# print(a)
# print(type(a))

# a = int(3.14) //소수점 이하 버림
# print(a) 
# print(type(a)) 

# print(5/2)
# print(5//2) //몫
# print(5%2)

# print(-2 ** 2) //거듭제곱이 단항연산자보다 우선순위

# a = 0
# a += 1
# print(a)

# a = input()
# print(a)
# a = int(input())
# print(a)
# a, b = map(int, input().split())
# print(a, b)
# a = list(map(int, input().split()))
# print(a)

'''
num = list(map(int, input().split()))
a, b, c, d, e = map(int, input().split())

print(num)
print(a, b, c, d, e)
'''

# a, b = 1, 2

# print(a >= b)

# print(2 and 6)
# print(2 and 0)
# print(0 and 2)

# print(6 or 2)
# print(2 or 0)
# print(0 or 2)

# a 유니코드 : 97
# A 유니코드 : 65 //대소문자는 32차이가 난다

# print(ord('a'))
# print(ord('A'))
# print(chr(65))

#소문자 a를 입력받아 소문자 b를 출력해 보세요
# char = input()
# print(chr(ord(char) + 1))

#대문자를 입력받아 소문자를 출력해 보세요
# char = input()
# print(chr(ord(char) + 32))

'''
12/16 오후
'''
#조건식 : 비교연산, 논리연산, 멤버연산...
#조건식이 True이면 code를 실행

# if 조건식:
#     Code

# #elif는  if의 부정
# elif 조건식:
#     code

# #else는  elif의 부정
# else: 
#     code


# grade = int(input())

# if grade >= 95:
#     print('A+')
# elif grade >= 90:
#     print('A')
# elif grade >= 85:
#     print('B+')
# elif grade >= 80:
#     print('B')
# elif grade >= 75:
#     print('C+')
# elif grade >= 70:
#     print('C')
# else:
#     print('D')



# grade = int(input())
# score = ''

# if grade >= 95:
#     score = 'A+'
# elif grade >= 90:
#     score = 'A'
# elif grade >= 85:
#     score = 'B+'
# elif grade >= 80:
#     score = 'B'
# elif grade >= 75:
#     score = 'C+'
# elif grade >= 70:
#     score = 'C'
# else:
#     score = 'D'

# print(f'{score}학점')


# year = int(input())

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('윤년')
# else:
#     print('윤년x')

# b1, b2, b3, b4 = map(int, input().split())

# if b1 >= b2 and b1 >= b3 and b1 >= b4:
#      print(f'b1이 가장 크다')

# 위 함수를 알고리즘으로 풀어본다면 다음과 같다
# if b1 >= max(b2, b3, b4):
#      print(f'b1이 가장 크다')


# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1
'''
# C언어 for와 비교
# arr = [1, 2, 3, 4, 5];
#     for i in range(5);
#     arr(i);  

# for n in 'heeyeon':
#     print(n)

# range(start, end, step)
# end값이 포함되지 않는다는 것이 핵심
# ==============================

str_num = "12345"
# break 조건에 부합할 경우 반복문을 탈출

for i in str_num:
    if i == '3':
        break
    print(i) # 출력 결과 : 1, 2

# continue  조건에 부합할 경우 반복문 '처음'으로 돌아가기
for i in str_num:
    if i == '3':
        continue
    print(i) # 출력 결과 : 1, 2, 4, 5

for i in range(5):
    if i == 2:
        continue    
     if i == 4:
        break
    print(i) #출력 0, 1, 3
'''


'''
12/17 오전
'''
# a = [] 할당
# a = [1, 1, 1] 할당
# a.append(1)
# a = [2, 2, 2, 6] 할당
# a.append(5)
# print(a) //총 3번 할당

#day2 8페이지 도전문제 
# arr = [1, 5, 2, 7, 3, 6]

# print(arr[0], arr[len(arr)-1])
# print(arr[0], arr[-1]) // 마지막은 -1요소와 같다

# print(arr[0:6:2]) //홀수만
# for i in arr:
#     if 3 <= i <= 6: print(i) //3에서 6사이만

#day2 11페이지 도전문제 
# arr = [0] * 5
# value = 5

# for i in range(5):
#     arr[i] = value
#     value += 1

# for num in arr:
#     print(num, end = ' ')

#day2 22페이지 도전문제 

# a, b = 0, 0

# def input_num():
#     global a, b
#     a, b = map(int, input().split())

# def output_num():
#     global a, b
#     input_num()
#     for i in range(a, b+1):
#         print(i, end = ' ')

# output_num()

'''
#2중 for문
2x3 행렬을 출력하세요.
###
###

for i in range(2):
    for j in range(3):
        print('#', end = ' ')
    print()

2x5 행렬을 출력하세요.
01234
01234

for i in range(2):
    for j in range(5):
        print(j, end = '')
    print()

3x3 행렬을 출력하세요.
123
456
789

a = 1
for i in range(3):
    for j in range(3):
                print(a, end = '')
                a += 1
    print()
'''
# 7의 갯수를 반복문+조건문을 이용해 작성하세요.
# 짝수 개수? i % 2 == 0
# 3과 5 tkdl 3 <= i <= 5

# arr = [1, 4, 4, 7, 7, 7, 7, 2, 7]
# cnt = 0

# for i in arr:
#     if i == 7:
#         cnt += 1
       
# print(f'{cnt}개')

#value가 0이고, 5개의 요소로 이루어진 1차원 배열
# arr1 = [0] * 5
# arr2 = [0 for _ in range(5)] //2차원 리스트때문에 두가지 다 알아야함
# print(arr2)

#1번. 0으로 채워진 2x4 행렬을 하드코딩 하세요.
# height = 2
# width = 4

# arr3 = [[0] * width for _ in range(height)]
# print(arr3)
# #2번. 2중for문 사용해서 모두 7로 채우세요. 2x4 행렬을 하드코딩 하세요.

# for i in range(height):
#     for j in range(width):
#         arr3[i][j] = 7
# print(arr3)

#3x5행렬을 만들고, 0부터 14로 채우기
# rows = 3
# cols = 5

# arr = [[0 for _ in range(cols)] for _ in range(rows)] // 리스트컴프레션

# num = 0
# for i in range(rows):
#     for j in range(cols):
#         arr[i][j] = num
#         num += 1
# print(arr)

'''
return 함수
def 함수명(매개변수):
    Code
    return 반환값

함수명(함수인자)
'''
#두 정수의 합을 계산하는 함수를 정의하고, 호출해 보세요(retrun 함수)

# def add_func(a, b):
#     result = a + b
#     return result 

# a, b = map(int, input().split())

# print(add_func(a, b)) 

'''
딕셔너리

1.첫번째방법
a = dict()
a = {} // 딕셔너리 맞음
a['Hi'] = 55
#'hi'는 key, 55는 value
2.두번째방법
a = {'HI' : 55, 'BBQ' : 'KFC'} // 가변형 비시퀀스


#day2 31페이지 도전문제
lst = ['MC', 'BTS', 'BTS', 'MC', 'BTS']
cnt = 0 

di = dict()
for i in lst:
    di[i] = 0

for i in lst:
    di[i] += 1

max_cnt = 0
result = ''

for word, cnt in di.items():
    if cnt > max_cnt:
        max_cnt = cnt
        result = word

print(result)
'''

#문자열이 몇개인지 출력한다->value값을 추출한다
#day2 35페이지 도전문제
# lst = ['ABE', 53 -99, -99, 124]

# di = dict()
# for i in lst:
#     di[str(i)] = 0

# for i in lst:
#     di[str(i)] += 1

# a = input()
# print(di[a])

#day2 40페이지 도전문제
# di = {'KFC' : 10, 'MC' : 20, 'MOMS' : 30}
# a = input()

# if a in di:
#     print(di[a])
# else:
#     print(1000)
'''
#key 로 순회
for key in di:
    print(key)

#value로 순회
for value in di.values():
print(value)

#키와 value로 순회
for key, value in di.items():
    print(f'{key} : {value}')
'''
#day2 41페이지 도전문제
'''
lst = ['MC', 'BTS', 'BTS', 'MC', 'BTS']

di = dict()

for i in lst:
    if (i not in di): di[i] = 0
    di[i] += 1

print(f'MC : {di['MC']}개\nBTS : {di['BTS']}개')

'''
#dictionary 도전과제 1번
'''
N, M = map(int, input().split())

di = dict()

#N개의 수열 입력받기
lst = list(map(int, input().split()))

for i in lst:
    if i not in di: di[i] = 0
    di[i] += 1

#M개의 질문 입력받기
question = list(map(int, input().split()))
for q in question:
    if q in di:
        print(di[q], end = ' ')
    else:
        print(0, end = ' ')
'''
#dictionary 도전과제 2번
'''
N, M = map(int, input().split())

di = dict()

lst = list(map(int, input().split()))

for i in lst:
    if i not in di: di[i] = 0
    di[i] += 1

for _ in range(M):
    question = int(input())
    if question in di:
        print(di[question])
    else:
        print(0)
'''
#tuple 55페이지
'''
def abc(value):
    a = value[3][2][0]
    for i in a:
        print(i)

abc([1, 2, ('A', 'B'), [1, 2, [("KFC", 'MOMS', 'BHC')]]])
'''
#58페이지
'''
di = dict()

di['HI'] = [1, 2, 3, 'KFC1']
di['OH'] = [1, 5, {'HO': 14, 'MY': 119, 'QQ' : 'KFC2'}]
di[-153] = [(1, 2, (5, 6, 'KFC3'))]

print(di['HI'][3])
print(di['OH'][2]['QQ'])
print(di[-153][0][2][2])
'''

#12/18 오전

# import json

# a = dict()

# a['name'] = 'sanghi'
# a['price'] = 4900
# a['brand'] = 'mcdonald'

# #b는 json(인코딩)
# b = json.dumps(a, indent = 4)

# #c는 딕셔너리(디코딩)
# c = json.loads(b)

# print(b)
# print(c)

# f1 = open('mc.json', 'r')
# f2 = open('output.txt', 'w')

# txt = f1.read()
# f2.write(txt)
# print(txt)

# f2.close()
# f1.close()

# txt =''

# with open('mc.json', 'r')  as f1:
#     txt = f1.read()

# with open('output.txt', 'w') as f2:
#     f2.write(txt)

# import json

# txt = ''

# with open('mc.json', 'r') as f1:
#     txt = f1.read()

# #json을 dict로 디코딩
# di = json.loads(txt)

# with open('output.txt', 'w') as f2:
#     f2.write(' '.join(str(x) for x in di['widget']['window'].keys()) + '\n')
#     f2.write(' '.join(str(x) for x in di['widget']['image'].values()) + '\n')
#     f2.write(' '.join(str(x) for x in di['widget']['text'].items()))

# import json
# import requests

# url = "https://api.tvmaze.com/singlesearch/shows?q=narcos&embed=episodes"
# #.text ---> json 객체
# r = requests.get(url)
# print(r.text)

'''
12/19 수업 OOP(class)
'''
#class함수에서 명칭은 반드시 대문자로 시작

# class Zergling:
#     def __init__(self):
#         self.hp = 20
#         self.mana = 50
    
#     def run(self):
#         print('뛴다')
#         self.hp -= 1
#         self.mana += 1

#     def show_status(self):
#         print(f'hp : {self.hp}, mana : {self.mana}')

# z1 = Zergling()
# z2 = Zergling()

# z1.run()
# z1.show_status()

# for i in range(5): z2.run() //run()매서드 5회 반복
# z2.show_status()


# class GameMachine():
#     def __init__(self):
#         self.coins = 0

#     def input_coin(self, amount):
#         if amount > 5:
#             return
#         if self.coins + amount > 10:
#             return
#         self.coins += amount

#     def play_game(self):
#         if self.coins < 1:
#             print('코인을 넣어주세요')
#             return
#         self.coins -= 1
#         print('게임 재밌다')

#     def show_status(self):
#         print(f'남아있는 코인은 {self.coins} 입니다')
        
# gm = GameMachine()
# gm.input_coin(2)
# gm.show_status()
# gm.play_game()
# gm.show_status()

# class Tire():
#     def run(self):
#         print('런')

# class Tire1(Tire):
#     def ran(self):
#         print('랜')

# class Tire2(Tire):
#     def run(self):
#         print('런런')
#     def ron(self):
#         print('론')

'''
데이터 사이언스 기초
'''

# import numpy as np //numpy는 벡터연산이 가능하다(결과갑 비교해보기)

#그냥 리스트 곱
# lst = [1, 2, 3, 4, 5]
# result_lst = lst * 2

# print(result_lst)

#numpy 벡터곱
# numpy_array = np.array([1, 2, 3, 4, 5])
# result_array = numpy_array * 2
# print(result_array)













