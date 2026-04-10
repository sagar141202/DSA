# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given the array `[2,3,1,1,4]`, you can reach the last index because you can jump from index 0 to index 1, then from index 1 to index 2, and so on. However, given the array `[3,2,1,0,4]`, you cannot reach the last index.

## Approach
The algorithm uses a greedy approach to keep track of the maximum reachable index. It iterates over the array, updating the maximum reachable index at each step. If the maximum reachable index is ever less than the current index, it means we cannot reach the current index, and thus we cannot reach the last index.

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
            // if we can't reach this index, return false
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
Input: [2,3,1,1,4]
Output: true
Input: [3,2,1,0,4]
Output: false
```

## Key Takeaways
- We use a greedy approach to solve this problem in linear time complexity.
- The key insight is to keep track of the maximum reachable index and update it at each step.
- If we ever encounter an index that is beyond our maximum reachable index, we return false.