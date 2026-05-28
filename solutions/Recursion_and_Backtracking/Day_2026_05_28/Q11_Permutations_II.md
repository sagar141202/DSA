# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all unique permutations. The input is a list of integers, and the output is a list of lists, where each sublist is a unique permutation of the input list. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The input list can contain duplicate elements, and the output should not contain duplicate permutations.

## Approach
The approach to solve this problem is to use backtracking and recursion to generate all permutations of the input list, while avoiding duplicate permutations by sorting the input list and skipping duplicate elements. This ensures that each permutation is unique and that the output does not contain duplicates.

## Complexity
- Time: O(N! / (k1! * k2! * ... * kn!)) where N is the length of the input list and k1, k2, ..., kn are the frequencies of each element in the list
- Space: O(N) for the recursion stack

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
    vector<vector<int>> res;
    vector<bool> used(nums.size(), false);
    vector<int> path;
    backtrack(nums, used, path, res);
    return res;
}

int main() {
    vector<int> nums = {1, 1, 2};
    vector<vector<int>> res = permuteUnique(nums);
    for (auto& perm : res) {
        for (auto& num : perm) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
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
- To avoid duplicate permutations, sort the input list and skip duplicate elements during the backtracking process.
- Use a boolean array to keep track of used elements to avoid duplicates.
- The time complexity of this solution is O(N! / (k1! * k2! * ... * kn!)) due to the skipping of duplicate elements.