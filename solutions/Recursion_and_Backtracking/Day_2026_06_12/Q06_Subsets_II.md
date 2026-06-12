# Subsets II

## Problem Statement
Given a collection of integers that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given the array [1, 2, 2], the subsets are: `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The array can contain duplicate elements, but the subsets should not.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all subsets and then remove duplicates. We sort the array to handle duplicates and skip them during recursion.

## Complexity
- Time: O(2^n * n) where n is the number of elements in the array
- Space: O(2^n * n) for storing the subsets

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<int>& subset, vector<vector<int>>& result) {
    result.push_back(subset);
    for (int i = start; i < nums.size(); i++) {
        // Skip duplicates
        if (i > start && nums[i] == nums[i - 1]) continue;
        subset.push_back(nums[i]);
        backtrack(nums, i + 1, subset, result);
        subset.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> subset;
    sort(nums.begin(), nums.end());
    backtrack(nums, 0, subset, result);
    return result;
}
```

## Test Cases
```
Input: [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all subsets of an array.
- To remove duplicate subsets when the array contains duplicates, we can sort the array and skip duplicates during recursion.
- The time complexity is exponential because we are generating all subsets, and the space complexity is also exponential for storing the subsets.