#!/usr/bin/python3
def get_multiplied_digit(number):
	int_to_str=str(number)
	first=int(int_to_str[0])
	if len(int_to_str)>1:
		return first*get_multiplied_digit(int(int_to_str[1:]))
	else:
		return first
print (get_multiplied_digit(40304))