# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it is impossible to reach the last index, return -1. The array is 0-indexed, and the length of the array is between 1 and 10^4. The elements in the array are between 0 and 10^5.

## Approach
We will use dynamic programming to solve this problem by maintaining an array that stores the minimum number of jumps required to reach each index. We will iterate through the array and update the minimum number of jumps required to reach each index based on the previous indices that can jump to it.

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
        
        return jumps[n - 1] == INT_MAX ? -1 : jumps[n - 1];
    }
};
```

## Test Cases
```
Input: [2,3,1,1,4]
Output: 2
Input: [2,3,0,1,4]
Output: 2
Input: [0,1]
Output: -1
```

## Key Takeaways
- The problem can be solved using dynamic programming by maintaining an array that stores the minimum number of jumps required to reach each index.
- We iterate through the array and update the minimum number of jumps required to reach each index based on the previous indices that can jump to it.
- If it is impossible to reach the last index, we return -1.