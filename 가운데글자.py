def solution(s):
    
    #짝수 일 때
    if(len(s)%2==0):
        return s[int(len(s)/2)-1:int(len(s)/2)+1]
    #홀수 일 때
    else:
        return s[int(len(s)/2)]

print(solution("abcde"))