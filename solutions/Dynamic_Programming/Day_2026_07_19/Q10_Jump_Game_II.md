# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it's impossible to reach the last index, return -1. For example, given the array `[2,3,1,1,4]`, the minimum number of jumps to reach the last index is `2` by jumping from index `0` to index `1` and then from index `1` to index `4`. The constraints are `1 <= nums.length <= 10^4` and `0 <= nums[i] <= 10^5`.

## Approach
The algorithm uses dynamic programming and greedy approach to find the minimum number of jumps. It maintains an array to store the minimum number of jumps to reach each index. At each index, it tries to extend the jump range by considering all previous indices that can reach the current index.

## Complexity
- Time: O(n^2)
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
- Use a greedy approach to extend the jump range at each index.
- Maintain a variable to store the maximum reachable index.
- Use another variable to store the remaining steps before we need to make another jump.