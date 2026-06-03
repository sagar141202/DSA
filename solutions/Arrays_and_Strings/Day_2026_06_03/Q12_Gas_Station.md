# Gas Station

## Problem Statement
There are `n` gas stations along a circular route, where the amount of gas at each station is given in the `gas` array, and the cost of traveling from one station to the next is given in the `cost` array. The task is to find the starting point that allows us to complete the circuit and return to the starting point without running out of gas. If it's impossible to complete the circuit, return -1. The function should take two integer arrays `gas` and `cost` of size `n` as input, where `gas[i]` is the amount of gas at the `i-th` station and `cost[i]` is the cost of traveling from the `i-th` station to the `(i+1)-th` station.

## Approach
The algorithm uses a greedy approach to find the starting point by maintaining a running total of gas and cost. It iterates through the arrays and updates the total gas and total cost. If the total gas is less than the total cost at any point, it resets the starting point. The function returns the starting point if the total gas is greater than or equal to the total cost after iterating through the arrays.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
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
- We use a greedy approach to find the starting point by maintaining a running total of gas and cost.
- If the total gas is less than the total cost at any point, we reset the starting point.
- The function returns the starting point if the total gas is greater than or equal to the total cost after iterating through the arrays.