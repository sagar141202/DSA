# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is `[1, 2, 2]`, the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is sorted, and the length of the input array will not exceed 10.

## Approach
The solution utilizes recursion and backtracking to generate all subsets. It sorts the input array and skips duplicates to avoid duplicate subsets. The algorithm uses a helper function to recursively generate subsets.

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
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible subsets of a given array.
- Sorting the input array and skipping duplicates can avoid duplicate subsets.
- The time complexity of generating all subsets is O(2^n), where n is the number of elements in the input array.