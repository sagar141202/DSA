# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, and return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is `[1, 2, 2]`, the output will be `[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]`. The integers in the input array may have duplicates, but the output should not have duplicate subsets.

## Approach
The problem can be solved using recursion and backtracking. The idea is to generate all possible subsets and then remove duplicates by sorting the input array and skipping duplicate elements during the recursion. The base case for the recursion is an empty subset.

## Complexity
- Time: O(2^n * n) where n is the number of elements in the input array, due to generating all subsets and sorting them.
- Space: O(2^n * n) for storing the result.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> path;
        sort(nums.begin(), nums.end());
        backtrack(result, path, nums, 0);
        return result;
    }

    void backtrack(vector<vector<int>>& result, vector<int>& path, vector<int>& nums, int start) {
        result.push_back(path);
        for (int i = start; i < nums.size(); i++) {
            // Skip duplicates
            if (i > start && nums[i] == nums[i - 1]) continue;
            path.push_back(nums[i]);
            backtrack(result, path, nums, i + 1);
            path.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 2};
    vector<vector<int>> result = solution.subsetsWithDup(nums);
    // Print the result
    for (auto subset : result) {
        for (auto num : subset) {
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
[
  [],
  [1],
  [1,2],
  [1,2,2],
  [2],
  [2,2]
]
```

## Key Takeaways
- Use recursion and backtracking to generate all subsets of the input array.
- Sort the input array to handle duplicates and skip them during the recursion.
- The result will contain all unique subsets of the input array.