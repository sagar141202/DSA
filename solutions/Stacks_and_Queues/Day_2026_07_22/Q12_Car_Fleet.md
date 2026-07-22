# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. Each car has a position and a speed. The position is a positive integer, and the speed is a positive integer. If a car in front is slower than a car behind it, the car behind will catch up to the car in front. The task is to find out how many car fleets will arrive at the destination. A car fleet is a group of cars that will arrive at the destination at the same time. The position of the destination is target. The input will be a 2D vector where the first element of each sub-array is the position and the second element is the speed.

## Approach
To solve this problem, we will use a stack to keep track of the fleets. We will sort the cars based on their positions and then iterate through them. If a car can catch up to the car at the top of the stack, we will pop the car from the stack. Otherwise, we will push the car onto the stack.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int carFleet(int target, vector<vector<int>>& position) {
        // Sort the cars based on their positions
        sort(position.begin(), position.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] > b[0];
        });

        // Initialize the stack to keep track of the fleets
        stack<double> fleets;

        // Iterate through the cars
        for (auto& car : position) {
            // Calculate the time it takes for the car to reach the destination
            double time = (double)(target - car[0]) / car[1];

            // If the stack is not empty and the car can catch up to the car at the top of the stack
            if (!fleets.empty() && time <= fleets.top()) {
                // Continue to the next car
                continue;
            }

            // Push the time onto the stack
            fleets.push(time);
        }

        // The number of fleets is the size of the stack
        return fleets.size();
    }
};
```

## Test Cases
```
Input: target = 12, position = [[10,2],[8,4],[0,2],[5,4],[3,1]]
Output: 3
```

## Key Takeaways
- Sort the cars based on their positions to ensure that we are always considering the car that is closest to the destination.
- Use a stack to keep track of the fleets and avoid counting a car that can catch up to another car.
- Calculate the time it takes for each car to reach the destination and compare it with the time at the top of the stack to determine if a car can catch up to another car.