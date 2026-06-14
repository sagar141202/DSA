# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it's impossible to reach the last index, return -1. For example, given the array `[2,3,1,1,4]`, the minimum number of jumps to reach the last index is 2 (jump 1 step from index 0 to index 1, then 3 steps to index 4).

## Approach
We use dynamic programming to solve this problem by maintaining an array to store the minimum number of jumps required to reach each index. The algorithm iterates through the array, updating the minimum number of jumps for each index based on the previous indices that can reach it.

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
        int n = nums.size();
        if (n <= 1) return 0;
        
        int maxReach = nums[0];
        int step = nums[0];
        int jumps = 1;
        
        for (int i = 1; i < n; i++) {
            if (i == n - 1) return jumps;
            
            maxReach = max(maxReach, i + nums[i]);
            step--;
            
            if (step == 0) {
                jumps++;
                if (i >= maxReach) return -1;
                step = maxReach - i;
            }
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
- We initialize `maxReach` and `step` with the value of the first element in the array, which represents the maximum reachable index and the remaining steps before we need to make another jump.
- We iterate through the array, updating `maxReach` and `step` based on the current index and its value.
- If `step` becomes 0, we increment the number of jumps and update `step` with the remaining reachable indices.