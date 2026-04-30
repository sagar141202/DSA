# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations. Return the starting gas station's index if you can travel around the circuit once in a clockwise direction, otherwise return -1. If there is a solution, it is guaranteed to be unique. For example, given gas = [1,2,3,4,5] and cost = [3,4,5,1,2], the function should return 3.

## Approach
The approach to solve this problem is to use a two-pointer technique and keep track of the total gas and the current gas. We iterate through the gas stations and update the total gas and the current gas. If the current gas is negative, we reset it and update the start pointer.

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
- We need to keep track of the total gas and the current gas to determine if we can complete the circuit.
- If the current gas is negative, we reset it and update the start pointer.
- The time complexity is O(n) and the space complexity is O(1) because we only use a constant amount of space.