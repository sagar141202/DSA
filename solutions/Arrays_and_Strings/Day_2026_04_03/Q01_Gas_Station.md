# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array. You have a car with an unlimited gas tank and you want to complete a circuit of the route. However, you can only hold a certain amount of gas in your tank at any given time. Given two arrays, one for the gas available at each station and one for the cost to travel to the next station, determine if it is possible to complete the circuit and return to the starting point. If it is possible, return the starting point, otherwise return -1. The constraints are 1 <= n <= 10^4, 0 <= gas[i] <= 10^4, and 0 <= cost[i] <= 10^4.

## Approach
The algorithm uses a two-pointer technique and greedy approach to find the starting point. It calculates the total gas available and the total cost to travel the entire route. If the total gas available is less than the total cost, it is impossible to complete the circuit. Otherwise, it iterates over the gas stations to find the starting point.

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
- The problem can be solved using a two-pointer technique and greedy approach.
- The total gas available must be greater than or equal to the total cost to travel the entire route.
- The starting point is the station where the tank is empty after traveling from the previous starting point.