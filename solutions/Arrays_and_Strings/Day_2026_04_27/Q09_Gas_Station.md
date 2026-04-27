# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array `gas`. You have a car with an unlimited gas tank and it costs `cost[i]` gas to travel from station `i` to its next station (`i+1`). The function should return the starting gas station's index if it is possible to travel around the circuit once, otherwise return -1. The input arrays are of size n, where n is the number of gas stations. The car starts with an empty tank.

## Approach
The algorithm uses a two-pointer technique to keep track of the total gas and the current gas. It iterates over the array, updating the total gas and the current gas. If the current gas becomes negative, it resets the current gas and the start pointer.

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
        int total = 0;
        int tank = 0;
        int start = 0;
        for (int i = 0; i < gas.size(); i++) {
            total += gas[i] - cost[i];
            tank += gas[i] - cost[i];
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        return total >= 0 ? start : -1;
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
- We only need to find the starting point of the circuit.
- If the total gas is less than the total cost, it is impossible to complete the circuit.
- We should reset the start pointer when the tank becomes empty.