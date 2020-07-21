def solution(heights):
    
    answer = [0]*len(heights)
    print(answer)
    heights.reverse()
    
    for i in range(0, len(heights), 1):
        for j in range(i+1, len(heights), 1):
            if(heights[i]<heights[j]):
                answer[i]=len(heights)-j
                break
        
    answer.reverse()
    
    return answer


print(solution([1,5,3,6,7,6,5]))