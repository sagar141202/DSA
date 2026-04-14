# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas, and the cost of traveling from one station to the next is given in an array cost. The task is to determine if it is possible to travel around the route and return to the starting point without running out of gas, and if so, to find the starting point. The function should return the starting point, and if it is not possible, return -1. The constraints are 1 <= n <= 10^4, 0 <= gas[i] <= 10^4, and 0 <= cost[i] <= 10^4.

## Approach
The algorithm uses a single pass through the arrays to track the total gas and the current gas. If the current gas is negative at any point, the starting point is updated to the next station. The function returns the starting point if the total gas is non-negative, and -1 otherwise.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total = 0;
        int tank = 0;
        int start = 0;
        for (int i = 0; i < gas.size(); i++) {
            total += gas[i] - cost[i];
            tank += gas[i] - cost[i];
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        return total >= 0 ? start : -1;
    }
};
```

## Test Cases
```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
```

## Key Takeaways
- The key to this problem is to track the total gas and the current gas separately.
- If the current gas is negative at any point, the starting point is updated to the next station.
- The function returns the starting point if the total gas is non-negative, and -1 otherwise.