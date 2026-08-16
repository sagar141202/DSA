# Subsets

## Problem Statement
Given a set of distinct integers, find all possible subsets of the set. The set can contain duplicate elements, but each subset should be unique. For example, given the set [1, 2, 3], the subsets are [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]. The input is a vector of integers, and the output should be a vector of vectors, where each inner vector is a subset.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start with an empty subset and then recursively add each element to the subset. We use backtracking to remove the last added element when we have explored all possible subsets with that element.

## Complexity
- Time: O(2^n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> subset;
        backtrack(result, subset, nums, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& subset, vector<int>& nums, int start) {
        result.push_back(subset);
        for (int i = start; i < nums.size(); i++) {
            subset.push_back(nums[i]);
            backtrack(result, subset, nums, i + 1);
            subset.pop_back();
        }
    }
};
```

## Test Cases
```
Input: [1, 2, 3]
Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
Input: [0]
Output: [[], [0]]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible subsets of a set.
- Start with an empty subset and recursively add each element to the subset.
- Use backtracking to remove the last added element when we have explored all possible subsets with that element.