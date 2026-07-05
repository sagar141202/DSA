# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input collection is given as an array of integers. For example, given the array [1,1,2], the function should return [[1,1,2], [1,2,1], [2,1,1]]. The input array will not be empty and will contain at most 20 elements.

## Approach
The solution uses recursion and backtracking to generate all permutations. It sorts the input array first to handle duplicates. Then it uses a recursive function to generate all permutations, skipping duplicates by checking if the current element is the same as the previous one.

## Complexity
- Time: O(N! / (K1! * K2! * ... * Km!)) where N is the total number of elements and K1, K2, ..., Km are the counts of each duplicate element
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
    for (int i = start; i < nums.size(); i++) {
        if (i != start && nums[i] == nums[start]) continue;
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> result;
    backtrack(nums, 0, result);
    return result;
}
```

## Test Cases
```
Input: [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]
Input: [2,2,1,1]
Output: [[1,1,2,2], [1,2,1,2], [1,2,2,1], [2,1,1,2], [2,1,2,1], [2,2,1,1]]
```

## Key Takeaways
- Sort the input array to handle duplicates
- Use recursion and backtracking to generate all permutations
- Skip duplicates by checking if the current element is the same as the previous one