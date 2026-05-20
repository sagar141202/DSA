# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets. The solution must not contain duplicate subsets. For example, if the input is [1, 2, 2], the output should be [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]. The input array can contain up to 100 elements, and each element can be in the range [-10, 10]. 

## Approach
The approach to solve this problem involves using recursion and backtracking to generate all possible subsets. We will sort the input array first and then use a recursive function to generate the subsets, skipping duplicates in the process. 

## Complexity
- Time: O(2^n * n) where n is the number of elements in the input array, because in the worst case, we are generating all possible subsets and sorting them.
- Space: O(2^n * n) because in the worst case, we are storing all possible subsets.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        sort(nums.begin(), nums.end()); // sort the input array
        backtrack(result, current, nums, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current); // add the current subset to the result
        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i - 1]) continue; // skip duplicates
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
- Sorting the input array helps in skipping duplicates.
- Using recursion and backtracking is a good approach to generate all possible subsets.
- The time and space complexity can be high for large input arrays.