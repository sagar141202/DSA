# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index by jumping from index 0 to index 1, then from index 1 to index 2, and so on. However, if `nums = [3,2,1,0,4]`, the function should return `false` because we cannot reach the last index.

## Approach
The algorithm uses a greedy approach, iterating through the array and keeping track of the maximum reachable index. If the maximum reachable index is ever less than the current index, we know we cannot reach the last index. The intuition is to always try to extend the maximum reachable index as far as possible.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;
        for (int i = 0; i < nums.size(); i++) {
            // If the current index is greater than the maxReach, return false
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
- The greedy approach is suitable for this problem because we only need to keep track of the maximum reachable index.
- The time complexity is O(n) because we only iterate through the array once.
- The space complexity is O(1) because we only use a constant amount of space to store the maximum reachable index.