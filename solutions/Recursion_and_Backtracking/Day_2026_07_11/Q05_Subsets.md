# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets (the power set). The solution should be implemented using recursion and backtracking. The set is represented as a vector of integers, and the subsets should be returned as a vector of vectors of integers. For example, given the set [1, 2, 3], the power set is [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]. The input set is guaranteed to have at most 20 elements.

## Approach
The algorithm uses recursion to generate all possible subsets by iterating over each element in the set and deciding whether to include it in the current subset or not. This decision is made using backtracking, where we explore all possible branches of the recursion tree. The base case for the recursion is when we have processed all elements in the set.

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
- Recursion and backtracking can be used to solve problems that involve exploring all possible combinations of a set of elements.
- The time complexity of generating all subsets of a set is O(2^n), where n is the size of the set.
- The space complexity of storing all subsets of a set is also O(2^n), where n is the size of the set.