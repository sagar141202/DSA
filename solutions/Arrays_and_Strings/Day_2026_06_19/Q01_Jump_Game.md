# Jump Game

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index. For example, given `nums = [2,3,1,1,4]`, the output is `true` because we can reach the last index (4) from the first index (0) by jumping 1 step from index 0 to index 1, then 3 steps to index 4. On the other hand, if `nums = [3,2,1,0,4]`, the output is `false` because we cannot reach the last index.

## Approach
We use a greedy algorithm to keep track of the farthest reachable position. If the farthest reachable position is greater than or equal to the current position, we can reach the current position. We update the farthest reachable position if we can reach a position that is farther than the current farthest reachable position.

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
        int lastpos = nums.size() - 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (i + nums[i] >= lastpos) {
                lastpos = i;
            }
        }
        return lastpos == 0;
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
- We can solve this problem using a greedy algorithm.
- We only need to keep track of the farthest reachable position to determine if we can reach the last index.
- The time complexity is O(n) because we only iterate through the array once.