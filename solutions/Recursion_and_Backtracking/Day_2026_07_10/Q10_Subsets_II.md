# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates and no negative numbers, return all possible subsets. The solution set must not contain duplicate subsets. For example, if the input is [1, 2, 2], the output will be [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]].

## Approach
The approach involves using recursion and backtracking to generate all possible subsets. We will sort the input array first and skip duplicates during the recursion process. The base case for the recursion is when the start index exceeds the size of the input array.

## Complexity
- Time: O(2^n * n)
- Space: O(n)

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
- Use recursion and backtracking to generate all possible subsets of the input array.
- Sort the input array and skip duplicates during the recursion process to avoid duplicate subsets in the result.
- The time complexity is O(2^n * n) due to generating all subsets and copying them to the result, where n is the size of the input array.