# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each station, you can stop to refuel and add the amount of gas at that station to your tank. However, if at any point your gas level becomes negative, you will not be able to complete the circuit. Given the array gas and an array cost where cost[i] represents the cost of traveling from station i to station i+1, return the starting gas station's index if you can complete the circuit, otherwise return -1. The input arrays are 1-indexed, but the solution should be 0-indexed.

## Approach
The algorithm uses a two-pointer approach to track the total gas and the current gas level. It iterates through the gas stations, adding the gas at each station to the total gas and subtracting the cost of traveling to the next station. If the current gas level becomes negative, it resets the starting station index and the current gas level.

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
- The key to solving this problem is to track the total gas and the current gas level separately.
- If the current gas level becomes negative, it means we cannot start from the current starting station, so we reset the starting station index.
- The time complexity of this solution is O(n), where n is the number of gas stations.