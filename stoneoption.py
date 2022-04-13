import random

# stone_positive =["각성", "선수필승", "예리한 둔기", "원한", "구슬동자", "중갑 착용", "최대 마나 증가",
#   "탈출의 명수", "급소 타격", "슈퍼 차지", "실드 관통", "강령술", "강화 방패", "결투의 대가",
#   "굳은 의지", "기습의 대가", "긴급구조", "달인의 저력", "돌격대장", "마나 효율 증가", "마나의 흐름",
#   "바리케이드", "번개의 분노", "부러진 뼈", "분쇄의 주먹", "불굴", "속전속결", "승부사",
#   "시선 집중", "아드레날린", "안정된 상태", "약자 무시", "에테르 포식자", "여신의 가호",
#   "위기 모면", "저주받은 인형", "전문의", "정기 흡수", "정밀 단도", "질량 증가", "추진력", "타격의 대가",
#   "폭발물 전문가"]

# stone_negative =["공격력 감소", "방어력 감소", "이동속도 감소", "공격속도 감소"]

# P = stone_positive
# N = stone_negative

# for good in range(1):
#   p = random.sample(P, 2)
#   print(f'{p}')

# for bad in range(1):
#   n = random.sample(N, 1)
#   print(f'{n}')

# P = random.sample(p, 2)

# lottery = good, bad

# for stone in lottery:
#   print("뽑기 완료. 당신의 돌은 {0},{1},{2} 이다.".format(good,good,bad))


# for good in range(1):
#   p = random.sample(P, 2)

# for bad in range(1):
#   n = random.sample(N, 1)
  
# print("니놈의 돌은 \n{0}\n{1}\n{2}다.".format(p[0],p[1],n[0]))


# def game(level, printBridge):
#     res = []
#     player = 1
#     for i in range(level):
#         isBroke = random.randrange(2)
#         if isBroke:
#             res.append(True)
#             player += 1
#         else:
#             res.append(False)
    
#     if printBridge:
#         for isBroke in res:
#             if isBroke:
#                 print("X", end=" ")
#             else:
#                 print("O", end=" ")
    
#     return player

# game(18,True)


import random
# success=0.75 #성공확률 성공 할 때마다 현재 성공률이 0.95배가 됨
# print('0을 입력하면 멈춤')
# trying=input()
# while trying != '0':
#     rate=random.random()
#     if rate < success:
#         print('0',end='')
#         success=success*0.9
#     else:
#         print('x',end='')
#         success=success*1.1
#     trying=input()

# chance = 0.75
# rate=random.random()
# choice = int(input())


# if rate < chance:
#   result = "O"
#   chance -= 0.1
#   if chance <= 0.25:
#     chance = 0.25
        

# else:
#   result = "X"
#   chance += 0.1
#   if chance >= 0.75:
#     chance = 0.75


# option1 = []
# option2 = []
# option3 = []
# if choice == 1:
#   option1.append(result)

# if choice == 2:
#   option2.append(result)

# if choice == 3:
#   option3.append(result)

# if choice == 1:
#   print(option1)
#   print(option2)
#   print(option3)

# if choice == 2:
#   print(option1)
#   print(option2)
#   print(option3)

# if choice == 3:
#   print(option1)
#   print(option2)
#   print(option3)

# from io import StringIO

# def return_print(*message):
#     io = StringIO()
#     print(*message, file=io, end="")
#     return io.getvalue()

# wow = return_print("하하", "호호", "히히")
# print(wow)


# value = []

# def game_start():
#   print("돌을 깎으러 왔는가? 게임을 시작하지.")

# def game_over():
#   print("이대로 빤스런을 한다고? 쫄았다면 어쩔수 없지.")

# def in_game():
  
#   stone_negative =["공격력 감소", "방어력 감소", "이동속도 감소", "공격속도 감소"]

#   N = stone_negative

#   for bad in range(1):
#     n = random.sample(N, 1)
      
#   class Gameovererror(Exception):
#     def __init__(self,msg):
#       self.msg = msg
#     def __str__(self):
#       return self.msg

#   class limiterror(Exception):
#     def __init__(self,msg):
#       self.msg = msg
#     def __str__(self):
#       return self.msg

#   class sapjilerror(Exception):
#     def __init__(self,msg):
#       self.msg = msg
#     def __str__(self):
#       return self.msg
    
#   print("첫번째 돌 옵션을 골라라")
#   option1 = input()
#   print("두번째 돌 옵션을 골라라")
#   option2 = input()
#   print("디버프는 내 마음대로 하겠다 디버프는 {0}이다.".format(n[0]))

#   print("돌이 결정되었다.")
#   print(option1)
#   print(option2)
#   print("{0}".format(n[0]))

#   # 30회 제한
#   chance = 0.75
#   trying = 30
#   option1_t= 10
#   option2_t= 10
#   option3_t= 10

#   result_1 = []
#   result_2 = []
#   result_3 = []

#   # valueerror가 1, 2만 선택하면 지랄남
#   # 기왕이면 남은횟수 표시가 input 글자수와 상관없이 같이 몰려있으면 좋겠음



#   while trying > 0:
#       rate=random.random()
          
#       try:
#         choice = str(input())
#         if rate < chance:
#           result = "O"
#           chance -= 0.1
#           if chance <= 0.25:
#             chance = 0.25
          

#         else:
#           result = "X"
#           chance += 0.1
#           if chance >= 0.75:
#             chance = 0.75

        
          
#         if choice == str(1):
#           trying -= 1
#           option1_t -= 1
#           result_1.append(result)
#           if option1_t < 0:
#             option1_t = 0
#             if choice == str(1):
#               trying += 1
#               result_1.pop()
#               raise limiterror("")

#           print("시작 확률 75.0%, 현재 확률 {0}%.".format(round(chance*100,0)))
#           print(option1,result_1,"\t\t\t(남은 횟수 {0}회)".format(option1_t))
#           print(option2,result_2,"\t\t\t(남은 횟수 {0}회)".format(option2_t))
#           print(n[0],result_3,"\t\t\t(남은 횟수 {0}회)".format(option3_t))
#           print("총 남은 횟수 {0}회".format(trying))
      
            
        
#         if choice == str(2):
#           trying -= 1
#           option2_t -= 1
#           result_2.append(result)
#           if option2_t < 0:
#             option2_t = 0
#             if choice == str(2):
#               trying += 1
#               result_2.pop()
#               raise limiterror("")

#           print("시작 확률 75.0%, 현재 확률 {0}%.".format(round(chance*100,0)))
#           print(option1,result_1,"\t\t\t(남은 횟수 {0}회)".format(option1_t))
#           print(option2,result_2,"\t\t\t(남은 횟수 {0}회)".format(option2_t))
#           print(n[0],result_3,"\t\t\t(남은 횟수 {0}회)".format(option3_t))
#           print("총 남은 횟수 {0}회".format(trying))



#         if choice == str(3):
#           trying -= 1
#           option3_t -= 1
#           result_3.append(result)
#           if option3_t < 0:
#             option3_t = 0
#             if choice == str(3):
#               trying += 1
#               result_3.pop()
#               raise limiterror("")

#           print("시작 확률 75.0%, 현재 확률 {0}%.".format(round(chance*100,0)))
#           print(option1,result_1,"\t\t\t(남은 횟수 {0}회)".format(option1_t))
#           print(option2,result_2,"\t\t\t(남은 횟수 {0}회)".format(option2_t))
#           print(n[0],result_3,"\t\t\t(남은 횟수 {0}회)".format(option3_t))
#           print("총 남은 횟수 {0}회".format(trying))


#         if trying == 0:
#           raise Gameovererror("돌깎기 완료")

#         if choice >= str(4):
#           raise ValueError


#       except limiterror:
#         print("10회 제한")

#       except ValueError:
#         print("병신짓 하지마라")
      
        
#       except Gameovererror:
#         print("돌깎기 완료")
#         print(option1,result_1.count("O"))
#         print(option2,result_2.count("O"))
#         print(n[0],result_3.count("O"))

def game_start():
  print("게임을 시작하지")
def in_game():
  print("게임중")
def game_over():
  print("빤쓰런 ㅋ")
def retry():
  print("리트? 대답은 y 나 n으로 하도록")

  decision = "Unknown"
  yes = "y"
  no = "n"
  answer = yes + no

  while answer:
    try:
      decision = input()
      if decision == yes:
        game_start()
        in_game()
        retry()
        break
      

      elif decision == no:
        game_over()
        break

      else:
        raise ValueError

    except ValueError:
      print("또 지랄이네")

retry()


# except Gameovererror:
#         print("돌깎기 완료")
#         print(option1,result_1.count("O"))
#         print(option2,result_2.count("O"))
#         print(n[0],result_3.count("O"))