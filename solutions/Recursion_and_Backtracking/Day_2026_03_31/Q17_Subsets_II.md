# Subsets II

## Problem Statement
Given a collection of integers that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given `[1, 2, 2]`, the subsets are `[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]`. The length of the input array will not exceed 10.

## Approach
The solution utilizes recursion and backtracking to generate all possible subsets. It sorts the input array and skips duplicate elements to avoid duplicate subsets. The algorithm iterates over the array, deciding whether to include each element in the current subset or not.

## Complexity
- Time: O(2^n) where n is the number of elements in the input array, as in the worst case, we generate all possible subsets.
- Space: O(2^n) for storing the result, and O(n) for the recursion stack in the worst case.

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
Output: [
  [],
  [1],
  [1,2],
  [1,2,2],
  [2],
  [2,2]
]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible subsets of a given set.
- Sorting the input array and skipping duplicates helps avoid duplicate subsets.
- The time and space complexity of the solution is exponential due to the generation of all possible subsets.