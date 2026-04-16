# Permutations

## Problem Statement
Given a collection of distinct numbers, return all possible permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a permutation of the input list. For example, given the input [1, 2, 3], the output should be [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]].

## Approach
The solution uses recursion and backtracking to generate all permutations. It iterates over each element in the input list, adds it to the current permutation, and recursively generates all permutations of the remaining elements. The base case is when the input list is empty, in which case the current permutation is added to the result list.

## Complexity
- Time: O(n!)
- Space: O(n!)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == nums.size()) {
        result.push_back(nums);
        return;
    }
    for (int i = start; i < nums.size(); i++) {
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int>> result;
    backtrack(nums, 0, result);
    return result;
}
```

## Test Cases
```
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of a list.
- The time complexity is O(n!) because there are n! permutations of a list of length n.
- The space complexity is O(n!) because we need to store all permutations in the result list.