# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, and no two subsets should be the same, return all possible subsets. The integers are given in an array `nums`, and the result should be returned in a non-decreasing order (ascending order). For example, if the input is `[1, 2, 2]`, the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The length of `nums` is between 1 and 10, and all elements in `nums` are between 1 and 10.

## Approach
The solution uses recursion and backtracking to generate all subsets. It sorts the input array first to handle duplicates. Then it uses a recursive function to generate all subsets by either including or excluding the current element. If the current element is the same as the previous one, it skips the current element to avoid duplicates.

## Complexity
- Time: O(2^n) where n is the number of elements in the input array, since in the worst case, we generate all possible subsets.
- Space: O(2^n) for storing the result, and O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<int>& path, vector<vector<int>>& result) {
    result.push_back(path);
    for (int i = start; i < nums.size(); i++) {
        // skip duplicates
        if (i > start && nums[i] == nums[i - 1]) continue;
        path.push_back(nums[i]);
        backtrack(nums, i + 1, path, result);
        path.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> path;
    sort(nums.begin(), nums.end());
    backtrack(nums, 0, path, result);
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
- Recursion and backtracking can be used to solve problems that require generating all possible combinations or permutations.
- Sorting the input array can help handle duplicates and ensure that the result is in non-decreasing order.
- Using a recursive function with a `start` index can help avoid duplicates by skipping the current element if it is the same as the previous one.