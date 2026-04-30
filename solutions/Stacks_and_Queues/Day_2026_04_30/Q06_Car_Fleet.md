# Car Fleet

## Problem Statement
There are n cars going to the same destination along a one-way road. The cars start at different positions and have different speeds. Each car will stop at a certain position. If a car reaches a position where another car has stopped, it will stop at that position. The task is to find the number of car fleets that will arrive at the destination. A car fleet is a group of cars that will stop at the same position.

## Approach
We can use a stack to keep track of the positions and speeds of the cars. We sort the cars by their positions in descending order and then iterate through them. If the current car's speed is greater than the speed of the car at the top of the stack, we push the current car's position and speed onto the stack.

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

int main() {
    Solution solution;
    int target = 12;
    vector<int> position = {10,8,0,5,3};
    vector<int> speed = {2,4,1,1,3};
    cout << solution.carFleet(target, position, speed) << endl;
    return 0;
}
```

## Test Cases
```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Input: target = 100, position = [0,2,4,6,8], speed = [1,1,1,1,1]
Output: 1
```

## Key Takeaways
- We use a stack to keep track of the positions and speeds of the cars.
- The cars are sorted by their positions in descending order to ensure that we process the cars that are closest to the destination first.
- We calculate the time it takes for each car to reach the destination and push it onto the stack if it's greater than the time of the car at the top of the stack.