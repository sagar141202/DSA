# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. Each car has a position and a speed. The position of the ith car is position[i], and its speed is speed[i]. The destination is at position target. A car can catch up and form a fleet with cars in front of it if it can reach the same position as the car in front of it before it reaches the destination. The task is to find the number of car fleets that will arrive at the destination. The position and speed of each car are given as arrays position and speed, and the destination is given as target.

## Approach
We can solve this problem by using a stack to store the arrival times of the cars. We first calculate the arrival time of each car by dividing the distance from the car's position to the target by its speed. Then, we sort the cars based on their positions in descending order and iterate over them. If the current car's arrival time is less than or equal to the arrival time of the car at the top of the stack, we pop the car from the stack because the current car can catch up with it. Otherwise, we push the current car's arrival time into the stack.

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
        sort(cars.begin(), cars.end(), [](const auto& a, const auto& b) {
            return a.first > b.first;
        });
        stack<double> st;
        for (auto& car : cars) {
            double arrivalTime = (double)(target - car.first) / car.second;
            if (st.empty() || arrivalTime > st.top()) {
                st.push(arrivalTime);
            }
        }
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
- We use a stack to store the arrival times of the cars.
- We sort the cars based on their positions in descending order to ensure that we process the cars from the front to the back.
- We use a pair to store the position and speed of each car for easier sorting and processing.