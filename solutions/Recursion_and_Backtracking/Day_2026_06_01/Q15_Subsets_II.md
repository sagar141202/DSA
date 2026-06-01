# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is `[1, 2, 2]`, the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array can contain up to 100 elements, and each element can range from 0 to 100. The order of subsets in the output does not matter.

## Approach
The solution involves using recursion and backtracking to generate all subsets. We will sort the input array first to handle duplicates. Then, we'll use a recursive function to build subsets, skipping duplicates to ensure uniqueness.

## Complexity
- Time: O(2^n * n) where n is the number of elements in the input array, due to generating all subsets and copying them to the result.
- Space: O(2^n * n) for storing the result, as in the worst case, the total number of subsets (including the empty subset) is 2^n.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<int>& path, vector<vector<int>>& result) {
    result.push_back(path);
    for (int i = start; i < nums.size(); ++i) {
        // Skip duplicates to ensure unique subsets
        if (i > start && nums[i] == nums[i-1]) continue;
        path.push_back(nums[i]);
        backtrack(nums, i + 1, path, result);
        path.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> path;
    sort(nums.begin(), nums.end()); // Sort to handle duplicates
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
- Recursion and backtracking can be used to generate all possible subsets of a given set.
- Sorting the input array helps in handling duplicates by ensuring that identical elements are adjacent, making it easier to skip them and avoid duplicate subsets.
- The time and space complexity of this solution is exponential due to the nature of generating all subsets.