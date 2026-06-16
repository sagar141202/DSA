# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. It is guaranteed that you are able to reach the last index.

## Approach
The problem can be solved using dynamic programming by maintaining an array to store the minimum jumps required to reach each index. We iterate over the array and update the minimum jumps for each index by considering all previous indices that can reach the current index.

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
        vector<int> dp(n, INT_MAX);
        dp[0] = 0; // minimum jumps to reach the first index is 0
        
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
```

## Key Takeaways
- We use dynamic programming to store the minimum jumps required to reach each index.
- We update the minimum jumps for each index by considering all previous indices that can reach the current index.
- The time complexity is O(n^2) because we have two nested loops, and the space complexity is O(n) because we use a vector of size n to store the minimum jumps.