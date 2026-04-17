# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array `gas`. You have a car with an unlimited gas tank and you want to complete a tour of the route. The car starts with an empty tank at one of the gas stations. At each station, you can stop for gas, and your car will consume the gas to travel to the next station. The amount of gas consumed to travel from one station to the next is given in an array `cost`. Determine if it is possible to complete the tour and return the starting gas station index if it is possible.

## Approach
The algorithm uses a single pass through the arrays to track the total gas and the current gas in the tank. If the total gas is negative at any point, it is impossible to complete the tour. Otherwise, the starting index is the index where the current gas in the tank is minimum.

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
- We can use a single pass through the arrays to solve the problem.
- The total gas and the current gas in the tank are tracked separately to determine the starting index.
- If the total gas is negative, it is impossible to complete the tour.