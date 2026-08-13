# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to travel around the circuit. At each gas station, you can stop and refuel. However, if you arrive at a gas station with an empty tank, you cannot refuel and your journey ends. Given two arrays, gas and cost, where gas[i] is the amount of gas available at the i-th gas station and cost[i] is the cost of traveling from the i-th gas station to the (i+1)-th gas station, determine if it is possible to complete the circuit and return the starting gas station index if it is possible.

## Approach
The algorithm involves calculating the total gas available and the total cost of the trip. If the total gas is less than the total cost, it is impossible to complete the circuit. Otherwise, we can find the starting gas station index by iterating through the gas stations and keeping track of the minimum gas level.

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
- The key to solving this problem is to understand that if the total gas available is less than the total cost, it is impossible to complete the circuit.
- We can find the starting gas station index by iterating through the gas stations and keeping track of the minimum gas level.
- The time complexity of the solution is O(n), where n is the number of gas stations.