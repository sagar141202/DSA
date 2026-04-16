# Subsets

## Problem Statement
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if `nums = [1, 2, 3]`, the solution is `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`. The array size will not exceed 10.

## Approach
The problem can be solved using backtracking, where we try to include or exclude each element from the current subset. This approach ensures that we generate all possible subsets. We use recursion to explore all possibilities.

## Complexity
- Time: O(2^n)
- Space: O(n)

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
- Recursion and backtracking can be used to solve problems that involve exploring all possible combinations or permutations.
- The time complexity of this solution is exponential because we are generating all possible subsets.
- The space complexity is linear because we need to store the current subset and the result.