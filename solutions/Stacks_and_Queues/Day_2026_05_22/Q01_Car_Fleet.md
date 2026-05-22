# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one lane road. The cars are numbered from 0 to n-1. Each car has a position and a speed. The position of the car is given by position[i] and the speed of the car is given by speed[i]. A car will arrive at the destination if its position plus its speed is greater than or equal to the destination. If a car is caught by another car, it will not arrive at the destination. We need to find the number of car fleets that will arrive at the destination. A car fleet is a group of cars that will arrive at the destination together.

## Approach
We use a stack to keep track of the cars that will arrive at the destination. We iterate over the cars in reverse order and for each car, we check if it will be caught by the car at the top of the stack. If it will be caught, we continue to the next car. If it will not be caught, we add it to the stack. The size of the stack at the end will be the number of car fleets.

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
        // Create a vector of pairs where each pair contains the position and speed of a car
        vector<pair<int, int>> cars;
        for (int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }
        
        // Sort the cars based on their positions
        sort(cars.begin(), cars.end());
        
        // Initialize a stack to keep track of the cars that will arrive at the destination
        stack<double> st;
        
        // Iterate over the cars in reverse order
        for (int i = cars.size() - 1; i >= 0; i--) {
            // Calculate the time it will take for the current car to arrive at the destination
            double time = (double)(target - cars[i].first) / cars[i].second;
            
            // If the stack is empty or the current car will not be caught by the car at the top of the stack, add it to the stack
            if (st.empty() || time > st.top()) {
                st.push(time);
            }
        }
        
        // The size of the stack at the end will be the number of car fleets
        return st.size();
    }
};
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
```

## Key Takeaways
- Use a stack to keep track of the cars that will arrive at the destination.
- Sort the cars based on their positions to ensure that we are considering the cars that are closest to the destination first.
- Calculate the time it will take for each car to arrive at the destination and compare it with the time of the car at the top of the stack to determine if it will be caught.