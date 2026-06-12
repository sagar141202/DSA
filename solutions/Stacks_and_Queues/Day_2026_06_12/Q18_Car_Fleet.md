# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n-1. Each car i has a position (in miles) and a speed (in miles per hour). The destination is at position target miles. Each car will stop when it reaches the destination. A car i will catch up to car j if and only if car i's position plus its speed times the time it travels equals car j's position plus its speed times the same amount of time. The time it takes for a car to reach the destination is the distance to the destination divided by the car's speed. If a car catches up to another car, they will form a fleet and arrive at the destination at the same time. The task is to find the number of car fleets that will arrive at the destination.

## Approach
The approach is to sort the cars based on their positions in descending order. Then, iterate over the sorted cars and calculate the time it takes for each car to reach the destination. If the current car's time is less than or equal to the previous car's time, it means the current car will catch up to the previous car and they will form a fleet. Otherwise, the current car will form a new fleet.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int carFleet(int target, vector<int>& position, vector<int>& speed) {
    int n = position.size();
    vector<pair<int, int>> cars;
    for (int i = 0; i < n; i++) {
        cars.push_back({position[i], speed[i]});
    }
    sort(cars.rbegin(), cars.rend());
    int fleets = 0;
    double prevTime = 0.0;
    for (auto& car : cars) {
        double time = (double)(target - car.first) / car.second;
        if (time > prevTime) {
            fleets++;
            prevTime = time;
        }
    }
    return fleets;
}
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Input: target = 10, position = [3], speed = [3]
Output: 1
```

## Key Takeaways
- Sort the cars based on their positions in descending order to ensure that we are always comparing the current car with the previous car that has not been caught up yet.
- Use a variable to keep track of the time it takes for the previous car to reach the destination.
- If the current car's time is greater than the previous car's time, it means the current car will not catch up to the previous car and will form a new fleet.