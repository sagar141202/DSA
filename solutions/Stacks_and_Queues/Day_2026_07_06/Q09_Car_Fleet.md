# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n - 1. Each car i has a position (in miles) and a speed (in miles per hour). The target is to reach a destination at position target. The function should return the number of car fleets that will arrive at the destination. A car fleet is a group of cars that will arrive at the destination at the same time. If a car catches up to another car, they will be in the same fleet. The input is an array of positions and an array of speeds, both of length n, and the target position.

## Approach
We can solve this problem by sorting the cars based on their positions and then iterating over them. For each car, we calculate the time it will take to reach the target and compare it with the time of the previous car. If the current car will arrive earlier or at the same time as the previous car, we consider them to be in the same fleet.

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
        
        // Create a vector of pairs to store the position and speed of each car
        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }
        
        // Sort the cars based on their positions in descending order
        sort(cars.begin(), cars.end(), [](const auto& a, const auto& b) {
            return a.first > b.first;
        });
        
        int fleets = 0;
        double maxTime = 0.0;
        
        // Iterate over the sorted cars
        for (int i = 0; i < n; i++) {
            // Calculate the time it will take for the current car to reach the target
            double time = (double)(target - cars[i].first) / cars[i].second;
            
            // If the current car will arrive later than the previous car, consider it as a new fleet
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
Input: target = 10, position = [3], speed = [3]
Output: 1
```

## Key Takeaways
- Sort the cars based on their positions to efficiently compare the arrival times.
- Use a variable to keep track of the maximum time seen so far to determine if a car will arrive later than the previous car.
- The time complexity is O(n log n) due to the sorting operation.