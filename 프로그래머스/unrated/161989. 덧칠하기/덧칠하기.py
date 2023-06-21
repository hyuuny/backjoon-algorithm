from collections import deque

def solution(n, m , section):
    
    answer = 0					
    section = deque(section)	
    
    while section:
        start = section.popleft()
        
        while section and start + m > section[0]: 
            section.popleft()
        answer += 1
    
    return answer


print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))
