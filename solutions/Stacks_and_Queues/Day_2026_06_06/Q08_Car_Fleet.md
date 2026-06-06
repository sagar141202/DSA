# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n-1. Each car has a position and a speed. The position is the distance from the destination, and the speed is the constant speed the car is traveling. If a car is traveling faster than the car in front of it, it will eventually catch up to the car in front. If a car catches up to another car, they will travel together as a fleet. The task is to find the number of car fleets that will arrive at the destination. The input is an array of positions and an array of speeds, both of length n. The position array is sorted in ascending order, meaning the car at index 0 is the closest to the destination.

## Approach
The algorithm uses a stack to keep track of the fleets. It iterates over the positions and speeds in reverse order. If the current car is faster than the car at the top of the stack, it is added to the stack as a new fleet. If the current car is slower than or equal to the car at the top of the stack, it is added to the existing fleet.

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
        // Combine position and speed into a vector of pairs and sort by position in descending order
        vector<pair<int, int>> cars;
        for (int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.rbegin(), cars.rend());
        
        // Initialize the stack with the first car
        stack<double> fleets;
        fleets.push((double)(target - cars[0].first) / cars[0].second);
        
        // Iterate over the rest of the cars
        for (int i = 1; i < cars.size(); i++) {
            // Calculate the time it takes for the current car to reach the target
            double time = (double)(target - cars[i].first) / cars[i].second;
            // If the current car is faster than the car at the top of the stack, add it to the stack
            if (time > fleets.top()) {
                fleets.push(time);
            }
        }
        
        // The number of fleets is the size of the stack
        return fleets.size();
    }
};
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
```

## Key Takeaways
- The key to solving this problem is to sort the cars by their positions in descending order.
- The use of a stack to keep track of the fleets simplifies the solution and reduces the time complexity to O(n).
- The solution assumes that the input arrays are valid and that the position array is sorted in ascending order.