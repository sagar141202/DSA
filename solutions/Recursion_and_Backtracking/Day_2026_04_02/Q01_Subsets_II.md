# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is `[1, 2, 2]`, the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array can contain duplicate elements, but the output should not have duplicate subsets.

## Approach
The solution uses recursion and backtracking to generate all possible subsets. It sorts the input array first and skips duplicate elements during the backtracking process. This ensures that duplicate subsets are not generated.

## Complexity
- Time: O(2^n) where n is the number of elements in the input array, as in the worst case, we generate all possible subsets.
- Space: O(2^n) for storing the result, and O(n) for the recursion stack.

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
            // Skip duplicate elements
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
- Sort the input array before generating subsets to handle duplicates.
- Use a `start` index to keep track of the current position in the array during backtracking.
- Skip duplicate elements by checking if the current element is the same as the previous one.