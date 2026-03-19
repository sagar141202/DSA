# Subsets

## Problem Statement
Given a set of distinct integers `nums`, return all possible subsets (the power set). The solution set must not contain duplicate subsets. The subsets can be returned in any order. For example, given `nums = [1, 2, 3]`, the output will be `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`. The length of `nums` will be in the range `[1, 10]`, and `1 <= nums[i] <= 10`.

## Approach
We will use recursion and backtracking to generate all possible subsets. The algorithm works by adding each element to the current subset and then recursively generating all subsets of the remaining elements. The base case is when all elements have been processed, at which point we add the current subset to the result.

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
- Use recursion and backtracking to generate all possible subsets of a given set of integers.
- The time complexity is exponential due to the generation of the power set.
- The space complexity is also exponential due to the storage of all subsets in the result.