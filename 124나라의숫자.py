def solution(n):
    answer = 0
    """
        나머지 0 일때 4
        나머지 1 일때 1
        나머지 2 일때 2
        
    """
    arr123 = [4, 1, 2]
    temp = []
    if(n==0):
        return 0
    
    while(1):
        na = n%3
        temp.append(arr123[na])
        n = int(n/3)
        if(na==0):
            n -= 1
        if(n<=0):
            break
    temp.reverse()
    
    for i in range(0, len(temp), 1):
        answer += temp[i]
        if(i != (len(temp)-1)):
            answer *= 10
    answer = str(answer)
    
    return answer
    
print(solution(13))