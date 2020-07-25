def solution(answers):
    answer = []
    temp = []
    a1 = [1,2,3,4,5]
    count1 = 0
    a2 = [2,1,2,3,2,4,2,5]
    count2 = 0
    a3 = [3,3,1,1,2,2,4,4,5,5]
    count3 = 0
    for i in range(0, len(answers), 1):
        if a1[i%5] == answers[i]:
            count1 += 1
    for i in range(0, len(answers), 1):
        if a2[i%8] == answers[i]:
            count2 += 1
    for i in range(0, len(answers), 1):
        if a3[i%10] == answers[i]:
            count3 += 1

    temp.append(count1) 
    temp.append(count2) 
    temp.append(count3)
    temp1 = temp[:]
    temp.sort()
    max = temp[2] 
    for i in range(0, 3, 1):
        if max == temp1[i]:
            answer.append(i+1)
    

    return answer

print(solution([1,3,2,4,2]))