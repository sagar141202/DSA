# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. Each car has a constant position and speed. The goal is to find out how many car fleets will arrive at the destination. A car fleet is defined as a group of cars that will arrive at the destination at the same time. The position and speed of each car are given as an array of pairs, where the first element of the pair is the position and the second element is the speed. The destination is at position 0. The position of each car is given in descending order, and the speed of each car is given in ascending order.

## Approach
We can use a stack to solve this problem, where the stack stores the arrival time of each car. We iterate over the cars from right to left, and for each car, we calculate its arrival time. If the arrival time is less than or equal to the arrival time of the car at the top of the stack, we pop the stack until the arrival time is greater than the arrival time of the car at the top of the stack, or the stack is empty. Then, we push the arrival time of the current car into the stack.

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
        sort(cars.begin(), cars.end(), greater<pair<int, int>>());
        stack<double> stk;
        for (auto& car : cars) {
            double arrivalTime = (double)(target - car.first) / car.second;
            if (stk.empty() || arrivalTime > stk.top()) {
                stk.push(arrivalTime);
            }
        }
        return stk.size();
    }
};
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
```

## Key Takeaways
- The problem can be solved using a stack to store the arrival times of the cars.
- The key insight is that a car will arrive at the same time as the car in front of it if its arrival time is less than or equal to the arrival time of the car in front of it.
- The time complexity is O(n) due to the sorting and iteration over the cars.