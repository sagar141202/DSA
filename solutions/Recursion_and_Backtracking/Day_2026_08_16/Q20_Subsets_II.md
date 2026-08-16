# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, and return all possible subsets (the power set). Each subset should not contain duplicate subsets. For example, given `[1, 2, 2]`, the result should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is not null, and the elements in the array are not null. The size of the input array is not more than 30.

## Approach
The problem can be solved using recursion and backtracking. We will use a recursive function to generate all subsets and use backtracking to avoid duplicate subsets. The key idea is to sort the array first and skip the duplicate elements during the recursion.

## Complexity
- Time: O(2^n) where n is the number of elements in the array, as there are 2^n possible subsets.
- Space: O(2^n) for storing the result, and O(n) for the recursion stack.

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
            // skip duplicate elements
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
- Sort the array before generating subsets to handle duplicates.
- Use a recursive function with backtracking to generate all subsets.
- Skip duplicate elements during the recursion to avoid duplicate subsets.