# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The length of the input list will not exceed 10, and the elements in the list will be between 1 and 10.

## Approach
The algorithm uses recursion and backtracking to generate all permutations. It iterates over the input list, swaps each element with the current position, and recursively generates all permutations of the remaining list. To avoid duplicates, it skips the current iteration if the current element is the same as the previous one.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the input list, and k1, k2, ..., kn are the frequencies of each element
- Space: O(N) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == nums.size()) {
        result.push_back(nums);
        return;
    }
    unordered_set<int> used;
    for (int i = start; i < nums.size(); i++) {
        if (used.find(nums[i]) != used.end()) continue;
        used.insert(nums[i]);
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
- Use backtracking to generate all permutations of the input list
- Use an unordered set to skip duplicates in the current iteration
- Sort the input list to ensure that duplicate elements are adjacent to each other