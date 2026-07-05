# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the function should return `true` because we can reach the last index (4) from the first index (0) by jumping 1 step from index 0 to index 1, then 3 steps to index 4. However, given `nums = [3,2,1,0,4]`, the function should return `false` because we cannot reach the last index from the first index.

## Approach
The algorithm uses a greedy approach to track the maximum reachable index. We initialize the maximum reachable index to 0 and then iterate over the array, updating the maximum reachable index if we can reach further. If the maximum reachable index is ever less than the current index, we return false.

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
        int maxReachableIndex = 0;
        for (int i = 0; i < nums.size(); i++) {
            // if the current index is beyond the max reachable index, return false
            if (i > maxReachableIndex) return false;
            // update the max reachable index
            maxReachableIndex = max(maxReachableIndex, i + nums[i]);
        }
        // if we can reach the last index, return true
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
- We can solve this problem using a greedy approach by tracking the maximum reachable index.
- The time complexity is O(n) where n is the number of elements in the array, and the space complexity is O(1) as we only use a constant amount of space.