# Subsets

## Problem Statement
Given a set of distinct integers, nums, return all possible subsets (the power set). The solution set must not contain duplicate subsets. The subsets can be in any order, and the problem has the following constraints: 1 <= nums.length <= 20, and -10^9 <= nums[i] <= 10^9. For example, if the input is [1, 2, 3], the output should be [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].

## Approach
The approach to solve this problem is to use recursion and backtracking. We start with an empty subset and then for each number in the set, we either include it in the subset or not. This way, we generate all possible subsets. The key idea is to use a recursive function to explore all possibilities.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        backtrack(result, current, nums, 0);
        return result;
    }
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int start) {
        result.push_back(current);
        for (int i = start; i < nums.size(); i++) {
            current.push_back(nums[i]);
            backtrack(result, current, nums, i + 1);
            current.pop_back();
        }
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> subsets = solution.subsets(nums);
    for (auto subset : subsets) {
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
Input: [1, 2, 3]
Output: 
[] 
[1] 
[1, 2] 
[1, 2, 3] 
[1, 3] 
[2] 
[2, 3] 
[3]
```

## Key Takeaways
- The problem can be solved using recursion and backtracking by exploring all possible subsets.
- The time complexity is O(2^n) because we are generating all possible subsets of the input set.
- The space complexity is also O(2^n) because we need to store all the subsets in the result.