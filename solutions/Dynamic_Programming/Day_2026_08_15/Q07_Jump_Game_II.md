# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. For example, if the input array is `[2,3,1,1,4]`, the minimum number of jumps to reach the last index is `2` (jump 1 step from index 0 to index 1, then 3 steps to the last index).

## Approach
We use dynamic programming to solve this problem by maintaining an array to store the minimum number of jumps required to reach each index. We iterate over the array and update the minimum number of jumps for each index based on the previous indices that can reach it. The algorithm ensures that we always choose the minimum number of jumps to reach the current index.

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
        
        vector<int> dp(n, INT_MAX);
        dp[0] = 0;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (j + nums[j] >= i) {
                    dp[i] = min(dp[i], dp[j] + 1);
                }
            }
        }
        
        return dp[n - 1];
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
- The dynamic programming approach helps to avoid redundant calculations and ensures an efficient solution.
- The time complexity can be optimized to O(n) by using a greedy approach, where we maintain the maximum reachable index and the minimum number of jumps to reach it.