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


while i<10 :

	hand = input("가위바위보 중에 하나를 고르세요 (종료:x)  ")
	computerhand = random.choice(computer)

	if hand == "가위" :
		if computerhand == "가위":
			print("컴퓨터 : 가위")
			print("무승부입니다.")
			i++
		elif computerhand == "바위" :
			print("컴퓨터 : 바위")
			print("컴퓨터가 이겼습니다.")
			i++
		else :
			print("컴퓨터 : 보")
			print("플레이어가 이겼습니다.")
			playerwin += 1
			i++
	elif hand == "바위" :
		if computerhand == "가위":
			print("컴퓨터 : 가위")
			print("플레이어가 이겼습니다.")
			playerwin += 1
			i++
		elif computerhand == "바위":
			print("컴퓨터 : 바위")
			print("무승부입니다.")
			i++
		else :
			print("컴퓨터 : 보")
			print("컴퓨터가 이겼습니다.")
			computerwin += 1
			i++
	elif hand == "보" :
		if computerhand == "가위":
			print("컴퓨터 : 가위")
			print("컴퓨터가 이겼습니다.")
			computerwin += 1
			i++
		elif computerhand == "바위":
			print("컴퓨터 : 바위")
			print("플레이어가 이겼습니다.")
			playerwin += 1
			i++
		else :
			print("컴퓨터 : 보")
			print("무승부입니다.")
			i++
print("컴퓨터 : " ,computerwin ," 플레이어 : " ,playerwin)
