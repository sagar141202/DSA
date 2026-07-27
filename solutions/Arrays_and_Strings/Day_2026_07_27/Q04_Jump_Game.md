# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by the following sequence of steps: `0 -> 1 -> 4`. However, given `nums = [3,2,1,0,4]`, the function should return `false` because there is no way to reach the last index from the first index.

## Approach
We will use a greedy approach, iterating through the array and keeping track of the maximum reachable position. If we can reach the last index, we return true; otherwise, we return false. The key idea is to always try to extend the reachable range.

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
- The greedy approach is suitable for this problem, as we only need to keep track of the maximum reachable position.
- We should always try to extend the reachable range, which is done by updating `maxReach` with the maximum value between the current `maxReach` and `i + nums[i]`.