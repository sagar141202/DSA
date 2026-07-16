# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by jumping to index 1 and then to index 4. However, given `nums = [3,2,1,0,4]`, the function should return `false` because we cannot reach the last index from the first index.

## Approach
We will use a greedy approach to solve this problem, iterating through the array and keeping track of the maximum reachable position. If the maximum reachable position is ever less than the current index, we return false. Otherwise, we return true at the end of the iteration.

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
            // if we cannot reach this position, return false
            if (i > maxReach) return false;
            // update the maximum reachable position
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
- The greedy approach is suitable for this problem because we only need to keep track of the maximum reachable position.
- The time complexity is linear because we only iterate through the array once.
- The space complexity is constant because we only use a constant amount of space to store the maximum reachable position.