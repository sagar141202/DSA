# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is `[1, 2, 3]`, a solution set is `[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]`. The input will not contain duplicates, and the length of the input will be between 1 and 6.

## Approach
The algorithm uses recursion and backtracking to generate all permutations. It iterates over each element in the input array, swaps it with the first element, and recursively generates permutations for the remaining elements. After each recursive call, it backtracks by swapping the elements back to their original positions.

## Complexity
- Time: O(n!)
- Space: O(n)

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
```

## Key Takeaways
- Recursion and backtracking can be used to generate all permutations of a given array.
- The time complexity is O(n!) because there are n! possible permutations.
- The space complexity is O(n) for the recursive call stack.