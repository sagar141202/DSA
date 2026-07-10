# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it is impossible to reach the last index, return -1. For example, given the array `[2,3,1,1,4]`, the minimum number of jumps to reach the last index is `2` by jumping from index `0` to index `1` and then from index `1` to index `4`. The constraints are `1 <= nums.length <= 10^4` and `0 <= nums[i] <= 10^5`.

## Approach
We will use a greedy algorithm with dynamic programming to solve this problem. The idea is to maintain an array to store the minimum number of jumps to reach each index. We will iterate through the array and update the minimum number of jumps to reach each index based on the previous indices that can jump to it.

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
Input: [2,3,0,1,4]
Output: 2
```

## Key Takeaways
- The key to this problem is to maintain the maximum reachable index and the remaining steps before we need to make another jump.
- We use a greedy approach to always try to extend the maximum reachable index as much as possible.
- If we cannot reach the last index, we return -1.