# Gas Station

## Problem Statement
There are `n` gas stations along a circular route, where the amount of gas at each station is given in the array `gas`. You have a car with an unlimited gas tank and you want to complete a tour around the route. At each station, you can either refuel or not. The cost of traveling from one station to the next is given in the array `cost`. Determine if it's possible to complete the tour and return to the starting point, and if so, find the starting station.

## Approach
We will use a greedy algorithm to find the starting station. The idea is to keep track of the total gas and the total cost as we traverse the stations. If the total gas is ever less than the total cost, we know that the current station cannot be the starting point.

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
- We need to consider the total gas and the total cost to determine if it's possible to complete the tour.
- We use a greedy algorithm to find the starting station by keeping track of the tank level as we traverse the stations.
- If the total gas is less than the total cost, it's impossible to complete the tour.