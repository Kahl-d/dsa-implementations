
# accepts an integer n
# returns sum of the digits of n


def sum_of_digits(num):
    
    sum = 0

    while num:
        sum += num%10
        num = num//10


    return sum




num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))