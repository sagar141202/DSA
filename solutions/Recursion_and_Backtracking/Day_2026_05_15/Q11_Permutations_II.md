# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input is an array of integers, and the output should be a vector of vectors, where each inner vector represents a unique permutation of the input array. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The input array can contain duplicate elements, and the output should not contain any duplicate permutations.

## Approach
The problem can be solved using recursion and backtracking. We can sort the input array and then use a recursive function to generate all permutations. To avoid duplicate permutations, we can skip the current element if it is the same as the previous one.

## Complexity
- Time: O(N! / (k1! * k2! * ... * km!)) where N is the length of the input array, and k1, k2, ..., km are the frequencies of each distinct element
- Space: O(N) for the recursive call stack

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
- To avoid duplicate permutations, we need to skip the current element if it is the same as the previous one and the previous one has not been visited.
- We can use a recursive function to generate all permutations of the input array.
- Sorting the input array is necessary to handle duplicate elements correctly.