# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-way road. The cars are numbered from 0 to n - 1. The car i is moving at a speed of speed[i] and is at position position[i]. The cars cannot pass each other, so if a car is slower than the car in front of it, it will catch up to the car in front of it. The task is to find out how many car fleets will arrive at the destination. A car fleet is a group of cars that will arrive at the destination at the same time.

## Approach
The approach is to use a stack to keep track of the cars. We sort the cars based on their positions and then iterate over them. If the current car is faster than the car at the top of the stack, we pop the stack until we find a car that is faster than the current car or the stack is empty.

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
        sort(cars.begin(), cars.end(), [](pair<int, int>& a, pair<int, int>& b) {
            return a.first > b.first;
        });
        stack<double> stk;
        for (auto& car : cars) {
            double time = (double)(target - car.first) / car.second;
            // If the stack is empty or the current car is faster than the car at the top of the stack
            if (stk.empty() || time > stk.top()) {
                stk.push(time);
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
- Use a stack to keep track of the cars.
- Sort the cars based on their positions.
- If the current car is faster than the car at the top of the stack, pop the stack until we find a car that is faster than the current car or the stack is empty.