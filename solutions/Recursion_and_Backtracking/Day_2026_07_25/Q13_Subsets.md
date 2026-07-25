# Subsets

## Problem Statement
Given a set of distinct integers, nums, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given nums = [1, 2, 3], the solution is `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`. The input array will have a maximum length of 10, and all elements will be between -10 and 10.

## Approach
The approach is to use backtracking to generate all subsets. We can start with an empty subset and then add each element from the input set one by one. The key idea is to use recursion to explore all possible subsets. We will use a helper function to generate subsets recursively.

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
```

## Key Takeaways
- Use backtracking to generate all subsets of a given set.
- Start with an empty subset and add elements one by one using recursion.
- Use a helper function to generate subsets recursively and explore all possible subsets.