# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all unique permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The input list is not guaranteed to be sorted, and the output permutations should not contain duplicates.

## Approach
The solution uses recursion and backtracking to generate all permutations. It sorts the input list to handle duplicates and skips duplicate elements during the recursion. The algorithm selects each element in the list, adds it to the current permutation, and recursively generates permutations for the remaining elements.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the input list and k1, k2, ..., kn are the frequencies of each distinct element
- Space: O(N) for the recursion stack and the current permutation

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
        if (i > start && nums[i] == nums[start]) continue;
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());
    backtrack(nums, 0, result);
    return result;
}
```

## Test Cases
```
Input: [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
Input: [2, 1, 1]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

## Key Takeaways
- Sort the input list to handle duplicates
- Use recursion and backtracking to generate all permutations
- Skip duplicate elements during the recursion to avoid duplicate permutations