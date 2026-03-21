# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, and return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is [1, 2, 2], the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is not null, and the length of the input array is not more than 30.

## Approach
The problem can be solved using recursion and backtracking, sorting the input array and skipping duplicates to avoid duplicate subsets. The algorithm starts with an empty subset and recursively adds elements to the subset. If a duplicate element is encountered, it is skipped to avoid duplicate subsets.

## Complexity
- Time: O(2^n) where n is the number of elements in the input array, as there are 2^n possible subsets in the worst case.
- Space: O(2^n) for storing the subsets.

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
- Recursion and backtracking can be used to generate all possible subsets of a given array.
- To avoid duplicate subsets when the input array contains duplicates, the array should be sorted and duplicates should be skipped during the backtracking process.
- The time complexity of the algorithm is O(2^n) due to the generation of all possible subsets, and the space complexity is also O(2^n) for storing the subsets.