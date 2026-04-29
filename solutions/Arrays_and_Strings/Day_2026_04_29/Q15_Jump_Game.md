# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by jumping 1 step from index 0 to index 1, then 3 steps to index 4. On the other hand, given `nums = [3,2,1,0,4]`, the function should return `false` because we cannot reach the last index from the first index.

## Approach
We can solve this problem using a greedy algorithm, where we keep track of the maximum reachable position. We initialize the maximum reachable position to 0 and then iterate through the array, updating the maximum reachable position at each step. If we encounter an index that is beyond the maximum reachable position, we return false.

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
            // If the current index is beyond the maxReach, return false
            if (i > maxReach) {
                return false;
            }
            // Update maxReach
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
- The key to this problem is to keep track of the maximum reachable position.
- We can use a greedy algorithm to solve this problem in O(n) time complexity.
- The space complexity is O(1) because we only use a constant amount of space to store the maximum reachable position.