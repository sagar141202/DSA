# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The length of the input list is at most 10, and the elements are in the range [1, 10^5].

## Approach
The approach to solve this problem is to use backtracking and recursion to generate all permutations, while skipping duplicates to ensure uniqueness. We sort the input list to group duplicate elements together, making it easier to skip them.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the input list, and k1, k2, ..., kn are the frequencies of each unique element
- Space: O(N) for the recursive call stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, vector<bool>& used, vector<int>& path, vector<vector<int>>& result) {
    if (path.size() == nums.size()) {
        result.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        // Skip duplicates and used elements
        if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) {
            continue;
        }
        used[i] = true;
        path.push_back(nums[i]);
        backtrack(nums, used, path, result);
        path.pop_back();
        used[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    vector<bool> used(nums.size(), false);
    vector<int> path;
    sort(nums.begin(), nums.end());
    backtrack(nums, used, path, result);
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
- Use backtracking and recursion to generate all permutations of the input list
- Skip duplicates by checking if the current element is the same as the previous one and the previous one has not been used
- Use a boolean array to keep track of used elements to avoid duplicates in the result