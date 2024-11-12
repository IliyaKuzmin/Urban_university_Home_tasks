#!/usr/bin/python3
calls=0
def count_calls():
	global calls
	calls+=1
def string_info(string):
	count_calls()
	return (len(string),string.upper(),string.lower())
def is_contains(string,list_to_search):
	listing=[]
	count_calls()
	for item in list_to_search:
		listing.append(item.lower())
	return string.lower() in listing
print(is_contains("Cat",["dog","cAT"]))
print(is_contains("Cat",["dog","pAT"]))
print(string_info("Pottery"))
print(string_info("Europe"))