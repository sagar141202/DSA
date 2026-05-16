# Gas Station

## Problem Statement
There are N gas stations along a circular route, where the amount of gas at each station is given in the array `gas`. The gas at each station can be used to travel to the next station, and the cost of traveling from one station to the next is given in the array `cost`. The goal is to determine if it is possible to complete a circuit around the route, starting from a given station, and if so, return the starting station. If it is not possible, return -1. The constraints are 1 <= N <= 10^4, 0 <= gas[i] <= 10^4, and 0 <= cost[i] <= 10^4.

## Approach
The algorithm uses a greedy approach to find the starting station by iterating over the gas and cost arrays. It keeps track of the total gas and total cost, as well as the minimum total gas and the corresponding starting station.

## Complexity
- Time: O(N)
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
- The key to this problem is to understand that if the total gas is less than the total cost, it is impossible to complete the circuit.
- We use a greedy approach to find the starting station by iterating over the gas and cost arrays.
- We keep track of the total gas, total cost, and the minimum total gas to determine the starting station.