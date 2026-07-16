# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it is impossible to reach the last index, return 0. The array is 0-indexed, and you can only jump to indices that are within your current jump range. For example, if you are at index 0 and the value at index 0 is 3, you can jump to indices 1, 2, or 3.

## Approach
The algorithm uses dynamic programming to track the minimum number of jumps required to reach each index. It iterates through the array, updating the minimum number of jumps for each index based on the minimum number of jumps required to reach the previous indices that can jump to the current index.

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
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize the dynamic programming table with a base case, and then fill it up iteratively.
- Use a greedy approach to find the minimum number of jumps required to reach each index.