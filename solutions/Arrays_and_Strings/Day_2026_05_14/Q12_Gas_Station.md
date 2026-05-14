# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to travel around the circuit. At each station, you can refuel and then travel to the next station. The cost of traveling from one station to the next is given in an array cost. Return the starting gas station's index if you can travel around the circuit and return -1 otherwise. The constraints are 1 <= n <= 10^4, 0 <= gas[i] <= 10^4, and 0 <= cost[i] <= 10^4.

## Approach
The algorithm uses a two-pass approach, first calculating the total gas and total cost to check if it's possible to complete the circuit. Then, it iterates through the stations to find the starting point with the maximum gas.

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
- We need to check if the total gas is greater than or equal to the total cost to determine if it's possible to complete the circuit.
- The starting point should have the maximum gas, and we can use a two-pass approach to find it.
- The time complexity is O(n), where n is the number of gas stations.