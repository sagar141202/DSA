# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n - 1. Each car has a position and a speed. The position of the car is given by the array position, and the speed of the car is given by the array speed. If a car is overtaken by another car, it will stop and follow the other car. What is the number of car fleets that will arrive at the destination? The position and speed of each car is given as position[i] and speed[i] respectively. The destination is at position target. 1 <= n <= 10^4, 0 <= position[i], speed[i] <= 10^6, 1 <= target <= 10^6.

## Approach
The algorithm sorts the cars based on their positions in descending order. Then it iterates over the sorted cars, calculating the time it takes for each car to reach the destination. If the current car's time is less than the previous car's time, it means the current car will be overtaken and won't form a new fleet.

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
        sort(cars.begin(), cars.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.first > b.first;
        });
        
        int fleets = 0;
        double maxTime = 0.0;
        
        // Iterate over the sorted cars
        for (int i = 0; i < n; i++) {
            double time = (double)(target - cars[i].first) / cars[i].second;
            
            // If the current car's time is greater than the previous car's time, it forms a new fleet
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
- Sort the cars based on their positions to efficiently calculate the time it takes for each car to reach the destination.
- Use a variable to keep track of the maximum time it takes for a car to reach the destination, and increment the fleet count whenever a car's time is greater than the maximum time.
- Calculate the time it takes for each car to reach the destination using the formula time = (target - position) / speed.