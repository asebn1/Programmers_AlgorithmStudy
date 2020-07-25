
import collections

# collections 사용하면 - 사용 가능
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))