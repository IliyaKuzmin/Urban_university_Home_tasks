#!/usr/bin/python3
my_list=[42,69,322,13,0,99,-5,9,8,7,-6,5]
index_in_list=0
while (index_in_list<len(my_list)):
	if my_list[index_in_list] < 0:
		break
	elif my_list[index_in_list] == 0:
		index_in_list=index_in_list+1
		continue
	else : print (my_list[index_in_list])
	index_in_list=index_in_list+1