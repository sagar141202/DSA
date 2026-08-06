# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given the set `[1, 2, 2]`, the subsets are `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The integers in the subset can be in any order, and the subset itself can be in any order in the output.

## Approach
This problem can be solved using recursion and backtracking, where we generate all subsets and skip duplicates. We sort the input array to group duplicates together, making it easier to identify and skip duplicate subsets. The algorithm explores all possible combinations of the input array elements.

## Complexity
- Time: O(2^n * n) where n is the number of elements in the input array, as in the worst case, we generate all subsets and each subset can contain up to n elements.
- Space: O(2^n * n) for storing the result, as in the worst case, the number of subsets is 2^n and each subset can contain up to n elements.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(int start, vector<int>& nums, vector<int>& path, vector<vector<int>>& result) {
    result.push_back(path);
    for (int i = start; i < nums.size(); ++i) {
        // Skip duplicates to avoid duplicate subsets
        if (i > start && nums[i] == nums[i - 1]) continue;
        path.push_back(nums[i]);
        backtrack(i + 1, nums, path, result);
        path.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> path;
    sort(nums.begin(), nums.end()); // Sort to group duplicates
    backtrack(0, nums, path, result);
    return result;
}

int main() {
    vector<int> nums = {1, 2, 2};
    vector<vector<int>> result = subsetsWithDup(nums);
    for (const auto& subset : result) {
        for (const auto& num : subset) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 2]
Output: 
[ ]
[ 1 ]
[ 1 2 ]
[ 1 2 2 ]
[ 2 ]
[ 2 2 ]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible subsets of a given set.
- Sorting the input array helps in skipping duplicate subsets by grouping duplicate elements together.
- The `backtrack` function is a crucial component in generating all subsets, and it uses a `start` index to ensure that each element is considered in the subset generation process.