# Car Fleet

## Problem Statement
There are `n` cars going to the same destination along a one-lane road. The cars are numbered from 1 to `n`, and each car has a position `position[i]` and a speed `speed[i]`. The task is to find the number of car fleets, which is defined as a group of cars that will arrive at the destination at the same time. A car will catch up to another car if and only if the car behind is faster than the car in front. The positions and speeds of the cars are given as two separate arrays.

## Approach
The algorithm uses a stack to keep track of the cars that will not be caught by any other car. We sort the cars by their positions in descending order and then iterate over the sorted cars, pushing each car onto the stack if it will not be caught by the car at the top of the stack.

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
        // Sort the cars by their positions in descending order
        sort(cars.begin(), cars.end(), greater<pair<int, int>>());
        stack<double> st;
        for (auto& car : cars) {
            double time = (double)(target - car.first) / car.second;
            // If the stack is empty or the current car will not be caught by the car at the top of the stack, push it onto the stack
            if (st.empty() || time > st.top()) {
                st.push(time);
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
- Use a stack to keep track of the cars that will not be caught by any other car.
- Sort the cars by their positions in descending order to ensure that we process the cars from the front to the back.
- Calculate the time it takes for each car to reach the destination and push it onto the stack if it will not be caught by the car at the top of the stack.