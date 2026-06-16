# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a permutation of the input list. For example, given the input [1, 2, 3], the output should be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]. The length of the input list is between 1 and 6, and all elements in the list are between 1 and 10.

## Approach
The solution uses recursion and backtracking to generate all permutations. It iterates over each element in the list, removes it, generates all permutations of the remaining elements, and then inserts the removed element at each possible position in the permutations. This process continues until all elements have been used.

## Complexity
- Time: O(n!)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(result, nums, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& nums, int start) {
        if (start == nums.size()) {
            result.push_back(nums);
        }
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            backtrack(result, nums, start + 1);
            swap(nums[start], nums[i]);
        }
    }
};
```

## Test Cases
```
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Key Takeaways
- Use recursion and backtracking to solve permutation problems.
- The time complexity of permutation problems is often O(n!), where n is the number of elements.
- The space complexity can be O(n) for storing the recursive call stack.