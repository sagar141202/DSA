# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n-1. The car numbered i is initially at position position[i] on the road and is traveling at speed speed[i]. The target is to find the number of car fleets that will arrive at the destination. A car fleet is formed when a car cannot catch up to another car that is ahead of it. The positions and speeds of the cars are given as two separate arrays. The length of the road is not given, but we can assume it is larger than the maximum position of the cars. We can also assume that the speeds are positive and the positions are non-negative.

## Approach
The algorithm sorts the cars by their positions in descending order. Then it iterates through the sorted list and checks if the current car can catch up to the previous car. If it cannot, a new fleet is formed.

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
        
        // Create pairs of position and speed
        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }
        
        // Sort the cars by position in descending order
        sort(cars.begin(), cars.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.first > b.first;
        });
        
        int fleets = 0;
        double maxTime = 0;
        
        // Iterate through the sorted list of cars
        for (int i = 0; i < n; i++) {
            double time = (double)(target - cars[i].first) / cars[i].second;
            
            // If the current car cannot catch up to the previous car, a new fleet is formed
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
- Sort the cars by their positions to simulate the movement of the cars.
- Use a variable to keep track of the maximum time it takes for a car to reach the target.
- If a car cannot catch up to the previous car, it forms a new fleet.