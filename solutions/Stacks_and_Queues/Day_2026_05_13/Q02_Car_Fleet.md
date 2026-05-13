# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n-1. Each car has a position (in miles) and a speed (in miles per hour). The position and speed of each car is given. A car is considered to be in a fleet if it is moving in the same direction as the previous car and the previous car has not been overtaken by the current car. The task is to find the number of car fleets that will arrive at the destination. The position of the destination is not given, but we can assume it to be a large number. The cars are initially given in the order of their positions, from the car closest to the destination to the car farthest from the destination.

## Approach
The algorithm uses a stack to keep track of the cars that have not been overtaken. We iterate over the cars from the closest to the farthest, and for each car, we check if it will overtake the car at the top of the stack. If it will, we pop the car from the stack. If it will not, we push the car onto the stack. The size of the stack at the end will be the number of car fleets.

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
        double maxTime = 0.0;
        for (int i = 0; i < n; i++) {
            double time = (double)(target - cars[i].first) / cars[i].second;
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
```

## Key Takeaways
- The problem can be solved using a simple iterative approach with a stack.
- The time complexity of the solution is O(n log n) due to the sorting of the cars.
- The space complexity of the solution is O(n) for storing the cars.