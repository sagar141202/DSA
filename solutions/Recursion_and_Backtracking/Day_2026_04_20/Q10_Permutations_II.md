# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. For example, given the input [1, 1, 2], the function should return [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The input array will contain integers between 1 and 9, and the length of the array will be between 1 and 8.

## Approach
The solution utilizes a recursive backtracking approach to generate all permutations of the input array. It sorts the array to handle duplicates and skips the same element to avoid duplicate permutations. The base case for recursion is when the current permutation is complete.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the array and k1, k2, ..., kn are the frequencies of each number
- Space: O(N) for recursion stack

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
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of an array.
- Sort the array to handle duplicates and skip the same element to avoid duplicate permutations.
- Use a base case for recursion to stop the recursion when the current permutation is complete.