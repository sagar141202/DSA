# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. You are allowed to jump to any index within your jump range. For example, if you are at index 0 and the value at this index is 3, you can jump to index 1, 2, or 3.

## Approach
The problem can be solved using dynamic programming by maintaining an array to store the minimum number of jumps required to reach each index. We iterate through the array and update the minimum number of jumps for each index based on the minimum number of jumps required to reach the previous indices within the jump range.

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
        
        return jumps[n - 1];
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
- We use dynamic programming to solve the problem efficiently by avoiding redundant calculations.
- The time complexity can be optimized to O(n) by using a greedy approach, where we maintain the maximum reachable index and the number of steps to reach that index.