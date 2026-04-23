# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a trip around the circuit. At each gas station, you can stop for gas. The cost of traveling from one station to the next is given in an array cost. Determine if it is possible to complete the trip and return to the starting point. If it is possible, return the starting gas station index. If it is not possible, return -1. The trip can be completed if the total amount of gas is greater than or equal to the total cost.

## Approach
The approach to this problem is to use a single pass through the arrays to track the total gas and cost, as well as the current gas level. If the current gas level becomes negative, we reset it and update the starting point. We also keep track of the total gas and cost to determine if the trip is possible.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalGas = 0;
        int totalCost = 0;
        int currentGas = 0;
        int start = 0;
        
        for (int i = 0; i < gas.size(); i++) {
            totalGas += gas[i];
            totalCost += cost[i];
            currentGas += gas[i] - cost[i];
            
            if (currentGas < 0) {
                start = i + 1;
                currentGas = 0;
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
- The key to this problem is to keep track of the current gas level and reset it when it becomes negative.
- We also need to keep track of the total gas and cost to determine if the trip is possible.
- The time complexity is O(n) because we only need to make a single pass through the arrays.