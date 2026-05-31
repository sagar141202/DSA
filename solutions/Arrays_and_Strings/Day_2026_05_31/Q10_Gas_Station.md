# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each station, you can stop to refuel. The cost of traveling from one station to the next is given in an array cost. Determine if it's possible to complete the circuit and return to the starting point without running out of gas. If it is possible, return the starting gas station's index. If it's impossible, return -1. The constraints are 1 <= n <= 10^4, 0 <= gas[i] <= 10^4, and 0 <= cost[i] <= 10^4.

## Approach
The algorithm involves iterating through the gas stations and calculating the total gas and total cost. If the total gas is less than the total cost, it's impossible to complete the circuit. Otherwise, we can find the starting point by iterating through the stations and keeping track of the current gas level.

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
- We can use a single pass through the gas stations to determine if it's possible to complete the circuit and find the starting point.
- We need to keep track of the total gas and total cost to determine if it's possible to complete the circuit.
- We need to keep track of the current gas level (tank) to find the starting point.