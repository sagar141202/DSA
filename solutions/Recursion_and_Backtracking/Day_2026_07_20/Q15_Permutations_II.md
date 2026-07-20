# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input collection is not sorted, and the output should not contain duplicate permutations. For example, given the input [1,1,2], the output should be [[1,1,2], [1,2,1], [2,1,1]].

## Approach
The approach to solve this problem is to use backtracking and recursion. We will generate all permutations and skip the duplicates by sorting the input array and skipping the same elements.

## Complexity
- Time: O(N! / (K1! * K2! * ... * Km!)) where N is the total number of elements, and K1, K2, ..., Km are the counts of each duplicate element.
- Space: O(N) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, vector<bool>& used, vector<int>& path, vector<vector<int>>& res) {
    if (path.size() == nums.size()) {
        res.push_back(path);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) {
            continue;
        }
        used[i] = true;
        path.push_back(nums[i]);
        backtrack(nums, used, path, res);
        path.pop_back();
        used[i] = false;
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<bool> used(nums.size(), false);
    vector<vector<int>> res;
    vector<int> path;
    backtrack(nums, used, path, res);
    return res;
}
```

## Test Cases
```
Input: [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]
Input: [2,1,1]
Output: [[1,1,2], [1,2,1], [2,1,1]]
```

## Key Takeaways
- Use backtracking and recursion to generate all permutations.
- Skip duplicates by sorting the input array and checking for same elements.
- Use a boolean array to track the used elements.