# Car Fleet

## Problem Statement
There are `n` cars going to the same destination along a one-lane road. The cars are numbered from 1 to `n`, and each car has a position and a speed. The position of the `i-th` car is `position[i]`, and its speed is `speed[i]`. The task is to find the number of car fleets that will arrive at the destination. A car fleet is a group of cars that will arrive at the destination at the same time. If a car is faster than the car in front of it and can catch up to it, they will form a fleet.

## Approach
The algorithm sorts the cars based on their positions in descending order. Then it iterates over the sorted cars, and for each car, it checks if it can catch up to the car in front of it. If it can, it forms a fleet with the car in front of it. If it cannot, it forms a new fleet.

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
        // Sort the cars based on their positions in descending order
        sort(cars.begin(), cars.end(), greater<pair<int, int>>());
        int fleets = 0;
        double arrivalTime = 0;
        for (int i = 0; i < n; i++) {
            // Calculate the arrival time of the current car
            double currentTime = (double)(target - cars[i].first) / cars[i].second;
            // If the current car cannot catch up to the car in front of it, it forms a new fleet
            if (currentTime > arrivalTime) {
                fleets++;
                arrivalTime = currentTime;
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
- Sort the cars based on their positions in descending order to efficiently check if a car can catch up to the car in front of it.
- Use a variable to keep track of the arrival time of the car in front of the current car to determine if the current car forms a new fleet.
- The time complexity of the solution is O(n log n) due to the sorting operation, and the space complexity is O(n) for storing the cars.