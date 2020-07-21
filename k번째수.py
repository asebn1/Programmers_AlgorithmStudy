def solution(array, commands):
    answer = []
    temp = []
    ind = []
    for i in range(0, len(commands), 1):
        temp.append(array[commands[i][0]-1:commands[i][1]])
        ind.append(commands[i][2])
    for i in range(0, len(temp), 1):
        temp[i].sort()
    
    for i in range(0, len(temp), 1):
        answer.append(temp[i][ind[i]-1])
    

    return answer
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))