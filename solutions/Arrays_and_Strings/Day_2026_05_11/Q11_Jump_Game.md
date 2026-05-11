# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the answer is `true` because we can reach the last index by jumping from index 0 to index 1, then from index 1 to index 2, then from index 2 to index 3, and finally from index 3 to index 4. On the other hand, given `nums = [3,2,1,0,4]`, the answer is `false` because we cannot reach the last index.

## Approach
The algorithm uses a greedy approach, maintaining the maximum reachable position as we iterate through the array. If the maximum reachable position is ever less than the current index, we know we cannot reach the last index. The algorithm iterates through the array once, keeping track of the maximum reachable position.

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
        int maxReach = 0; // maximum reachable position
        for (int i = 0; i < nums.size(); i++) {
            // if the current index is greater than the maximum reachable position, return false
            if (i > maxReach) return false;
            // update the maximum reachable position
            maxReach = max(maxReach, i + nums[i]);
        }
        return true; // if we can reach the last index, return true
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
- We can solve this problem using a greedy approach by maintaining the maximum reachable position.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large inputs.
- The key insight is that if the maximum reachable position is ever less than the current index, we know we cannot reach the last index.