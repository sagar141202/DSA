# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n - 1. Each car has a position and a speed. The position of the car is a non-negative integer, and the speed of the car is a positive integer. The destination is target miles away. The car fleet is formed when every car on the road is either in the fleet or behind a car in the fleet. A car is considered to be in the fleet if it is the lead car or if the car behind it is in the fleet and the car behind it will arrive at the destination before or at the same time as the current car. The task is to find the number of car fleets that will arrive at the destination.

## Approach
The algorithm uses a stack to keep track of the cars in the fleet. The stack is ordered by the arrival time of the cars. If a car arrives at the same time or earlier than the car at the top of the stack, it is pushed onto the stack. Otherwise, the car at the top of the stack is popped and the new car is pushed onto the stack.

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
        // Combine position and speed into a vector of pairs
        vector<pair<int, int>> cars;
        for (int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }
        
        // Sort the cars by position in descending order
        sort(cars.begin(), cars.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.first > b.first;
        });
        
        // Initialize the stack with the first car
        stack<double> stack;
        stack.push((double)(target - cars[0].first) / cars[0].second);
        
        // Iterate over the rest of the cars
        for (int i = 1; i < cars.size(); i++) {
            // Calculate the arrival time of the current car
            double arrivalTime = (double)(target - cars[i].first) / cars[i].second;
            
            // If the current car arrives after the car at the top of the stack, push it onto the stack
            if (arrivalTime > stack.top()) {
                stack.push(arrivalTime);
            }
        }
        
        // The number of fleets is equal to the size of the stack
        return stack.size();
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
- The cars are sorted by position in descending order to ensure that the cars at the front of the road are processed first.
- The stack is used to keep track of the cars in the fleet, and the size of the stack is equal to the number of fleets.
- The arrival time of each car is calculated and compared to the arrival time of the car at the top of the stack to determine whether it should be pushed onto the stack.