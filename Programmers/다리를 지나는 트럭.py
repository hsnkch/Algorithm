from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    # 다리를 나타내는 큐
    bridge = deque(0 for _ in range(bridge_length))
    # 대기 트럭들을 나타내는 큐
    truck_weights = deque(truck_weights)  
    # 현재 다리 위의 트럭 무게 합
    bridge_weight = 0  
    
    while bridge:
        answer += 1
        
        # 다리에서 나온 트럭 무게를 빼고, 새로운 트럭을 올림
        bridge_weight -= bridge.popleft()
        
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                bridge_weight += truck_weights[0]
                bridge.append(truck_weights.popleft())
                
            # 대기 중인 트럭을 올리지 못하는 경우 무게 0을 넣어줌
            else:
                bridge.append(0)
                
    return answer

print(solution(2, 10, [7,4,5,6]))