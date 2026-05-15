# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. Each car has a constant position and speed. The positions and speeds of the cars are given as two integer arrays `position` and `speed` of length `n`. The goal is to find the number of car fleets that will arrive at the destination. A car fleet is a group of cars that will arrive at the destination at the same time. The position of the destination is at position `target`. The position of each car is given as the distance from the destination, so a car at position 0 is already at the destination.

## Approach
The approach is to sort the cars based on their positions and then iterate through the sorted list to find the number of fleets. We can use a stack to keep track of the fleets. For each car, if it will arrive at the destination before the current fleet, we create a new fleet.

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
        sort(cars.rbegin(), cars.rend());
        int fleets = 0;
        double arriveTime = 0;
        for (auto& car : cars) {
            double time = (double)(car.first) / car.second;
            if (time > arriveTime) {
                fleets++;
                arriveTime = time;
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
Input: target = 10, position = [3], speed = [3]
Output: 1
```

## Key Takeaways
- Sort the cars based on their positions to simplify the problem.
- Use a variable to keep track of the arrival time of the current fleet.
- If a car will arrive at the destination before the current fleet, create a new fleet.