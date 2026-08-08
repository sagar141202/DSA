# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input array may contain duplicate elements, and the output should not have any duplicate permutations. For example, given the array [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]].

## Approach
The approach to solve this problem is to use recursion and backtracking, sorting the array first to handle duplicates. We will use a helper function to generate all permutations and skip duplicate elements.

## Complexity
- Time: O(N! / (K1! * K2! * ... * Km!)) where N is the total number of elements, and K1, K2, ..., Km are the counts of each duplicate element
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, vector<bool>& visited, vector<int>& path, vector<vector<int>>& result) {
    if (path.size() == nums.size()) {
        result.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (visited[i] || (i > 0 && nums[i] == nums[i - 1] && !visited[i - 1])) {
            continue;
        }
        visited[i] = true;
        path.push_back(nums[i]);
        backtrack(nums, visited, path, result);
        path.pop_back();
        visited[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    vector<bool> visited(nums.size(), false);
    vector<int> path;
    sort(nums.begin(), nums.end());
    backtrack(nums, visited, path, result);
    return result;
}
```

## Test Cases
```
Input: [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
```

## Key Takeaways
- To handle duplicate elements, we need to sort the array first and then skip duplicate elements during backtracking.
- We use a visited array to keep track of elements that have been used in the current permutation.
- The time complexity is affected by the number of duplicate elements, as we divide by the factorial of the count of each duplicate element.