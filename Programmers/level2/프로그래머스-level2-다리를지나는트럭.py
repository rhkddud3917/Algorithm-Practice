# -*- coding: utf-8 -*-
# 트럭은 한 번에 1만큼 움직인다 다리에 완벽히 올라와있는 트럭만 무게를 적용한다.
# 다리의 길이와 견딜 수 있는 무게, 트럭의 무게가 주어진다.
# 모든 트럭이 다리를 건너는 시간을 출력

def solution(bridge_length, weight, truck_weights):
    time = 0
    front = -1
    rear = 0
    on = 0
    state = []
    for el in range(0,len(truck_weights)):
        state.append(0)

    while True:
        #print("time: " + str(time) + " front: " + str(front) + " rear: " + str(rear))
        #print(state)
        if rear == len(truck_weights):
            break
        if state[rear] == bridge_length:
            on -= truck_weights[rear]
            rear += 1
        if front < len(truck_weights)-1 :
            if on + truck_weights[front+1] <= weight:
                on += truck_weights[front+1]
                front += 1
        for i in range(rear , front+1):
            state[i] += 1
        time += 1
    return time

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))