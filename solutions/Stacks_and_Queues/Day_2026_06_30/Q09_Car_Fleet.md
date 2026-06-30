# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n - 1. Each car has a position (in miles) and a speed (in miles per hour). The task is to find the number of car fleets that will arrive at the destination. A car fleet is a group of cars that will arrive at the destination at the same time. The position and speed of each car are given in two separate arrays, position and speed, where position[i] is the position of the ith car and speed[i] is the speed of the ith car. The destination is at position 1000. The time it takes for a car to arrive at the destination is calculated as (1000 - position[i]) / speed[i]. If two cars have the same arrival time, they are considered to be in the same fleet.

## Approach
The approach is to sort the cars based on their positions in descending order. Then, we iterate through the sorted list and calculate the arrival time for each car. If the current car's arrival time is less than or equal to the previous car's arrival time, it means they are in the same fleet, so we skip it. Otherwise, we increment the fleet count and update the previous car's arrival time.

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
    // sort cars based on their positions in descending order
    sort(cars.begin(), cars.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.first > b.first;
    });
    int fleetCount = 0;
    double prevArrivalTime = -1;
    for (int i = 0; i < n; i++) {
        double arrivalTime = (double)(target - cars[i].first) / cars[i].second;
        if (arrivalTime > prevArrivalTime) {
            fleetCount++;
            prevArrivalTime = arrivalTime;
        }
    }
    return fleetCount;
}
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
```

## Key Takeaways
- Sort the cars based on their positions in descending order to ensure that we are considering the cars that are closest to the destination first.
- Calculate the arrival time for each car and compare it with the previous car's arrival time to determine if they are in the same fleet.
- Use a variable to keep track of the previous car's arrival time and update it whenever we encounter a new fleet.