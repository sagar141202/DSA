# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-lane road. The cars are numbered from 0 to n-1. The cars are initially at positions car[0], car[1], ..., car[n-1] and the destination is at position target. Each car has a constant speed which is either positive or negative. A car fleet is when a car is following another car and the following car catches up to the car in front at the destination. The task is to find the number of car fleets that will arrive at the destination. The constraints are 1 <= n <= 10^4, 0 <= car[i] <= 10^6, 1 <= target <= 10^6, and -10^6 <= speed[i] <= 10^6. The examples are car = [1,5,0,3], speed = [1,2,1,1], target = 4, output = 1 and car = [3,5,1,2], speed = [2,3,1,1], target = 4, output = 2.

## Approach
The approach is to use a stack to store the time it takes for each car to reach the destination. We iterate over the cars from right to left and for each car, we calculate the time it takes to reach the destination. If the time is less than or equal to the time at the top of the stack, we pop the stack until we find a time that is greater than the current time or the stack is empty.

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
        int n = position.size();
        vector<pair<int, int>> cars;
        for (int i = 0; i < n; i++) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.rbegin(), cars.rend());
        stack<double> st;
        for (auto& car : cars) {
            double time = (double)(target - car.first) / car.second;
            if (st.empty() || time > st.top()) {
                st.push(time);
            }
        }
        return st.size();
    }
};
```

## Test Cases
```
Input: car = [1,5,0,3], speed = [1,2,1,1], target = 4
Output: 1
Input: car = [3,5,1,2], speed = [2,3,1,1], target = 4
Output: 2
```

## Key Takeaways
- Use a stack to store the time it takes for each car to reach the destination.
- Iterate over the cars from right to left to ensure that we are considering the cars that are closest to the destination first.
- If the time it takes for a car to reach the destination is less than or equal to the time at the top of the stack, pop the stack until we find a time that is greater than the current time or the stack is empty.