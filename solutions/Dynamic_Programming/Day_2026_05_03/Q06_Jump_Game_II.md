# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. You are allowed to jump to any index within your jump range. If it is impossible to reach the last index, return -1. For example, given the array [2,3,1,1,4], the minimum number of jumps to reach the last index is 2 (jump 1 step from index 0 to index 1, then 3 steps to index 4).

## Approach
We will use a dynamic programming approach to solve this problem. The idea is to maintain an array to store the minimum number of jumps required to reach each index. We will iterate through the array and update the minimum number of jumps required to reach each index.

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
```

## Key Takeaways
- We use a dynamic programming approach to solve this problem.
- We maintain an array to store the minimum number of jumps required to reach each index.
- We iterate through the array and update the minimum number of jumps required to reach each index.