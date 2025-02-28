import math

def wealthiest_customer(accounts):
    
    answer = [-1,-1]
    max_amount = -math.inf
    for i in range(len(accounts)):

        s = 0

        for amount in accounts[i]:
            s += amount


        if s > max_amount:
            
            max_amount = s
            answer = [i,s]


    return answer

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
print(wealthiest_customer(accounts))

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
print(wealthiest_customer(accounts))

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
print(wealthiest_customer(accounts))