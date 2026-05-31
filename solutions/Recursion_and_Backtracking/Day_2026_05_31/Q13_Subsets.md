# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets (the power set). The solution should be in lexicographic order. For example, given the set [1, 2, 3], the subsets are [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]. The input set will have a maximum of 20 elements and each element will be between 1 and 1000.

## Approach
The approach is to use recursion and backtracking to generate all possible subsets. We start with an empty subset and then recursively add each element to the subset. The key is to use a recursive function that takes the current subset and the remaining elements as parameters.

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
- Recursion and backtracking can be used to generate all possible subsets of a set.
- The time complexity is O(2^n) because we are generating 2^n subsets.
- The space complexity is O(2^n) because we are storing all subsets in the result vector.