def defuse(code, k):
    l = len(code)
    answer = [0 for i in range(len(code))]

    if k == 0:
        return answer
    
    if k < 0:
        k = k * -1
        sum = 0
        count = 0
        for i in range(0,l+k+1,1):
            if count < k:
                sum += code[i%l]
                count += 1

            else:
                answer[i%l] = sum
                sum = sum - code[(i-k)%l] + code[i%l]

        return answer

    if k > 0:

        sum = 0
        count = 0
        for i in range(len(code)-1, 0-k-1,-1):
            if count < k:
                sum += code[i%l]
                count += 1

            else:
                answer[i%l] = sum
                sum = sum - code[(i+k)%l] + code[i%l]
                

        return answer



code = [5, 7, 1, 4]
k = 3
print(defuse(code, k))

code = [1, 2, 3, 4]
k = 0
print(defuse(code, k))

code = [2, 4, 9, 3]
k = -2
print(defuse(code, k))