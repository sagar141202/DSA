# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by jumping 1 step from index 0 to index 1, then 3 steps to index 4. On the other hand, if we have `nums = [3,2,1,0,4]`, the function should return `false` because we cannot reach the last index from the first index.

## Approach
We can solve this problem using a greedy algorithm by iterating through the array and keeping track of the maximum reachable index. The algorithm iterates through the array, updating the maximum reachable index at each step. If the maximum reachable index is ever less than the current index, we return false, indicating that we cannot reach the last index.

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
            // If the current index is greater than the maximum reachable index, return false
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
- We use a greedy algorithm to solve this problem, keeping track of the maximum reachable index at each step.
- The time complexity is O(n), where n is the size of the input array, because we only need to iterate through the array once.
- The space complexity is O(1), because we only use a constant amount of space to store the maximum reachable index.