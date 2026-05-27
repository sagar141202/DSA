# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is [1, 2, 2], the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is not null and the length of the input array is not more than 100.

## Approach
The approach involves using backtracking to generate all possible subsets. We sort the input array and skip the duplicates to avoid duplicate subsets. The base case is when the start index equals the size of the array, at which point we add the current subset to the result. 

## Complexity
- Time: O(2^n) where n is the number of elements in the array, since in the worst case, we generate all possible subsets.
- Space: O(2^n) for storing the subsets.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<int>& subset, vector<vector<int>>& result) {
    result.push_back(subset);
    for (int i = start; i < nums.size(); i++) {
        // skip duplicates
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
Input: [0]
Output: [[], [0]]
```

## Key Takeaways
- To avoid duplicate subsets, we sort the input array and skip duplicates during backtracking.
- The use of backtracking allows us to efficiently generate all possible subsets of the input array.
- We use a helper function `backtrack` to perform the recursive operations and build the subsets.