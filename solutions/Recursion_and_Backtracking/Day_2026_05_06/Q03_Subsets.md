# Subsets

## Problem Statement
Given a set of distinct integers, nums, return all possible subsets (the power set). The solution set must not contain duplicate subsets. The given set can contain any number of integers, and the integers can be positive, negative, or zero. For example, given nums = [1, 2, 3], the output should be [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].

## Approach
The problem can be solved using recursion and backtracking. We will generate all subsets by choosing to include or exclude each element from the current subset. This approach ensures that we generate all possible subsets. We start with an empty subset and then recursively add elements to it.

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

// Alternatively, using iteration
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result = {{}};
        for (int num : nums) {
            int size = result.size();
            for (int i = 0; i < size; i++) {
                vector<int> newSubset = result[i];
                newSubset.push_back(num);
                result.push_back(newSubset);
            }
        }
        return result;
    }
};
```

## Test Cases
```
Input: [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
Input: [0]
Output: [[], [0]]
```

## Key Takeaways
- The key to solving this problem is understanding how recursion and backtracking work.
- We use a helper function (backtrack) to generate all subsets recursively.
- The iterative approach is also a good alternative to the recursive solution.