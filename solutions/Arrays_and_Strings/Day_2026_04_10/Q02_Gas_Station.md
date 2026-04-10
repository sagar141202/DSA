# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each station, you can stop for gas, and you have to use the gas to travel to the next station. If you start at station i, the amount of gas you have after traveling to station j is the sum of the gas at stations i through j minus the cost of traveling from i to j. Given two arrays, gas and cost, where gas[i] is the amount of gas at station i and cost[i] is the cost of traveling from station i to station i+1, return the starting gas station's index if you can complete the circuit, otherwise return -1. The constraints are 1 <= n <= 10^5, 0 <= gas[i], cost[i] <= 10^4, and the total amount of gas is not less than the total cost.

## Approach
The algorithm uses a two-pointer technique and prefix sum to track the total gas and total cost. It iterates over the stations, updating the total gas and cost, and checks if the car can complete the circuit. If the total gas is less than the total cost at any point, it resets the starting station.

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
        int totalGas = 0, totalCost = 0, tank = 0, start = 0;
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
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
```

## Key Takeaways
- The key to solving this problem is to track the total gas and total cost separately and update the starting station when the tank is empty.
- The algorithm uses a single pass through the stations, making it efficient for large inputs.
- The solution handles edge cases, such as when the total gas is less than the total cost, and returns -1 accordingly.