#This programm developed by Nikolaenko Oleksiy
import random

n1 = random.randint(1,20)

print("Вгадайте число від 1 до 20")

p = 0
while  p < 5:
	try:
	 	n2 = int(input("Будь-ласка введіть число : "))
	except Exception as e: 
		print("Невірне значення!")
		continue
	if n1 == n2:
		print("Ви виграли!")
		break
	elif n2 < n1:
		print("Запропоноване число менше задуманого!")
	else:
		print("Запропоноване число більше задуманого!")
	p += 1
	
if p == 5:
	print("Ви програли! Моє число", n1)
