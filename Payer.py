from sys import argv
#script, first, second, third = argv

first = int(argv[1])
second = int(argv[2])
third = int(argv[3])

print ("total_hours_payer: ", first)
print ("one_hour_payer: ", second)
print ("prime: ", third)

def Payer (total_hours_payer, one_hour_payer, prime):
	result = (total_hours_payer * one_hour_payer) + prime
	return result

print(Payer(first, second, third))