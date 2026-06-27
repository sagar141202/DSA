# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations. Return the starting gas station's index if you can travel around the circuit once in a clockwise direction, otherwise return -1. If there is a solution, it is guaranteed to be unique. For example, given gas = [1,2,3,4,5] and cost = [3,4,2,4,2], the function should return 3.

## Approach
The algorithm uses a single pass through the arrays to track the total gas and the current gas. If the total gas is less than the total cost, it's impossible to complete the journey. We keep track of the minimum gas level and its index to determine the starting point.

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
Input: gas = [1,2,3,4,5], cost = [3,4,2,4,2]
Output: 3
```

## Key Takeaways
- The problem can be solved by tracking the total gas and the current gas level.
- If the total gas is less than the total cost, it's impossible to complete the journey.
- We keep track of the minimum gas level and its index to determine the starting point.