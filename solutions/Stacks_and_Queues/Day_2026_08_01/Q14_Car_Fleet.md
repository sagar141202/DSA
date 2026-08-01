# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-way road. The cars start at the same time, but they have different speeds and starting positions. A car will catch up to and pass another car if it is faster. If a car catches up to another car, it will then travel at the same speed as the car it caught up to. The task is to find the number of car fleets that will arrive at the destination. The position and speed of each car is given as an array of pairs, where the first element of the pair is the position and the second element is the speed. The destination is at position target.

## Approach
The approach to solve this problem is to use a stack to keep track of the cars that have not been caught up to yet. We sort the cars based on their positions and then iterate over them. If a car is faster than the car at the top of the stack, we calculate the time it would take for the car to catch up to the car at the top of the stack. If this time is less than or equal to the time it would take for the car at the top of the stack to reach the destination, we pop the car from the stack.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int carFleet(int target, vector<vector<int>>& position, vector<int>& speed) {
    int n = position.size();
    vector<pair<int, int>> cars;
    for (int i = 0; i < n; i++) {
        cars.push_back({position[i], speed[i]});
    }
    sort(cars.begin(), cars.end(), [](pair<int, int> a, pair<int, int> b) {
        return a.first > b.first;
    });
    stack<double> stack;
    for (auto& car : cars) {
        double time = (double)(target - car.first) / car.second;
        if (stack.empty() || time > stack.top()) {
            stack.push(time);
        }
    }
    return stack.size();
}
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Input: target = 10, position = [3], speed = [3]
Output: 1
```

## Key Takeaways
- Sort the cars based on their positions to ensure that we are always considering the car that is closest to the destination.
- Use a stack to keep track of the cars that have not been caught up to yet.
- Calculate the time it would take for a car to catch up to the car at the top of the stack to determine if it should be popped from the stack.