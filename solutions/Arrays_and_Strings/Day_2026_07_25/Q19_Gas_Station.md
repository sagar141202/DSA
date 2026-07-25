# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array `gas`. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each station `i`, you can get `gas[i]` amount of gas. The cost of traveling from station `i` to its next station `i+1` is `cost[i]`. Determine if it is possible to complete the circuit and return the starting gas station's index if it is possible. If it is not possible, return -1. 
The constraints are: 
- 1 <= n <= 10^4
- 0 <= gas[i] <= 10^4
- 0 <= cost[i] <= 10^4
- The total amount of gas is not sufficient to complete the circuit more than once.

## Approach
The algorithm involves iterating over the gas stations and calculating the total amount of gas and the total cost. If at any point the total gas is less than the total cost, it's not possible to complete the circuit from the current starting point. Otherwise, we keep track of the starting point that allows us to complete the circuit.

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
- We need to keep track of the total amount of gas and the total cost to determine if it's possible to complete the circuit.
- If at any point the total gas is less than the total cost, we need to update the starting point.
- The time complexity is linear because we only need to iterate over the gas stations once.