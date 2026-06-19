# Subsets II

## Problem Statement
Given a collection of integers that might contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if the input is [1, 2, 2], the output will be [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]. The integers in the input array may have duplicates, and the integers are not guaranteed to be in any specific order.

## Approach
The approach involves using recursion and backtracking to generate all possible subsets. We will sort the input array to handle duplicates and ensure that duplicate subsets are not generated. The algorithm will skip duplicate elements during the recursion process.

## Complexity
- Time: O(2^n * n)
- Space: O(n)

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
        backtrack(result, current, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current); // add the current subset to the result
        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i-1]) continue; // skip duplicates
            current.push_back(nums[i]); // add the current element to the subset
            backtrack(result, current, nums, i + 1); // recurse
            current.pop_back(); // backtrack
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
- Sorting the input array helps in handling duplicates and avoiding duplicate subsets.
- Using a recursive approach with backtracking allows us to generate all possible subsets efficiently.
- Skipping duplicate elements during the recursion process ensures that duplicate subsets are not generated.