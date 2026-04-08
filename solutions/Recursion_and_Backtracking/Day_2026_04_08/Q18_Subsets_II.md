# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given the array `[1, 2, 2]`, the subsets are `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The integers in the array are in the range `[1, 200]`, and the size of the array is in the range `[1, 20]`.

## Approach
The solution utilizes recursion and backtracking to generate all possible subsets. It sorts the input array to handle duplicates and skips adding a duplicate element to the current subset.

## Complexity
- Time: O(2^n) where n is the number of elements in the array
- Space: O(n) for the recursion call stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        sort(nums.begin(), nums.end());
        backtrack(result, current, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current);
        for (int i = start; i < nums.size(); i++) {
            // Skip duplicates
            if (i > start && nums[i] == nums[i - 1]) continue;
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
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
- Recursion and backtracking can be used to generate all possible subsets of a given array.
- Sorting the input array helps handle duplicate elements.
- By skipping duplicate elements during the backtracking process, we avoid adding duplicate subsets to the result.