# Car Fleet

## Problem Statement
There are `n` cars going to the same destination along a one-way road. The cars are numbered from 1 to `n`, and each car has a position `position[i]` and a speed `speed[i]`. A car fleet is defined as a group of cars that will arrive at the destination at the same time. Determine the number of car fleets that will arrive at the destination. The positions and speeds are given as two separate arrays. It is guaranteed that all positions and speeds are positive.

## Approach
The algorithm involves sorting the cars by their positions in descending order and then iterating through them to calculate their arrival times. If a car's arrival time is less than or equal to the previous car's arrival time, it will be part of the same fleet. Otherwise, it will be part of a new fleet.

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
        
        // Sort the cars by their positions in descending order
        sort(cars.begin(), cars.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.first > b.first;
        });
        
        int fleets = 0;
        double maxTime = 0.0;
        
        // Iterate through the sorted cars to calculate their arrival times
        for (int i = 0; i < n; i++) {
            double time = (double)(target - cars[i].first) / cars[i].second;
            
            // If the current car's arrival time is greater than the max time, it will be part of a new fleet
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
- Sort the cars by their positions in descending order to process them from the furthest to the closest.
- Calculate the arrival time of each car and compare it with the previous car's arrival time to determine if it will be part of the same fleet.
- Use a variable to keep track of the maximum arrival time seen so far to efficiently determine the number of fleets.