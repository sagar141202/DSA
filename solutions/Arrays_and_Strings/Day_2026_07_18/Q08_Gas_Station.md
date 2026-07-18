# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each station, you can stop to refuel, and the amount of gas you gain is the value at that station. However, you also lose gas as you drive from one station to the next, and the amount of gas you lose is given in an array cost. The problem is to determine if it's possible to complete the circuit, and if so, to find the starting gas station.

## Approach
The algorithm involves calculating the total gas and total cost, then checking if the total gas is greater than or equal to the total cost. If it is, we can start at any station where the cumulative gas is greater than or equal to the cumulative cost.

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
- The key to solving this problem is to calculate the total gas and total cost, and to find the starting station where the cumulative gas is greater than or equal to the cumulative cost.
- If the total gas is less than the total cost, it's impossible to complete the circuit.
- The time complexity is O(n) because we only need to iterate through the gas and cost arrays once.