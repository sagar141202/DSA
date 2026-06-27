# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given the array `[1, 2, 2]`, the subsets are `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]` and the output should be `[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]` without any duplicates. The array elements are not guaranteed to be sorted, and the output does not need to be in a specific order.

## Approach
The problem can be solved using recursion and backtracking, where we generate all possible subsets and skip duplicates by sorting the input array and skipping the same elements. We will use a helper function to generate the subsets recursively.

## Complexity
- Time: O(2^n * n) where n is the number of elements in the array
- Space: O(n) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        sort(nums.begin(), nums.end()); // sort the array to handle duplicates
        backtrack(nums, 0, current, result);
        return result;
    }
    
    void backtrack(vector<int>& nums, int start, vector<int>& current, vector<vector<int>>& result) {
        result.push_back(current);
        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i - 1]) continue; // skip duplicates
            current.push_back(nums[i]);
            backtrack(nums, i + 1, current, result);
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
[] 
[1] 
[1, 2] 
[1, 2, 2] 
[2] 
[2, 2]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible subsets.
- Sort the input array to handle duplicates and skip the same elements.
- Use a helper function to generate the subsets recursively and avoid code duplication.