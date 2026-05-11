# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given the set `[1, 2, 2]`, the subsets are `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is not sorted, and the length of the input array is not more than 10. The elements in the array are in the range of 0 to 9.

## Approach
The approach involves using recursion and backtracking to generate all possible subsets. We will sort the input array to handle duplicates and skip them during the backtracking process. The algorithm will explore all possible branches of the subset tree.

## Complexity
- Time: O(2^n) where n is the number of elements in the input array, as in the worst case, we generate all possible subsets.
- Space: O(2^n) for storing the subsets and O(n) for the recursion stack.

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
            // Skip duplicates to avoid duplicate subsets
            if (i > start && nums[i] == nums[i - 1]) continue;
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
Input: [0]
Output: [[], [0]]
```

## Key Takeaways
- Use sorting to handle duplicates in the input array.
- Implement backtracking to explore all possible subsets.
- Skip duplicates during the backtracking process to avoid generating duplicate subsets.