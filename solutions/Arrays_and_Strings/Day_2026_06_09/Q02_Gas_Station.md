# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a circuit around the route. However, you can only hold a certain amount of gas in your tank at any given time. The gas at each station is just enough to travel to the next station, but you may not have enough gas to complete the circuit. Given two arrays, gas and cost, where gas[i] is the amount of gas at station i and cost[i] is the cost to travel from station i to station i+1 (or to station 0 if i is the last station), return the starting gas station's index if you can complete the circuit, otherwise return -1. The constraints are 1 <= n <= 10^5, 0 <= gas[i] <= 10^5, and 0 <= cost[i] <= 10^5.

## Approach
The algorithm involves iterating over the gas stations and calculating the total gas and total cost. If the total gas is less than the total cost, it's impossible to complete the circuit. Otherwise, we can start from each station and check if we can complete the circuit.

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
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
```

## Key Takeaways
- We need to calculate the total gas and total cost to determine if it's possible to complete the circuit.
- We use a tank variable to keep track of the current gas level.
- If the tank becomes negative, we reset it and update the start index.