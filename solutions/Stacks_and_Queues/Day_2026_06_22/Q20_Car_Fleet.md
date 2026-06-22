# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. Each car has a constant position and speed. The destination is target miles away. The task is to find the number of car fleets that will arrive at the destination. A car fleet is defined as a group of cars that will arrive at the destination at the same time. The position and speed of each car are given in an array of pairs, where the first element of the pair is the position and the second element is the speed. The position is the distance from the starting point to the car, and the speed is the speed of the car.

## Approach
The algorithm sorts the cars by their positions in descending order. Then, it iterates through the sorted cars and checks if the current car can catch up to the previous car. If it can, it means they will arrive at the same time and are part of the same fleet.

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
        sort(cars.begin(), cars.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.first > b.first;
        });
        int fleets = 0;
        double maxTime = 0.0;
        for (int i = 0; i < n; i++) {
            double time = (double)(target - cars[i].first) / cars[i].second;
            // If the current car's time is greater than the maxTime, it means it will arrive later
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
- Sort the cars by their positions to simulate the process of cars catching up to each other.
- Use a variable to keep track of the maximum time of the previous fleet to determine if the current car will arrive later.