# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input array may contain duplicate elements, and the output should not have any duplicate permutations. For example, given the array `[1, 1, 2]`, the output should be `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`. The input array is not null, and the length of the array is not larger than 10.

## Approach
The algorithm uses recursion and backtracking to generate all permutations. It iterates through the array, selects each element, and recursively generates permutations for the remaining elements. To avoid duplicates, it skips the current iteration if the current element is the same as the previous one.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the array and k1, k2, ..., kn are the frequencies of each element
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
        if (used.find(nums[i]) != used.end()) {
            continue;
        }
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
- Use recursion and backtracking to generate all permutations of the array
- Use an unordered set to keep track of used elements and skip duplicates
- Sort the input array to ensure that duplicate elements are adjacent to each other