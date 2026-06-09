# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, and no duplicate should be in the output, return all possible subsets. The problem requires generating all unique subsets from the given set of numbers. For example, if the input is [1, 2, 2], the output should be [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]. The input set can have a maximum size of 30 and each element can range from 0 to 100.

## Approach
The approach involves using recursion and backtracking to generate all subsets. We will sort the input array first to handle duplicates. Then, we will use a recursive function to generate all subsets.

## Complexity
- Time: O(2^n * n) where n is the size of the input array, because in the worst case, we are generating all subsets and each subset can have up to n elements.
- Space: O(2^n * n) for storing the result and the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(int start, vector<int>& nums, vector<int>& subset, vector<vector<int>>& result) {
    result.push_back(subset);
    for (int i = start; i < nums.size(); i++) {
        // skip duplicates
        if (i > start && nums[i] == nums[i - 1]) continue;
        subset.push_back(nums[i]);
        backtrack(i + 1, nums, subset, result);
        subset.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> subset;
    sort(nums.begin(), nums.end());
    backtrack(0, nums, subset, result);
    return result;
}
```

## Test Cases
```
Input: [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
Input: [0]
Output: [[], [0]]
```

## Key Takeaways
- Sort the input array to handle duplicates.
- Use recursion and backtracking to generate all subsets.
- Skip duplicates in the recursive function to avoid duplicate subsets in the result.