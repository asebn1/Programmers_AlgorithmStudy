def solution(n, lost, reserve):
    answer = 0
    temp = [1] * n
    for i in range(0, len(lost), 1):
        temp[lost[i]-1] -= 1

    for i in range(0, len(reserve), 1):
        temp[reserve[i]-1] += 1

    for i in range(0, n, 1):
        if temp[i] > 1:
            if i==0:
                if temp[i+1]==0:
                        temp[i] -= 1
                        temp[i-1] += 1
            elif i==(n-1):
                if temp[i-1]==0:
                        temp[i] -= 1
                        temp[i-1] += 1
            else:
                if temp[i-1]==0:
                    temp[i] -= 1
                    temp[i-1] += 1
                elif temp[i+1]==0:
                    temp[i] -= 1
                    temp[i+1] += 1

    
    for i in range(0, n, 1):
        if(temp[i]>0):
            answer += 1

    return answer
    
print(solution(3,[3],[1]))