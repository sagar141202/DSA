# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given the array `[2,3,1,1,4]`, you can reach the last index because you can jump from index 0 to index 1, then from index 1 to index 2, and so on. However, given the array `[3,2,1,0,4]`, you cannot reach the last index because you cannot jump from index 3 to index 4.

## Approach
The approach to solve this problem is to use a greedy algorithm, keeping track of the maximum reachable position. We initialize the maximum reachable position to 0 and then iterate through the array, updating the maximum reachable position at each step. If we encounter a position that is beyond the maximum reachable position, we return false. If we successfully iterate through the entire array, we return true.

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
            // if current position is beyond maxReach, return false
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
- We use a greedy approach to solve this problem, keeping track of the maximum reachable position.
- We iterate through the array only once, resulting in a time complexity of O(n).
- The space complexity is O(1) as we only use a constant amount of space to store the maximum reachable position.