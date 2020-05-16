def solution(A, B):
    survivals = 0
    stack = []
    for idx in range(len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    break
                else:
                    stack.pop()
                         
            else:
                survivals += 1
        else:
            stack.append(A[idx])
             
    survivals += len(stack)
    return survivals
	
#example : 8 fishes will remain
A=[78, 43, 22, 3, 59, 82, 61, 64, 20, 32, 51, 81, 92, 34, 96, 76, 100, 89, 36, 62, 71, 86, 37, 94, 28, 93, 67, 16, 30, 24, 40, 90, 55, 97, 58, 77, 18, 46, 39, 95, 13, 72, 44, 8, 2, 11, 54, 47, 19, 98]
B=[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0]
print(str(solution(A,B)))