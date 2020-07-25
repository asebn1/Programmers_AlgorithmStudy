
import collections

def solution(participant, completion):
    # collections 사용하면 - 사용 가능
    answer = collections.Counter(participant) - collections.Counter(completion)
    # 딕셔너리 형태를 리스트로 변환 후 출력
    return list(answer.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))