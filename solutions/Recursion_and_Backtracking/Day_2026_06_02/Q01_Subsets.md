# Subsets

## Problem Statement
Given a set of distinct integers, nums, return all possible subsets (the power set). The solution set must not contain duplicate subsets. The problem has the following constraints: 1 <= nums.length <= 20, and the elements in nums are between -10^9 and 10^9. For example, if the input is [1, 2, 3], the output will be [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]].

## Approach
The problem can be solved using recursion and backtracking by generating all possible subsets. This approach involves adding or not adding each element in the set to the current subset. The recursion tree will have two branches for each element: one where the element is included in the subset and another where it is not.

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
    vector<vector<int>> result = solution.subsets(nums);
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
- The problem is a classic example of using recursion and backtracking to generate all possible subsets of a given set.
- The time complexity is exponential due to the recursive nature of the solution, and the space complexity is also exponential because we are storing all possible subsets in the result.