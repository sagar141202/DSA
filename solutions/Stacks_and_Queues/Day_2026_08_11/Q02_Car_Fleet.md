# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-way road. The cars have different speeds and start at different positions. The destination is target miles away. Each car will travel at its given speed until it reaches the destination or it reaches another car that is not moving. When two cars meet, they will merge into a single car and continue moving at the speed of the slower car. How many car fleets will arrive at the destination?

## Approach
We can use a stack to solve this problem, sorting the cars by position and then iterating through them. If a car is faster than the car at the top of the stack, it will overtake it and we can pop the top car from the stack. The number of cars left in the stack will be the number of fleets.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
```

## Key Takeaways
- Sort the cars by position in descending order to simulate the overtaking process.
- Use a stack to keep track of the arrival times of the cars.
- If a car is faster than the car at the top of the stack, it will overtake it and we can pop the top car from the stack.