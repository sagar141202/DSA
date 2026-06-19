# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, if the input is [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The length of the input list will be between 1 and 9, and each integer in the list will be between 1 and 9.

## Approach
This problem can be solved using recursion and backtracking. We will use a helper function to generate all permutations and skip duplicates by sorting the input list and skipping the same numbers.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the input list, and k1, k2, ..., kn are the counts of each number in the list
- Space: O(N) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, vector<bool>& visited, vector<int>& path, vector<vector<int>>& res) {
    if (path.size() == nums.size()) {
        res.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (visited[i] || (i > 0 && nums[i] == nums[i-1] && !visited[i-1])) {
            continue;
        }
        visited[i] = true;
        path.push_back(nums[i]);
        backtrack(nums, visited, path, res);
        path.pop_back();
        visited[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> res;
    vector<bool> visited(nums.size(), false);
    vector<int> path;
    sort(nums.begin(), nums.end());
    backtrack(nums, visited, path, res);
    return res;
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
- Use recursion and backtracking to generate all permutations of the input list
- Sort the input list and skip duplicates to ensure uniqueness of permutations
- Use a helper function to generate permutations and a main function to sort the input list and call the helper function