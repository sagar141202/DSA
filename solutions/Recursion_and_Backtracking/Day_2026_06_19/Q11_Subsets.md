# Subsets

## Problem Statement
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. The subsets can be in any order, and the order of elements within a subset does not matter. For example, if `nums = [1, 2, 3]`, the output should be `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`. The size of `nums` is between 1 and 10, and all elements are between 1 and 100.

## Approach
The problem can be solved using recursion and backtracking, where we generate all possible subsets by either including or excluding each element. We start with an empty subset and then recursively add or remove elements to generate all subsets. This approach ensures that we cover all possible combinations of elements.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, nums, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current);
        for (int i = start; i < nums.size(); i++) {
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
        }
    }
};
```

## Test Cases
```
Input: nums = [1, 2, 3]
Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible subsets of a given set.
- The time complexity of this approach is exponential (2^n) due to the recursive nature of the solution.
- The space complexity is also exponential (2^n) as we need to store all possible subsets in the result.