# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. If it's impossible to reach the last index, return -1. For example, given the array `[2,3,1,1,4]`, the minimum number of jumps to reach the last index is 2, by jumping from index 0 to index 1, then from index 1 to index 4.

## Approach
The algorithm uses dynamic programming to track the minimum number of jumps required to reach each index. It iterates through the array, updating the minimum number of jumps for each index based on the minimum number of jumps required to reach the previous indices that can jump to the current index.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        
        vector<int> jumps(n, INT_MAX);
        jumps[0] = 0;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (j + nums[j] >= i) {
                    jumps[i] = min(jumps[i], jumps[j] + 1);
                }
            }
        }
        
        return jumps[n - 1] == INT_MAX ? -1 : jumps[n - 1];
    }
};
```

## Test Cases
```
Input: [2,3,1,1,4]
Output: 2
Input: [2,3,0,1,4]
Output: 2
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize the base case (jumps[0] = 0) to avoid incorrect results.
- Use a bottom-up approach to fill up the dp table (jumps array) for efficient computation.