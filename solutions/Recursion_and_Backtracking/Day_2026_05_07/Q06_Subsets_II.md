# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is `[1, 2, 2]`, the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is sorted, and the length of the input array will not exceed 10.

## Approach
The problem can be solved using recursion and backtracking, by generating all subsets of the given array and skipping duplicates. The key idea is to sort the array first and then use a recursive function to generate all subsets.

## Complexity
- Time: O(2^n) where n is the number of elements in the array, because in the worst case, we generate all possible subsets.
- Space: O(2^n) for storing the result, and O(n) for the recursive call stack.

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
- The problem requires generating all possible subsets of a given array with duplicates, and the solution set must not contain duplicate subsets.
- The input array should be sorted before generating subsets to handle duplicates correctly.
- The recursive function `backtrack` is used to generate all subsets, and it skips duplicates by checking if the current element is the same as the previous one.