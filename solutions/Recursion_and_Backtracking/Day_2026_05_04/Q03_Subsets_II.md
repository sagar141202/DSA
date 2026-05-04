# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given the set [1, 2, 2], the subsets are [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]].

## Approach
The problem can be solved using recursion and backtracking. We will sort the input array first and then use a recursive function to generate all subsets. To avoid duplicate subsets, we will skip the current element if it is the same as the previous one.

## Complexity
- Time: O(2^n * n) where n is the number of elements in the input array, as in the worst case, we have to generate all subsets and copy them to the result.
- Space: O(n) for the recursion stack, and O(2^n * n) for storing the result.

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
            // skip the current element if it is the same as the previous one
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
[] 
[1] 
[1, 2] 
[1, 2, 2] 
[2] 
[2, 2]
```

## Key Takeaways
- Sort the input array first to handle duplicate elements.
- Use recursion and backtracking to generate all subsets.
- Skip the current element if it is the same as the previous one to avoid duplicate subsets.