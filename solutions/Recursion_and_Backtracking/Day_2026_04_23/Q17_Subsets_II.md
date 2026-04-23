# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is [1, 2, 2], the output should be [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]. The input array can contain up to 100 elements, and each element can be in the range of -10 to 10.

## Approach
The algorithm uses recursion and backtracking to generate all subsets. It sorts the input array first to handle duplicates and then recursively adds each element to the current subset. If the current element is the same as the previous one, it skips the current element to avoid duplicate subsets.

## Complexity
- Time: O(2^n) where n is the number of elements in the input array
- Space: O(2^n) for storing the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<int>& subset, vector<vector<int>>& result) {
    result.push_back(subset);
    for (int i = start; i < nums.size(); i++) {
        // Skip duplicates to avoid duplicate subsets
        if (i > start && nums[i] == nums[i - 1]) continue;
        subset.push_back(nums[i]);
        backtrack(nums, i + 1, subset, result);
        subset.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    vector<int> subset;
    backtrack(nums, 0, subset, result);
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
- Sort the input array to handle duplicates
- Use recursion and backtracking to generate all subsets
- Skip duplicates to avoid duplicate subsets