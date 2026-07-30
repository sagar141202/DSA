# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given the array `[1, 2, 2]`, the subsets are `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]`. The input array is not null, and the size of the array is not more than 100.

## Approach
This problem can be solved using recursion and backtracking. The idea is to generate all subsets and then remove duplicates. We will use a sorting step to ensure that duplicate subsets are adjacent to each other.

## Complexity
- Time: O(2^n * n) where n is the size of the input array, because in the worst case, we are generating all subsets and then sorting them.
- Space: O(2^n * n) for storing the result.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        sort(nums.begin(), nums.end()); // sort to handle duplicates
        backtrack(result, current, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current);
        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i-1]) continue; // skip duplicates
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
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
[
  [],
  [1],
  [1, 2],
  [1, 2, 2],
  [2],
  [2, 2]
]
```

## Key Takeaways
- Use recursion and backtracking to generate all subsets.
- Sort the input array to handle duplicates.
- Skip duplicates in the backtracking step to avoid duplicate subsets.