# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it's impossible to reach the last index, return -1. For example, given the array `[2,3,1,1,4]`, the minimum number of jumps to reach the last index is `2` (jump 1 step from index 0 to index 1, then 3 steps to the last index).

## Approach
The problem can be solved using dynamic programming and greedy approach. We maintain an array to store the minimum jumps required to reach each position. At each step, we update the minimum jumps required to reach the next positions.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        // Initialize variables
        int n = nums.size();
        if (n <= 1) return 0;
        
        // Initialize the maxReach and step variables
        int maxReach = nums[0];
        int step = nums[0];
        int jumps = 1;
        
        // Iterate over the array
        for (int i = 1; i < n; i++) {
            // If we've reached the end of the current step, update the maxReach and step
            if (i == step) {
                jumps++;
                step = maxReach;
            }
            
            // Update the maxReach
            maxReach = max(maxReach, i + nums[i]);
            
            // If we can't reach the next position, return -1
            if (i >= step) return -1;
        }
        
        return jumps;
    }
};
```

## Test Cases
```
Input: [2,3,1,1,4]
Output: 2
Input: [2,3,0,1,4]
Output: 2
```

## Key Takeaways
- Use dynamic programming and greedy approach to solve the problem.
- Maintain variables to store the maximum reachable position and the current step.
- Update the variables at each step to find the minimum number of jumps required to reach the last index.