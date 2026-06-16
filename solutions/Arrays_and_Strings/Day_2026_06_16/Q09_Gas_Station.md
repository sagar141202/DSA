# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each station, you can stop and refuel, and you start with an empty tank at one of the gas stations. The cost of traveling from one station to the next is given in an array cost. Return the starting gas station's index if it is possible to travel around the circuit, otherwise return -1. The constraints are: 1 <= n <= 10^4, 0 <= gas[i] <= 10^4, 1 <= cost[i] <= 10^4.

## Approach
The algorithm uses a two-pass approach to find the starting gas station. First, it checks if it is possible to complete the circuit by calculating the total gas and total cost. If the total gas is less than the total cost, it returns -1. Otherwise, it calculates the starting gas station by iterating through the array and keeping track of the minimum gas level.

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
- We need to check if the total gas is greater than or equal to the total cost to determine if it is possible to complete the circuit.
- We use a two-pass approach to find the starting gas station, first checking if it is possible to complete the circuit and then calculating the starting gas station.
- The time complexity is O(n) and the space complexity is O(1), where n is the number of gas stations.