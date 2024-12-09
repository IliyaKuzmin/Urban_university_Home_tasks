#!/usr/bin/python3
import random
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#print(numbers[2:])
def divisor_of_a_number(number):
	divisors=[]
	num=0
	while num <= number:
		num=num+1
		if num > 1 and (number/num)%1 == 0:
			divisors.append(num)
	return divisors
# input of any type => word
def prepare_to_output(imput):
	droping_symbols=[" ",",","(",")","[","]"]
	string=str(imput)
	for sym in droping_symbols:
		string=string.replace(sym,"")
	print ("Ваш пароль: ",string)
def main(number):
	divisors=divisor_of_a_number(number)
	mid1_password=[]
	for num in divisors:
		if num == 2 :
			num=num+1
			continue
		mid_password=[]
		first=0
		while first+1 < num:
			first = first + 1
			second = num - first
			if second > first:
				mid_password.append((first,second))
		mid1_password=mid1_password+mid_password
	sorted_password=sorted(mid1_password, key=lambda x:x[0])
	prepare_to_output(sorted_password)
client_input=int(input("Загаданное число: "))
main(client_input)