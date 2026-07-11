# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input is a list of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input list. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The input list can contain duplicates, and the output should not contain any duplicate permutations.

## Approach
The algorithm uses backtracking to generate all permutations of the input list, skipping duplicate permutations by sorting the input list and only exploring branches where the current number is different from the previous one. This approach ensures that all unique permutations are generated without duplicates.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the total number of elements and k1, k2, ..., kn are the counts of each distinct element
- Space: O(N) for the recursion stack and the output list

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
    vector<int> path;
    vector<vector<int>> res;
    backtrack(nums, used, path, res);
    return res;
}
```

## Test Cases
```
Input: [1, 1, 2]
Output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
Input: [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

## Key Takeaways
- Use backtracking to generate all permutations of the input list.
- Sort the input list and skip duplicate branches to avoid duplicate permutations.
- Use a recursion stack and a boolean array to keep track of used numbers.