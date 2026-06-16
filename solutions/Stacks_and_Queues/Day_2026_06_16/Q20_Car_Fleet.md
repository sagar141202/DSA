# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n-1. Each car has a position and a speed. The position is the distance from the destination, and the speed is the speed at which the car is traveling. A car fleet is when a car catches up with the car in front of it and they become a single fleet. If car i catches up with car j, then the fleet will have the position and speed of car j. Given the positions and speeds of the cars, determine how many car fleets will arrive at the destination. The input positions and speeds are given as two separate arrays, where positions[i] is the position of car i and speeds[i] is the speed of car i.

## Approach
To solve this problem, we can use a stack-based approach, sorting the cars by their positions and then iterating over them to determine which cars will catch up to the car in front of them. We calculate the time it takes for each car to reach the destination and compare it with the time of the car in front of it.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& positions, vector<int>& speeds) {
        int n = positions.size();
        vector<pair<int, int>> cars;
        for (int i = 0; i < n; i++) {
            cars.push_back({positions[i], speeds[i]});
        }
        // sort the cars by their positions in descending order
        sort(cars.begin(), cars.end(), greater<pair<int, int>>());
        stack<double> times;
        for (auto& car : cars) {
            double time = (double)(target - car.first) / car.second;
            if (times.empty() || time > times.top()) {
                times.push(time);
            }
        }
        return times.size();
    }
};
```

## Test Cases
```
Input: target = 12, positions = [10,8,0,5,3], speeds = [2,4,1,1,3]
Output: 3
Input: target = 100, positions = [0,2,4,6,8,10], speeds = [1,1,1,1,1,1]
Output: 1
```

## Key Takeaways
- Sort the cars by their positions to process them in the correct order.
- Use a stack to keep track of the times it takes for each car to reach the destination.
- Compare the times of adjacent cars to determine if they will catch up to each other.