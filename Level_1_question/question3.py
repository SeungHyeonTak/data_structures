# 완주하지 못한 선수# 해시 알고리즘 사용하기def solution(participant, completion):    answer = ''  # 완주 못하면 answer에 담김    for i in range(len(completion)):        if completion[i] != participant[i + 1]:            answer = participant[i]    return answerif __name__ == "__main__":    participant = ["leo", "kiki", "eden"]  # 참가자 명단    completion = ["eden", "kiki"]  # 완주자 명단    print(solution(participant, completion))