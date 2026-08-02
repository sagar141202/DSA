# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. For example, if the input array is [2,3,1,1,4], the minimum number of jumps to reach the last index is 2 (jump 1 step from index 0 to index 1, then 3 steps to index 4). If it's impossible to reach the last index, return -1. The constraints are 1 <= nums.length <= 10^4 and 0 <= nums[i] <= 10^5.

## Approach
The algorithm uses dynamic programming to track the minimum number of jumps to reach each index. It iterates through the array, updating the minimum number of jumps to reach each index based on the previous indices that can jump to it. The intuition is to use a greedy approach to always choose the index that can jump the farthest.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;
        int maxReach = nums[0];
        int step = nums[0];
        int jumps = 1;
        for (int i = 1; i < n; i++) {
            if (i == n - 1) return jumps;
            maxReach = max(maxReach, i + nums[i]);
            step--;
            if (step == 0) {
                jumps++;
                if (i >= maxReach) return -1;
                step = maxReach - i;
            }
        }
        return -1;
    }
};
```

## Test Cases
```
Input: [2,3,1,1,4]
Output: 2
Input: [2,3,0,1,4]
Output: 2
Input: [0,1,2,3,4]
Output: -1
```

## Key Takeaways
- Use dynamic programming to track the minimum number of jumps to reach each index.
- Use a greedy approach to always choose the index that can jump the farthest.
- Handle edge cases where it's impossible to reach the last index.