# Gas Station

## Problem Statement
There are `n` gas stations along a circular route, where the amount of gas at each station is given in an array `gas`. The gas at each station can be used to travel to the next station, and the cost of traveling from one station to the next is given in an array `cost`. The task is to determine if it is possible to complete a tour around the route, and if so, to find the starting point. The function should return the starting point if it exists, and -1 otherwise. The constraints are: `n` is in the range `[1, 10^4]`, `gas` and `cost` are arrays of length `n` with values in the range `[0, 10^4]`.

## Approach
The algorithm uses a two-pointer approach to track the total gas and total cost, and a variable to track the starting point. If the total gas is ever less than the total cost, the starting point is updated. The starting point is returned if the total gas is greater than or equal to the total cost after iterating through all stations.

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
        int totalGas = 0;
        int totalCost = 0;
        int start = 0;
        int tank = 0;
        
        for (int i = 0; i < gas.size(); i++) {
            totalGas += gas[i];
            totalCost += cost[i];
            tank += gas[i] - cost[i];
            
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        
        return totalGas < totalCost ? -1 : start;
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
- The problem can be solved by tracking the total gas and total cost.
- The starting point is updated when the total gas is less than the total cost.
- The function returns -1 if the total gas is less than the total cost after iterating through all stations.