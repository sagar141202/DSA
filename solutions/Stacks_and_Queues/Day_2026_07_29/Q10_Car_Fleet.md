# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n - 1. Each car has a position and a speed. The position of each car is given by the array position, and the speed of each car is given by the array speed. The initial distance between each car and the destination is target. The task is to find the number of car fleets that will arrive at the destination. A car fleet is defined as a group of cars that will arrive at the destination at the same time. If a car catches up to another car, they will form a fleet and arrive at the same time. The position and speed of each car are non-negative integers, and the target is a positive integer.

## Approach
We will use a stack to keep track of the cars that have not been caught by other cars. We will iterate over the cars in reverse order of their positions and calculate their arrival times. If a car's arrival time is less than or equal to the arrival time of the car at the top of the stack, we will pop the car from the stack.

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
        stack<double> st;
        for (auto& car : cars) {
            double arrivalTime = (double)(target - car.first) / car.second;
            if (st.empty() || arrivalTime > st.top()) {
                st.push(arrivalTime);
            }
        }
        return st.size();
    }
};
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
```

## Key Takeaways
- The key to solving this problem is to sort the cars based on their positions in descending order.
- We use a stack to keep track of the cars that have not been caught by other cars.
- We calculate the arrival time of each car and compare it with the arrival time of the car at the top of the stack.