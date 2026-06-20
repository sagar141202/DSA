# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. Assume that you can always reach the last index.

## Approach
The algorithm uses dynamic programming to track the minimum jumps required to reach each position. It iterates over the array and updates the minimum jumps for each position based on the previous positions that can jump to it. The final result is the minimum jumps required to reach the last index.

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
- The key to this problem is to maintain two variables: `maxReach` to track the maximum reachable position and `step` to track the remaining steps before we need to make another jump.
- We update `maxReach` and `step` at each position and increment the jump count when `step` becomes zero.
- The time complexity is O(n) because we only iterate over the array once, and the space complexity is O(1) because we only use a constant amount of space to store the variables.