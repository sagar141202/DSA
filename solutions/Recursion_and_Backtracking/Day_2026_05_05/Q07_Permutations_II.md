# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input collection is given as an array of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input array. For example, given the array [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The length of the input array will be between 1 and 9, and each integer in the array will be between 1 and 9.

## Approach
The algorithm uses recursion and backtracking to generate all permutations. It sorts the input array to handle duplicates, and then recursively generates all permutations by swapping each element with the remaining elements. If a duplicate element is encountered, it skips the current iteration to avoid duplicate permutations.

## Complexity
- Time: O(N! / (K1! * K2! * ... * Km!)) where N is the length of the input array, and K1, K2, ..., Km are the frequencies of each distinct element in the array
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
Input: [2, 2, 1, 1]
Output: [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]
```

## Key Takeaways
- Use recursion and backtracking to generate all permutations of the input array
- Sort the input array to handle duplicates
- Use an unordered set to keep track of used elements in the current permutation to avoid duplicates