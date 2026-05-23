# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input array may contain duplicate integers. For example, given the array `[1, 1, 2]`, some permutations of it are `[1, 1, 2]`, `[1, 2, 1]`, and `[2, 1, 1]`. However, only `[1, 1, 2]`, and `[2, 1, 1]` should be returned as the duplicates are considered the same.

## Approach
The algorithm uses backtracking to generate all permutations of the input array, skipping duplicates to ensure uniqueness. It sorts the array to group duplicates together, making it easier to skip them. The function recursively generates permutations by selecting each element in the array and removing it from the current permutation.

## Complexity
- Time: O(N! / (k1! * k2! * ... * km!)) where N is the total number of elements and k1, k2, ..., km are the counts of each distinct element
- Space: O(N) for storing the recursion stack

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
        used[i] = false;
        path.pop_back();
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> res;
    vector<bool> used(nums.size(), false);
    vector<int> path;
    sort(nums.begin(), nums.end());
    backtrack(nums, used, path, res);
    return res;
}

int main() {
    vector<int> nums = {1, 1, 2};
    vector<vector<int>> result = permuteUnique(nums);
    for (auto& vec : result) {
        for (auto& num : vec) {
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
Output: 
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
```

## Key Takeaways
- To handle duplicates, we sort the array and skip the duplicates by checking if the current element is the same as the previous one and if the previous one has not been used.
- The time complexity is reduced by avoiding duplicate permutations.
- The space complexity is determined by the recursion stack, which can go up to the length of the input array.