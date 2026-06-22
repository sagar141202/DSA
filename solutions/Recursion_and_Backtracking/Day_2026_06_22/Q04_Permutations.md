# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. For example, if the input is [1, 2, 3], a solution set is [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The input array will have a length between 1 and 9, and each element will be between 1 and 10.

## Approach
The problem can be solved using recursion and backtracking. The idea is to fix each element in the array as the first element and generate all permutations of the remaining elements. This process continues until all elements have been fixed as the first element.

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
Input: [0, 1]
Output: [[0, 1], [1, 0]]
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of the input array.
- Fix each element as the first element and generate permutations of the remaining elements.
- Use swap operation to swap elements in the array, and backtrack to restore the original array.