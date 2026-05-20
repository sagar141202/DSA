# Gas Station

## Problem Statement
There are n gas stations along a circular route, where the amount of gas at each station is given in an array gas. You have a car with an unlimited gas tank and you want to complete a circuit around the route. At each gas station, you can stop to refuel. The amount of gas required to travel from one station to the next is given in an array cost. Determine if it is possible to complete the circuit and return the starting gas station index if it is possible. If it is not possible, return -1. The function should take two parameters: gas and cost, which are arrays of integers. The length of both arrays will be the same and will be in the range [1, 10^4]. The sum of gas will always be greater than or equal to the sum of cost.

## Approach
We can solve this problem by iterating over the gas stations and keeping track of the total gas and the minimum gas so far. If the total gas is less than 0 at any point, we need to start from the next station. We can use a single pass through the gas stations to find the starting index.

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
        int total = 0;
        int tank = 0;
        int start = 0;
        for (int i = 0; i < gas.size(); i++) {
            total += gas[i] - cost[i];
            tank += gas[i] - cost[i];
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        return total < 0 ? -1 : start;
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
- We only need to make one pass through the gas stations to find the starting index.
- We can use two variables, total and tank, to keep track of the total gas and the gas in the tank so far.
- If the total gas is less than 0, we know it is not possible to complete the circuit.