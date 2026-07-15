# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is [1,2,2], the output should be [[],[1],[1,2],[1,2,2],[2],[2,2]].

## Approach
The problem can be solved using recursion and backtracking. We will sort the input array to handle duplicates and then generate all subsets using a recursive function. The key idea is to skip duplicate elements during the recursive calls.

## Complexity
- Time: O(2^n * n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<int>& subset, vector<vector<int>>& result) {
    result.push_back(subset);
    for (int i = start; i < nums.size(); i++) {
        // skip duplicates
        if (i > start && nums[i] == nums[i-1]) continue;
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
Input: [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Input: [0]
Output: [[],[0]]
```

## Key Takeaways
- Sorting the input array is necessary to handle duplicates.
- Using a recursive function with backtracking is a suitable approach for generating all subsets.
- Skipping duplicate elements during recursive calls is crucial to avoid duplicate subsets in the result.