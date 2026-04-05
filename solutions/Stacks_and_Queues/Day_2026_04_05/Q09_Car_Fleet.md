# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 1 to n, and each car has a position (in miles) and a speed (in miles per hour). The target is to find the number of car fleets that will arrive at the destination. A car fleet is defined as a group of cars that will arrive at the destination at the same time. The position and speed of each car are given in two arrays, position and speed, where position[i] is the position of the ith car and speed[i] is the speed of the ith car. The length of the road is target miles.

## Approach
To solve this problem, we can use a stack data structure to keep track of the cars that will arrive at the destination at the same time. We can iterate over the cars from the destination to the starting point, and for each car, we can calculate its arrival time. If the current car's arrival time is less than or equal to the arrival time of the car at the top of the stack, we can pop the car from the stack because it will not be the leader of a fleet.

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
        // Sort the cars based on their positions in descending order
        sort(cars.begin(), cars.end(), greater<pair<int, int>>());
        int fleets = 0;
        double arrivalTime = 0.0;
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
- Use a stack data structure to keep track of the cars that will arrive at the destination at the same time.
- Sort the cars based on their positions in descending order to process them from the destination to the starting point.
- Calculate the arrival time of each car and compare it with the arrival time of the car at the top of the stack to determine if it will be the leader of a fleet.