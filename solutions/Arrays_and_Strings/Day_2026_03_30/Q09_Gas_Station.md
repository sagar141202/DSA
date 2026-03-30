# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations. Return the starting gas station's index if you can travel around the circuit once in a clockwise direction, otherwise return -1. If there is a solution, it is guaranteed that it is unique.

## Approach
The algorithm involves calculating the total gas and total cost, then checking if it's possible to complete the circuit. If possible, it iterates over the stations to find the starting point with the minimum tank level.

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
        
        return totalGas < totalCost ? -1 : start;
    }
};

int main() {
    Solution solution;
    vector<int> gas = {1,2,3,4,5};
    vector<int> cost = {3,4,5,1,2};
    cout << solution.canCompleteCircuit(gas, cost);
    return 0;
}
```

## Test Cases
```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
```

## Key Takeaways
- The algorithm first checks if the total gas is sufficient to cover the total cost.
- If the total gas is sufficient, it then finds the starting point by maintaining a tank level and resetting it when the tank level becomes negative.
- The time complexity of the algorithm is O(n), where n is the number of gas stations.