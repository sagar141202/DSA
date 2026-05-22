# Subsets

## Problem Statement
Given a set of distinct integers, nums, return all possible subsets (the power set). The solution set must not contain duplicate subsets. It is guaranteed that 0 <= nums.length <= 20 and -10^9 <= nums[i] <= 10^9 for all i in the range [0, nums.length). For example, if nums = [1, 2, 3], a solution is [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].

## Approach
The algorithm uses recursion and backtracking to generate all subsets. It iterates over the input set, adding each element to the current subset or not, thus exploring all possible combinations. The base case for recursion is when all elements have been processed.

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
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int index) {
        result.push_back(current);
        for (int i = index; i < nums.size(); i++) {
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
- The use of recursion and backtracking allows for an elegant solution to the subsets problem.
- The time and space complexity are both exponential due to the nature of generating the power set.
- The solution can be applied to any set of distinct integers, making it a versatile algorithm.