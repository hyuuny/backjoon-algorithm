def solution(participant, completion):
    d = {}
    
    # d[x]가 존재하면 1을 더하고, 존재하지 않으면 0 저장
    for x in participant:
        d[x] = d.get(x, 0) + 1
        
    # 완주자는 d[x]에서 1씩 마이너스
    for x in completion:  
        d[x] -= 1
        
    dnf = [k for k, v in d.items() if v > 0]
    answer = dnf[0]
    
    return answer