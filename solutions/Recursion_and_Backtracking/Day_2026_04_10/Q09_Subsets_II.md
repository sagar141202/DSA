# Subsets II

## Problem Statement
Given a collection of integers that may contain duplicates, nums, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given nums = [1, 2, 2], the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is not guaranteed to be sorted, and the output does not need to be in a specific order.

## Approach
This problem can be solved using recursion and backtracking. We start with an empty subset and then recursively add each element from the input array to the current subset. To avoid duplicate subsets, we sort the input array and skip duplicate elements during recursion.

## Complexity
- Time: O(2^n * n) where n is the number of elements in the input array, as we generate all possible subsets and sort the input array.
- Space: O(2^n * n) for storing the result and the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        sort(nums.begin(), nums.end()); // sort to handle duplicates
        backtrack(result, current, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int index) {
        result.push_back(current); // add current subset to result
        for (int i = index; i < nums.size(); i++) {
            if (i > index && nums[i] == nums[i - 1]) continue; // skip duplicates
            current.push_back(nums[i]); // add current element to subset
            backtrack(result, current, nums, i + 1); // recurse
            current.pop_back(); // backtrack
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
- Recursion and backtracking are useful for problems involving combinatorial explosion, such as generating all possible subsets.
- To handle duplicate elements, sort the input array and skip duplicates during recursion.
- The time and space complexity of this solution are exponential due to the generation of all possible subsets.