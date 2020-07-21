def solution(arr):
    answer = []
    if(len(arr)==0):
        return answer
    answer.append(arr[0])
    count = 0
    for i in range(1, len(arr), 1):
        if(arr[i] != answer[count]):
            answer.append(arr[i])
            count += 1
    
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))