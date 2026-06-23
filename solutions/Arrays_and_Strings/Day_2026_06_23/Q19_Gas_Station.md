# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. The gas at each station can be used to travel to the next station, and each station has a cost, given in an array cost, to travel to the next station. The task is to determine if it is possible to complete a tour that visits all gas stations and returns to the starting point, and if so, find the starting point. The constraints are: 1 <= n <= 10^4, 0 <= gas[i] <= 10^4, 1 <= cost[i] <= 10^4.

## Approach
The algorithm uses a prefix sum array to track the total gas and total cost at each station. It iterates through the stations to find the starting point where the total gas is greater than or equal to the total cost.

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
- The key to solving this problem is to track the total gas and total cost separately.
- If the total gas is less than the total cost, it is impossible to complete the tour.
- The starting point is the station where the tank becomes empty, i.e., the total gas is less than the total cost.