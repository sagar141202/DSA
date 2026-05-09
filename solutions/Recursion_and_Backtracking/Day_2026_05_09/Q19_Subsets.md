# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets (the power set). The solution should be implemented using recursion and backtracking. The input is a vector of integers, and the output is a vector of vectors, where each inner vector represents a subset. For example, given the input [1, 2, 3], the output should be [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]. The input vector is guaranteed to have at most 10 elements, and each element is between 1 and 100.

## Approach
The algorithm uses recursion and backtracking to generate all subsets. It starts with an empty subset and recursively adds each element to the current subset, then backtracks to explore other possibilities. The base case is when all elements have been considered, at which point the current subset is added to the result.

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
- Use recursion and backtracking to generate all subsets of a given set.
- Start with an empty subset and recursively add each element to the current subset.
- Backtrack to explore other possibilities after adding each element.