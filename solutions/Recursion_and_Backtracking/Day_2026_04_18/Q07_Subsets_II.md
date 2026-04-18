# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is `[1, 2, 2]`, the output will be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is sorted, and the size of the input array is in the range [0, 10].

## Approach
The approach is to use recursion and backtracking to generate all possible subsets. We will sort the array first and then use a recursive function to generate subsets. If the current element is the same as the previous one, we will skip it to avoid duplicates.

## Complexity
- Time: O(2^n) where n is the number of elements in the input array, since in the worst case, we generate all possible subsets.
- Space: O(n) for the recursion stack and to store the subsets.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> path;
        sort(nums.begin(), nums.end());
        backtrack(result, path, nums, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& path, vector<int>& nums, int start) {
        result.push_back(path);
        for (int i = start; i < nums.size(); i++) {
            // skip duplicates
            if (i > start && nums[i] == nums[i - 1]) continue;
            path.push_back(nums[i]);
            backtrack(result, path, nums, i + 1);
            path.pop_back();
        }
    }
};
```

## Test Cases
```
Input: [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
Input: [0]
Output: [[], [0]]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible subsets.
- Sort the input array to handle duplicates.
- Skip duplicates by checking if the current element is the same as the previous one.