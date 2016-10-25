"""
Game

 * Author : 김원배
 * Created : 김원배
 * Last modified : 김원배
"""

import random

computer = ["가위","바위","보"]
computerhand = random.choice(computer)
i = 0
computerwin = 0
playerwin = 0

while True :
	hand = input("가위바위보 중에 하나를 고르세요 (종료:x)  ")

	computerhand = random.choice(computer)

	if hand == "가위" :
		if computerhand == "가위":
			print("컴퓨터 : 가위")
			print("무승부입니다.")


		elif computerhand == "바위" :
			print("컴퓨터 : 바위")
			print("컴퓨터가 이겼습니다.")
			print("--------------")
			computerwin += 1

		else :
			print("컴퓨터 : 보")
			print("플레이어가 이겼습니다.")
			print("--------------")
			playerwin += 1

	elif hand == "바위" :
		if computerhand == "가위":
			print("컴퓨터 : 가위")
			print("플레이어가 이겼습니다.")
			print("--------------")
			playerwin += 1

		elif computerhand == "바위":
			print("컴퓨터 : 바위")
			print("무승부입니다.")
			print("--------------")


		else :
			print("컴퓨터 : 보")
			print("컴퓨터가 이겼습니다.")
			print("--------------")
			computerwin += 1

	elif hand == "보" :
		if computerhand == "가위":
			print("컴퓨터 : 가위")
			print("컴퓨터가 이겼습니다.")
			print("--------------")
			computerwin += 1

		elif computerhand == "바위":
			print("컴퓨터 : 바위")
			print("플레이어가 이겼습니다.")
			print("--------------")
			playerwin += 1

		else :
			print("컴퓨터 : 보")
			print("무승부입니다.")
			print("--------------")


	elif hand == "x" :
		break
print("컴퓨터 " ,computerwin , " : ",playerwin, " 플레이어" )
