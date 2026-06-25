# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the output is `true` because we can reach the last index (4) from the first index (0) by jumping 1 step from index 0 to index 1, then 3 steps to index 4. On the other hand, given `nums = [3,2,1,0,4]`, the output is `false` because we cannot reach the last index from the first index.

## Approach
The algorithm uses a greedy approach, keeping track of the maximum reachable position. If the maximum reachable position is ever less than the current position, we return false. Otherwise, we update the maximum reachable position.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.size(); i++) {
            // if we can't reach this position, return false
            if (i > maxReach) return false;
            // update maxReach
            maxReach = max(maxReach, i + nums[i]);
        }
        // if we can reach the last position, return true
        return true;
    }
};
```

## Test Cases
```
Input: nums = [2,3,1,1,4]
Output: true
Input: nums = [3,2,1,0,4]
Output: false
```

## Key Takeaways
- We use a greedy approach to solve the problem in linear time complexity.
- The key insight is to keep track of the maximum reachable position and update it as we iterate through the array.
- If we can't reach a position, we immediately return false, which allows us to avoid unnecessary iterations.