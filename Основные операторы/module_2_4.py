#!/usr/bin/python3
input_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sorted_input=sorted(input_numbers)
primes=[]
not_primes=[]
for item in sorted_input:
	if item == 1:
		continue
	if item > 1:
		not_prime=False
		for num in primes:
			if (item/num)%1>0:
				continue
			else: not_prime=True
		if not_prime:
			not_primes.append(item)
		else:
			primes.append(item)
print("Input: "+str(input_numbers))
print("Primes: "+str(primes))
print("Not_primes: "+str(not_primes))