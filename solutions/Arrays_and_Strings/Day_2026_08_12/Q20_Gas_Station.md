# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to travel around the circuit. At each station, you can stop for gas. The cost of traveling from one station to the next is given in an array cost. The task is to determine if it is possible to make a circuit around the gas stations and return to the starting point, given that you start with an empty tank. If it is possible, return the starting gas station index, otherwise return -1. The constraints are: 1 <= n <= 10^4, 0 <= gas[i] <= 10^4, 1 <= cost[i] <= 10^4.

## Approach
The problem can be solved by iterating over the gas stations and calculating the total amount of gas and the total cost. If the total amount of gas is greater than or equal to the total cost, then it is possible to make a circuit. We can use a variable to keep track of the total gas and the total cost, and another variable to keep track of the minimum gas and the index of the starting station.

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

int main() {
    Solution solution;
    vector<int> gas = {1,2,3,4,5};
    vector<int> cost = {3,4,5,1,2};
    cout << solution.canCompleteCircuit(gas, cost) << endl;
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
- The key to solving this problem is to keep track of the total gas and the total cost, and to find the starting station where the total gas is greater than or equal to the total cost.
- The problem can be solved in linear time complexity, O(n), where n is the number of gas stations.
- The space complexity of the solution is O(1), which means the space required does not change with the size of the input.