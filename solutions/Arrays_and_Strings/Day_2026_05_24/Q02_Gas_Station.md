# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas, and the cost of gas to travel from one station to the next is given in an array cost. The task is to determine if it is possible to travel around the route and return to the starting point without running out of gas, and if so, find the starting point. The constraints are 1 <= n <= 10^4, 0 <= gas[i] <= 10^4, and 1 <= cost[i] <= 10^4.

## Approach
The algorithm uses a greedy approach to find the starting point by iterating through the gas stations and keeping track of the total gas and total cost. If the total gas is greater than or equal to the total cost at any point, it means we can start from that point and travel around the route without running out of gas.

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
        int tank = 0;
        int start = 0;
        
        for (int i = 0; i < gas.size(); i++) {
            totalGas += gas[i];
            totalCost += cost[i];
            tank += gas[i] - cost[i];
            
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        
        if (totalGas < totalCost) {
            return -1;
        }
        
        return start;
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
- We need to keep track of the total gas and total cost to determine if it's possible to travel around the route.
- We use a greedy approach to find the starting point by iterating through the gas stations and keeping track of the tank level.
- If the total gas is less than the total cost, it's impossible to travel around the route.