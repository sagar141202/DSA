# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets. The solution should be implemented using recursion and backtracking. The input is a vector of integers, and the output should be a vector of vectors, where each inner vector represents a subset. For example, given the input [1, 2, 3], the output should be [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]. The input vector will contain at most 10 integers, and each integer will be between 1 and 100.

## Approach
The algorithm uses recursion to generate all subsets by either including or excluding the current element. This is achieved through backtracking, where we explore all possible branches of the recursion tree. The base case is when the input vector is empty, at which point we return a vector containing an empty subset.

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
- Recursion and backtracking can be used to generate all possible subsets of a given set.
- The time complexity is exponential due to the recursive nature of the algorithm, where each element can either be included or excluded from the subset.
- The space complexity is also exponential, as we need to store all generated subsets in the result vector.