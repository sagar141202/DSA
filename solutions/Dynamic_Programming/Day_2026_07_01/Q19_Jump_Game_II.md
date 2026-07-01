# Jump Game II

## Problem Statement
Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Your goal is to reach the last index in the minimum number of jumps. It is guaranteed that you are able to reach the last index.

## Approach
The problem can be solved using dynamic programming and greedy approach. We can use an array to store the minimum number of jumps required to reach each index. At each index, we try to find the minimum number of jumps by considering all previous indices that can reach the current index.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        vector<int> jumps(n, INT_MAX);
        jumps[0] = 0;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (j + nums[j] >= i) {
                    jumps[i] = min(jumps[i], jumps[j] + 1);
                }
            }
        }
        
        return jumps[n - 1];
    }
};
```

## Test Cases
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
             One possible way is to jump 1 step from index 0 to index 1, 
             then 3 steps to index 4.
```

## Key Takeaways
- The dynamic programming approach helps to avoid redundant calculations and improve efficiency.
- The greedy approach is used to find the minimum number of jumps at each index by considering all previous indices that can reach the current index.
- The time complexity is O(n^2) due to the nested loops, where n is the size of the input array.