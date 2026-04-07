# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n - 1. Each car has a position (in miles) and a speed (in miles per hour). The goal is to find the number of car fleets that will arrive at the destination. A car fleet is defined as a group of cars that will arrive at the destination at the same time. The position and speed of each car are given in two arrays, position and speed, where position[i] and speed[i] represent the position and speed of the ith car. Assume that the destination is at position 0.

## Approach
The approach to solve this problem is to use a stack to keep track of the cars that will arrive at the destination at the same time. We sort the cars based on their positions and then iterate over them. If the current car will arrive at the destination before the car at the top of the stack, we push it to the stack.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, int>> cars;
        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.begin(), cars.end(), [](auto& a, auto& b) {
            return a.first > b.first;
        });
        int fleets = 0;
        double arrivalTime = 0;
        for (auto& car : cars) {
            double time = (double)(target - car.first) / car.second;
            if (time > arrivalTime) {
                fleets++;
                arrivalTime = time;
            }
        }
        return fleets;
    }
};
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
```

## Key Takeaways
- Sort the cars based on their positions to ensure that we process the cars that are closer to the destination first.
- Use a stack or a variable to keep track of the arrival time of the previous car fleet.
- Calculate the arrival time of each car and compare it with the arrival time of the previous car fleet to determine if it will arrive at the same time.