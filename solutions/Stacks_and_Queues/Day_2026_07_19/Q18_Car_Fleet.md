# Car Fleet

## Problem Statement
There are `n` cars going to the same destination along a one-way road. The cars are numbered from 1 to `n`, and each car has a position `position[i]` and a speed `speed[i]`. Each car will only stop when a car in front of it stops. If a car reaches another car that has stopped, it will also stop. The destination is at position `target`. The function should return the number of car fleets, where a car fleet is a group of cars that will stop at the same position. The input will be two arrays, `position` and `speed`, and an integer `target`. The position and speed arrays will have the same length `n`, and the elements will be in the range `[0, 10^4]`. The target will be in the range `[0, 10^4]`.

## Approach
To solve this problem, we will use a stack-based approach. We will iterate over the cars in reverse order, calculating the time it takes for each car to reach the target. If the time for the current car is greater than the time for the car at the top of the stack, we will push the current car onto the stack.

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
        
        // Combine position and speed into a single vector of pairs
        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }
        
        // Sort the cars by their positions in descending order
        sort(cars.begin(), cars.end(), [](const auto& a, const auto& b) {
            return a.first > b.first;
        });
        
        int fleets = 0;
        double maxTime = 0;
        
        // Iterate over the cars and calculate the time it takes for each car to reach the target
        for (int i = 0; i < n; i++) {
            double time = (double)(target - cars[i].first) / cars[i].second;
            
            // If the time for the current car is greater than the maxTime, it will be the lead car of a new fleet
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
- The problem can be solved by iterating over the cars in reverse order and using a stack-based approach.
- The time complexity is O(n log n) due to the sorting step.
- The space complexity is O(n) for storing the combined position and speed vector.