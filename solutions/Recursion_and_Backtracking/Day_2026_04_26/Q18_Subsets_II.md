# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is [1, 2, 2], the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is sorted, and the length of the input array will not exceed 10.

## Approach
The approach involves using recursion and backtracking to generate all subsets. We will use a helper function to recursively add elements to the current subset. To avoid duplicates, we will skip the current element if it is the same as the previous one.

## Complexity
- Time: O(2^n) where n is the number of elements in the input array
- Space: O(n) for the recursion stack

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
- Use recursion and backtracking to generate all subsets of the input array.
- Sort the input array to handle duplicates.
- Skip the current element if it is the same as the previous one to avoid duplicates in the result.