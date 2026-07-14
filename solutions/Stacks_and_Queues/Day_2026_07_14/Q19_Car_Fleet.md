# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n - 1. Each car i has a position and a speed. The position of car i is given by position[i], and the speed of car i is given by speed[i]. The car fleet is moving in the same direction, and a car will arrive at the destination if and only if it is the leading car or the car behind it is moving slower. The task is to find the number of car fleets that will arrive at the destination. The constraints are 1 <= n <= 10^4, 0 <= position[i] <= 10^6, and 1 <= speed[i] <= 10^6.

## Approach
The algorithm sorts the cars based on their positions in descending order, then iterates through the sorted list to calculate the arrival time of each car and checks if it forms a new fleet. If a car's arrival time is less than or equal to the previous car's arrival time, it joins the previous fleet; otherwise, it forms a new fleet.

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
        sort(cars.begin(), cars.end(), greater<pair<int, int>>());
        int fleets = 0;
        double prevArrivalTime = -1;
        for (auto& car : cars) {
            double arrivalTime = (double)(target - car.first) / car.second;
            if (arrivalTime > prevArrivalTime) {
                fleets++;
                prevArrivalTime = arrivalTime;
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
- Sort the cars by their positions in descending order to process them from the front to the back.
- Use a variable to keep track of the previous car's arrival time to determine if a new fleet is formed.
- Calculate the arrival time of each car using the formula (target - position) / speed.