# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all unique permutations. The input collection is given as a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, given the input `[1, 1, 2]`, the output should be `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`. The length of the input list is at most 10, and the elements are in the range [1, 1000]. The input list may contain duplicate integers.

## Approach
To solve this problem, we can use a recursive backtracking approach, sorting the input list first to handle duplicates. We then iterate over each element in the list, adding it to the current permutation and recursively generating permutations for the remaining elements. To avoid duplicates, we skip the current iteration if the current element is the same as the previous one.

## Complexity
- Time: O(N! / (K1! * K2! * ... * Km!)) where N is the length of the input list and K1, K2, ..., Km are the frequencies of each distinct element
- Space: O(N) for the recursion stack and the space needed to store the permutations

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
        // Check for duplicates
        if (i > start && nums[i] == nums[start]) continue;
        // Swap elements
        swap(nums[start], nums[i]);
        // Recur for the next index
        backtrack(nums, start + 1, result);
        // Backtrack
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
- Sorting the input list helps handle duplicates by grouping identical elements together.
- Using a recursive backtracking approach allows for efficient generation of all unique permutations.
- Skipping duplicate elements during iteration ensures that only unique permutations are added to the result.