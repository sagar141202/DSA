# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a tour to visit all the gas stations. The car starts with an empty tank at one of the gas stations. At each gas station, you can stop for gas, and the car will consume some gas to travel to the next gas station. Given two arrays, gas and cost, where gas[i] is the amount of gas at the i-th gas station and cost[i] is the cost to travel from the i-th gas station to the next one, determine if it is possible to make a circular tour that visits all the gas stations exactly once. If it is possible, return the starting gas station's index. If it is not possible, return -1. The constraints are 1 <= n <= 10^4 and 0 <= gas[i], cost[i] <= 10^4.

## Approach
The algorithm uses a greedy approach to find the starting point of the tour. It calculates the total amount of gas and the total cost, then iterates over the gas stations to find the starting point. If the total amount of gas is less than the total cost, it returns -1.

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
- The key to solving this problem is to understand that if the total amount of gas is less than the total cost, it is impossible to complete the tour.
- The starting point of the tour is the point where the tank becomes empty.
- The time complexity is O(n) because we only need to iterate over the gas stations once.