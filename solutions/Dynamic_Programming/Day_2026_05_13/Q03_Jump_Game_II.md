# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. You are allowed to jump to any index within your jump range. If it is impossible to reach the last index, return -1. For example, given the array `[2,3,1,1,4]`, the minimum number of jumps to reach the last index is `2` by jumping from index `0` to index `1` and then from index `1` to index `4`. If the array is `[3,2,1,0,4]`, it is impossible to reach the last index.

## Approach
The solution uses dynamic programming and greedy approach to find the minimum number of jumps. We maintain an array to store the minimum number of jumps to reach each index and another array to store the maximum reachable index.

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
        
        return -1;
    }
};
```

## Test Cases
```
Input: [2,3,1,1,4]
Output: 2
Input: [3,2,1,0,4]
Output: -1
```

## Key Takeaways
- Use a greedy approach to always try to extend the maximum reachable index.
- Maintain a `step` variable to keep track of the remaining steps before we need to make another jump.
- If we cannot reach the next index, return -1 as it is impossible to reach the last index.