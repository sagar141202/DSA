# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by jumping. However, given `nums = [3,2,1,0,4]`, the function should return `false` because we cannot reach the last index (4) from the first index (0) by jumping. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.

## Approach
We will use a greedy algorithm to solve this problem by maintaining a variable to keep track of the maximum reachable index. We will iterate through the array and update this variable at each step. If we can reach the last index, we will return true; otherwise, we will return false.

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
        // Initialize the maximum reachable index to 0
        int maxReachableIndex = 0;
        
        // Iterate through the array
        for (int i = 0; i < nums.size(); i++) {
            // If we cannot reach the current index, return false
            if (i > maxReachableIndex) {
                return false;
            }
            
            // Update the maximum reachable index
            maxReachableIndex = max(maxReachableIndex, i + nums[i]);
        }
        
        // If we can reach the last index, return true
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
- The key to solving this problem is to maintain a variable to keep track of the maximum reachable index.
- We should update this variable at each step to ensure that we are considering the maximum jump length at each position.
- If we cannot reach the current index, we should immediately return false.