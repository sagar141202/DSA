# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each station, you can stop for gas and the car will consume some amount of gas to travel to the next station, which is given in an array cost. Determine if it is possible to complete a circuit and return the starting gas station index if it is possible. If it is not possible, return -1. The function should take two parameters: gas and cost, which are arrays of integers representing the amount of gas at each station and the cost to travel to the next station, respectively. For example, if gas = [1,2,3,4,5] and cost = [3,4,5,1,2], then the function should return the starting index of the gas station.

## Approach
The approach to solve this problem is to calculate the total amount of gas and the total cost, and then check if the total amount of gas is greater than or equal to the total cost. If it is, then we can complete a circuit. We can use a single pass through the arrays to calculate the total amount of gas and the total cost, and to find the starting index of the gas station.

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
        } else {
            return start;
        }
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
- The problem can be solved in a single pass through the arrays.
- We need to keep track of the total amount of gas and the total cost to determine if it is possible to complete a circuit.
- We need to find the starting index of the gas station by resetting the tank whenever it becomes negative.