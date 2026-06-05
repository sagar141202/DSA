# Subsets II

## Problem Statement
Given a collection of integers, `nums`, that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. It is guaranteed that `0 <= nums.size() <= 30`. For example, if `nums = [1, 2, 2]`, a solution is `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`.

## Approach
The algorithm uses recursion and backtracking to generate all possible subsets. It sorts the input array to handle duplicates and skips the same elements in the recursive calls. The base case is when the start index reaches the end of the array.

## Complexity
- Time: O(2^n) where n is the number of elements in the array
- Space: O(2^n) for storing the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        sort(nums.begin(), nums.end());
        backtrack(result, current, nums, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current);
        for (int i = start; i < nums.size(); i++) {
            // Skip duplicates
            if (i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
        }
    }
};
```

## Test Cases
```
Input: [1, 2, 2]
Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible subsets.
- Sort the input array and skip duplicates to avoid duplicate subsets.
- Use a start index to keep track of the current position in the array.