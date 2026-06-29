# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array `gas`. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each station, you can stop and refuel, but you cannot stop at the same station twice. The cost of traveling from one station to the next is given in an array `cost`, where `cost[i]` is the amount of gas needed to travel from station `i` to station `i+1`. If you start at station `i`, determine if it's possible to complete a circuit and return to station `i`. If it is, return the starting station index; otherwise, return `-1`. The constraints are: `n == gas.length == cost.length`, `1 <= n <= 10^5`, and `0 <= gas[i], cost[i] <= 10^4`.

## Approach
We can solve this problem by iterating over all possible starting stations and checking if we can complete a circuit from each one. We'll keep track of the total gas and the minimum gas level seen so far. If the total gas is non-negative at the end of the iteration, we've found a valid starting station.

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
- We need to consider all possible starting stations to find a valid one.
- Keeping track of the total gas and the minimum gas level seen so far helps us determine if a starting station is valid.
- If the total gas is less than the total cost, it's impossible to complete a circuit.