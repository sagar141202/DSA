# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. For example, given the array `[2,3,1,1,4]`, the minimum number of jumps to reach the last index is `2` (jump 1 step from index 0 to index 1, then 3 steps to the last index). If it's impossible to reach the last index, return -1.

## Approach
We use dynamic programming to track the minimum number of jumps to reach each index. We initialize the jumps array with infinity for all indices except the first one, which is 0. Then we iterate over the array and update the jumps array based on the maximum jump length at each position.

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
        
        vector<int> jumps(n, INT_MAX);
        jumps[0] = 0;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (j + nums[j] >= i) {
                    jumps[i] = min(jumps[i], jumps[j] + 1);
                }
            }
        }
        
        return jumps[n - 1] != INT_MAX ? jumps[n - 1] : -1;
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The jumps array is used to store the minimum number of jumps to reach each index.
- The time complexity can be optimized to O(n) by using a greedy approach.