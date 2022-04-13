# 돌 구매 (game_start)
# 다 깎음 (game_end)
# 옵션 3개 랜덤 + 디버프 옵션 1개 (4개 중 1개)

# if 7/7, 9/6 = 제법인데?
# if 9/7, 9/8, 9/9, 10/10 = 축하합니다
# else = 안녕 흑우?

import random
def game_start():
  print("Start Game")

def game_over():
  print("Game over")

def in_game():
  
  stone_negative =["Atk.PowerReduction", "DefenseReduction", "MoveSpeedReduction", "Atk.SpeedReduction"]

  N = stone_negative

  for bad in range(1):
    n = random.sample(N, 1)
      
  

  class limiterror(Exception):
    def __init__(self,msg):
      self.msg = msg
    def __str__(self):
      return self.msg
  
    
  print("Write first ability improvement option")
  option1 = input()
  print("Write second ability improvement option")
  option2 = input()
  print("Reduced ability is chosen by random.{0}".format(n[0]))

  print("Choice complete")
  print(option1)
  print(option2)
  print("{0}".format(n[0]))

  
  chance = 0.75
  trying = 30
  option1_t= 10
  option2_t= 10
  option3_t= 10

  result_1 = []
  result_2 = []
  result_3 = []

  
  # 기왕이면 남은횟수 표시가 input 글자수와 상관없이 같이 몰려있으면 좋겠음



  while trying > 0:
      rate=random.random()

      try:
        choice = int(input())
        if rate < chance:
          result = "O"
          chance -= 0.1
          if chance <= 0.25:
            chance = 0.25
          

        else:
          result = "X"
          chance += 0.1
          if chance >= 0.75:
            chance = 0.75

        
          
        if choice == 1:
          trying -= 1
          option1_t -= 1
          result_1.append(result)
          if option1_t < 0:
            option1_t = 0
            if choice == 1:
              trying += 1
              result_1.pop()
              raise limiterror("")
           

          print("First rate 75.0%, Success rate {0}%.".format(round(chance*100,0)))
          print(option1,result_1,"\t\t\t({0} choices left)".format(option1_t))
          print(option2,result_2,"\t\t\t({0} choices left)".format(option2_t))
          print(n[0],result_3,"\t\t\t({0} choices left)".format(option3_t))
          print("Total {0} choices left".format(trying))
          
      
            
        
        elif choice == 2:
          trying -= 1
          option2_t -= 1
          result_2.append(result)
          if option2_t < 0:
            option2_t = 0
            if choice == 2:
              trying += 1
              result_2.pop()
              raise limiterror("")
            

          print("First rate 75.0%, Success rate {0}%.".format(round(chance*100,0)))
          print(option1,result_1,"\t\t\t({0} choices left)".format(option1_t))
          print(option2,result_2,"\t\t\t({0} choices left)".format(option2_t))
          print(n[0],result_3,"\t\t\t({0} choices left)".format(option3_t))
          print("Total {0} choices left".format(trying))



        elif choice == 3:
          trying -= 1
          option3_t -= 1
          result_3.append(result)
          if option3_t < 0:
            option3_t = 0
            if choice == 3:
              trying += 1
              result_3.pop()
              raise limiterror("")
            

          print("First rate 75.0%, Success rate {0}%.".format(round(chance*100,0)))
          print(option1,result_1,"\t\t\t({0} choices left)".format(option1_t))
          print(option2,result_2,"\t\t\t({0} choices left)".format(option2_t))
          print(n[0],result_3,"\t\t\t({0} choices left)".format(option3_t))
          print("Total {0} choices left".format(trying))
        

        
          


        else:
          raise ValueError

      except limiterror:
        print("Ten times limit")

      except ValueError:
        print("Don't do any stupid")

  print("Final Result")
  print("Number means how many time you have successfully facet")
  print(option1, result_1.count("O"))
  print(option2, result_2.count("O"))
  print(n[0], result_3.count("O"))
      


def retry():
  print("Wanna retry? The answer must be 'y' or 'n'")

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
      print("Don't do any stupid")
    
    

game_start()
in_game()
retry()







# while

#   print("니놈의 돌은 ")
#     while 
#     if :
#       print("제법인데?")
#     elif :
#       print("축하합니다")
#     else:
#       print("안녕 흑우?")
   
  
 

#   trying=input()
#   game_over()






# print("니놈의 돌은 \n{0}\n{1}\n{2}다.".format(p[0],p[1],n[0]))


# while(True):
#   try:
#     print("골라")
#     choice = int(input())
#     if 1== choice:
#       print(p[0])
#     if 2== choice:
#         print(p[1])
#     if 3== choice:
#         print(n[0])
#     elif choice:
#       raise Gameovererror
#     else:
#       raise ValueError

#   except ValueError:
#     print("병신짓 하지마라")
  
#   except Gameovererror:
#     print("돌깎기 완료")
#     break
  
# print("리트?")


# game_over()





# import random
# ras=1.0 #성공확률 성공 할 때마다 현재 성공률이 0.95배가 됨
# print('0을 입력하면 멈춤')
# ch=input()
# while ch != '0':
#     rate=random.random()
#     if rate < ras:
#         print('성공',end='')
#         ras=ras*0.95
#     else:
#         print('실패',end='')
#     ch=input()


