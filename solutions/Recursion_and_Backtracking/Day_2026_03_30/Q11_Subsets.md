# Subsets

## Problem Statement
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. The input array can contain any number of elements, and the elements can be any integer. For example, if the input is `[1, 2, 3]`, the output will be `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`.

## Approach
The problem can be solved using recursion and backtracking. The idea is to consider each element in the array and decide whether to include it in the current subset or not. This process is repeated for all elements, resulting in all possible subsets. The base case for the recursion is when all elements have been considered.

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
Input: [1, 2, 3]
Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
Input: [0]
Output: [[], [0]]
```

## Key Takeaways
- The recursion and backtracking approach is useful for solving problems that involve generating all possible combinations of elements.
- The time complexity of this approach is exponential (O(2^n)) because each element can be either included or excluded from the subset.
- The space complexity is also exponential (O(2^n)) because in the worst case, we need to store all possible subsets.