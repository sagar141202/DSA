# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n - 1. Each car has a position and a speed. The position is the distance from the destination, and the speed is the speed at which the car is traveling towards the destination. If a car is traveling at a higher speed than the car in front of it, it will overtake the car in front. We need to find the number of car fleets that will arrive at the destination. A car fleet is a group of cars that will arrive at the destination at the same time. The input is an array of pairs, where each pair contains the position and speed of a car. The positions and speeds are non-negative integers.

## Approach
The algorithm sorts the cars based on their positions and then iterates over them. If the current car's arrival time is less than or equal to the previous car's arrival time, it means they will form a fleet. We use a stack to keep track of the fleets. The intuition is that if a car is traveling faster than the car in front of it, it will catch up and form a fleet.

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
        // Sort the cars based on their positions
        sort(cars.rbegin(), cars.rend());
        int fleets = 0;
        double arrivalTime = 0;
        for (auto& car : cars) {
            double time = (double)(target - car.first) / car.second;
            // If the current car's arrival time is greater than the previous car's arrival time, it will form a new fleet
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
- Sort the cars based on their positions to simulate the overtaking process.
- Use a variable to keep track of the previous car's arrival time to determine if a new fleet is formed.
- The time complexity is O(n log n) due to the sorting step.