# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in the array gas. You have a car with an unlimited gas tank and you want to travel around the circuit. At each gas station, you can stop for gas. The cost of traveling from one gas station to the next is given in the array cost. Determine if it is possible to travel around the circuit and return to the starting point, and if so, find the starting gas station.

## Approach
The problem can be solved by iterating over all possible starting points and checking if it's possible to complete the circuit. We can use a greedy approach to keep track of the total gas and cost at each station. If the total gas is ever less than the total cost, we know it's not possible to start at that station.

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
```

## Key Takeaways
- The key to solving this problem is to keep track of the total gas and cost at each station.
- If the total gas is ever less than the total cost, we know it's not possible to complete the circuit.
- We can use a greedy approach to find the starting point that allows us to complete the circuit.