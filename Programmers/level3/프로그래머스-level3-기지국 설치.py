# -*- coding: utf-8 -*-

def solution(n, stations, w):
    station_index = 0
    start = 1
    count = 0
    while(start <= n):
        if(station_index == len(stations)):
            target = n+1
            if ((target - start) % (2 * w + 1) == 0):
                count += (target - start) // (2 * w + 1)
            else:
                count += (target - start) // (2 * w + 1) + 1
            return count
        else:
            target = stations[station_index]-w
        if((target-start)%(2*w+1) == 0):
            count += (target-start)//(2*w+1)
        else:
            count += (target-start)//(2*w+1) + 1
        print(count)
        # 점프
        for i in range(station_index, len(stations)):
            if(i == len(stations)-1):
                if(stations[i]+w >= n):
                    return count
                else:
                    start = stations[i]+w+1
                    station_index = i+1
                    break
            if(stations[i+1]-stations[i] - 1 > 2 * w):
                start = stations[i]+w+1
                station_index = i+1
                break


    return count