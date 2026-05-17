# Subsets

## Problem Statement
Given a set of distinct integers, nums, return all possible subsets (the power set). The solution set must not contain duplicate subsets. It is guaranteed that 0 <= nums.length <= 20. For example, if nums = [1, 2, 3], a solution is [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].

## Approach
The problem can be solved using recursion and backtracking, where each number in the set is either included or excluded from the current subset. The base case is when all numbers have been processed. The algorithm explores all possible combinations of including or excluding each number.

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
- Recursion and backtracking can be used to generate all possible subsets of a given set of distinct integers.
- The time complexity is O(2^n) due to the exploration of all possible combinations, where n is the number of integers in the set.
- The space complexity is also O(2^n) to store all generated subsets.