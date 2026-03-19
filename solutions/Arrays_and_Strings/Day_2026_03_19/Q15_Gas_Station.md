# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array `gas`. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each station, you can stop for gas, and the cost to travel from one station to the next is given in an array `cost`. The task is to determine if it is possible to complete the circuit, and if so, return the starting gas station index. If it's impossible, return -1. The constraints are 1 <= n <= 10^4 and 0 <= gas[i], cost[i] <= 10^4.

## Approach
The algorithm involves iterating over the gas stations, keeping track of the total gas and the total cost. If the total gas is less than the total cost at any point, it means we cannot start from the current station. We also keep track of the minimum total gas and the corresponding index, which will be the starting point if we can complete the circuit.

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
- We need to keep track of the total gas and the total cost to determine if we can complete the circuit.
- We use a variable `tank` to keep track of the current gas level, and reset it to 0 when it becomes negative.
- The starting point is the index where the `tank` becomes 0, or the index where the total gas is greater than the total cost.