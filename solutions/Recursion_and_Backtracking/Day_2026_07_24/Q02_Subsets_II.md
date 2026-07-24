# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, given the array `[1, 2, 2]`, the subsets are `[], [1], [1, 2], [1, 2, 2], [2], [2, 2]`. However, since `[2]` and `[2, 2]` would both appear in the answer if we don't handle duplicates, and `[2]` should only appear once in the result.

## Approach
This problem can be solved using recursion and backtracking, where we generate all subsets and skip duplicates by sorting the input array and only considering each number if it's different from the previous one. The key idea is to use a recursive function to generate subsets and handle duplicates by checking if the current number is the same as the previous one.

## Complexity
- Time: O(2^n * n) where n is the number of elements in the array, since we generate all subsets (2^n) and for each subset, we might spend n time to copy it to the result.
- Space: O(n) for the recursion stack and to store the current subset being generated.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(int start, vector<int>& nums, vector<int>& path, vector<vector<int>>& result) {
    result.push_back(path);
    for (int i = start; i < nums.size(); i++) {
        // Skip duplicates
        if (i > start && nums[i] == nums[i - 1]) continue;
        path.push_back(nums[i]);
        backtrack(i + 1, nums, path, result);
        path.pop_back();
    }
}

vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> path;
    sort(nums.begin(), nums.end());
    backtrack(0, nums, path, result);
    return result;
}

int main() {
    vector<int> nums = {1, 2, 2};
    vector<vector<int>> result = subsetsWithDup(nums);
    for (auto& subset : result) {
        for (auto& num : subset) {
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
- Use recursion and backtracking to generate all subsets of the given array.
- To avoid duplicate subsets, sort the input array and skip duplicates by checking if the current number is the same as the previous one.
- The time complexity is O(2^n * n) and the space complexity is O(n) due to the recursion stack and the space needed to store the current subset.