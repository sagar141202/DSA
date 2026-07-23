# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is [1, 2, 3], the output should be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input array will have a length between 1 and 6, and the elements will be integers between -10 and 10.

## Approach
The solution uses backtracking to generate all permutations. It iterates over each element in the array, swaps it with the current element, and recursively generates permutations for the remaining elements. After each recursive call, it backtracks by swapping the elements back to their original positions.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(result, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& nums, int start) {
        if (start == nums.size()) {
            result.push_back(nums);
        }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            backtrack(result, nums, start + 1);
            swap(nums[start], nums[i]);
        }
    }
};
```

## Test Cases
```
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
Input: [0, 1]
Output: [[0, 1], [1, 0]]
```

## Key Takeaways
- The backtracking approach is useful for generating all permutations of a given array.
- The time complexity is O(N!) because there are N! possible permutations for an array of length N.
- The space complexity is O(N) because of the recursive call stack.