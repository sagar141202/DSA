# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n-1. Each car has a position and a speed. The position of the car is given by the array position, and the speed of the car is given by the array speed. If a car A catches up to another car B, then car A and car B will form a fleet. The task is to find the number of fleets that will be formed. The constraints are: 1 <= n <= 10^4, 1 <= position.length == speed.length == n <= 10^4, 0 <= position[i], speed[i] <= 10^6.

## Approach
To solve this problem, we use a stack-based approach. We first sort the cars based on their positions. Then we iterate over the sorted cars and for each car, we check if it can catch up to the car at the top of the stack. If it can, we pop the car from the stack. If it cannot, we push the car onto the stack.

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
        
        // Create a vector of pairs, where each pair contains the position and speed of a car
        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }
        
        // Sort the cars based on their positions
        sort(cars.begin(), cars.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.first > b.first;
        });
        
        int fleets = 0;
        double maxTime = 0.0;
        
        // Iterate over the sorted cars
        for (int i = 0; i < n; i++) {
            double time = (double)(target - cars[i].first) / cars[i].second;
            
            // If the current car cannot catch up to the car at the top of the stack, increment the fleet count and update the max time
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
- The problem can be solved using a stack-based approach.
- The cars need to be sorted based on their positions before iterating over them.
- The time complexity of the solution is O(n log n) due to the sorting step.