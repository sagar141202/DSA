# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each station, you can stop and refuel, but you cannot refuel at more than one station at a time. The cost of traveling from one station to the next is given in an array cost. The task is to determine if it is possible to complete the circuit and, if so, to find the starting gas station that will result in the minimum amount of gas used. The function should return the index of the starting gas station if it is possible to complete the circuit, otherwise return -1. The constraints are 1 <= n <= 10^4, 0 <= gas[i] <= 10^4, and 0 <= cost[i] <= 10^4.

## Approach
The approach to solve this problem is to use a two-pointer technique to track the total gas and the current gas. We iterate through the array and update the total gas and the current gas at each station. If the current gas is less than 0, we reset the current gas and update the starting station. The station with the minimum total gas will be the starting station.

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
        int currentGas = 0;
        int start = 0;
        
        for (int i = 0; i < gas.size(); i++) {
            totalGas += gas[i] - cost[i];
            currentGas += gas[i] - cost[i];
            
            if (currentGas < 0) {
                start = i + 1;
                currentGas = 0;
            }
        }
        
        return totalGas >= 0 ? start : -1;
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
- The key to solving this problem is to use a two-pointer technique to track the total gas and the current gas.
- The time complexity of this solution is O(n), where n is the number of gas stations.
- The space complexity of this solution is O(1), as we are using a constant amount of space to store the total gas, the current gas, and the starting station.