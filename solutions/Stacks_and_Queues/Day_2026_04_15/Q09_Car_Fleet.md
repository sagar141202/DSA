# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n-1. Each car has a position and a speed. The position is the distance from the destination, and the speed is how fast the car is moving towards the destination. If a car is slower than the car in front of it, it will catch up to the car in front. If a car catches up to another car, they form a car fleet. The task is to find the number of car fleets that will arrive at the destination. The input is an array of positions and an array of speeds, both of length n. The positions are in descending order, and the speeds are in ascending order. For example, if the positions are [10, 8, 0, 5, 3] and the speeds are [2, 4, 1, 1, 3], the number of car fleets is 3.

## Approach
The approach is to use a stack to keep track of the cars that have not been caught up by other cars. We iterate through the positions and speeds from right to left, and for each car, we check if it will catch up to the car in front of it. If it will, we remove the car in front from the stack. If it will not, we add the current car to the stack.

## Complexity
- Time: O(n)
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
        double maxTime = 0;
        for (auto& car : cars) {
            double time = (double)(target - car.first) / car.second;
            if (time > maxTime) {
                fleets++;
                maxTime = time;
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
Input: target = 10, position = [5,4,3,2,1], speed = [1,1,1,1,1]
Output: 1
```

## Key Takeaways
- The problem can be solved by iterating through the positions and speeds from right to left and using a stack to keep track of the cars that have not been caught up by other cars.
- The time complexity is O(n) because we are iterating through the positions and speeds once.
- The space complexity is O(n) because we are using a vector to store the cars.