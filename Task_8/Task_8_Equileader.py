def solution(A):
    remaining_leaders = 0
    stack =[]
    leader_count=0
    total=0
    slicing=0
    for i in (A):
        if(len(stack)==0):
            stack.append(i)
        else:
            if stack[-1]==i:
                stack.append(i)
            else:
                stack.pop()
    if(len(stack)):
        leader = stack.pop()
    else:
        leader = 1000000001
    for i in range(len(A)):
        if(leader==A[i]):
            total+=1
    for i in range(len(A)):
        if (leader == A[i]):
            leader_count+=1
        remaining_leaders=total-leader_count
        if remaining_leaders>(len(A)-i-1)/2 and leader_count>(i+1)/2:
            slicing+=1
    return slicing