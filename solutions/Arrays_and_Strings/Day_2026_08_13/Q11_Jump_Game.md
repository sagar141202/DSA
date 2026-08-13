# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the output is `true` because we can reach the last index by jumping from index 0 to index 1, then from index 1 to index 2, and so on. However, if `nums = [3,2,1,0,4]`, the output is `false` because we cannot reach the last index.

## Approach
The algorithm uses a greedy approach to track the maximum reachable position. It iterates through the array, updating the maximum reachable position at each step. If the maximum reachable position is ever less than the current index, it means we cannot reach the current index, so the function returns `false`.

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
            // If we can't reach this index, return false
            if (i > maxReach) {
                return false;
            }
            // Update the maximum reachable position
            maxReach = max(maxReach, i + nums[i]);
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
- We only need to keep track of the maximum reachable position, not the actual path.
- The greedy approach allows us to solve the problem in linear time complexity.
- The space complexity is constant because we only use a fixed amount of space to store the maximum reachable position.