# Subsets

## Problem Statement
Given a set of distinct integers, return all possible subsets. The solution should be implemented using recursion and backtracking. For example, given the set [1, 2, 3], the output should be [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]. The input set will have a maximum size of 20 and all elements are distinct.

## Approach
The approach involves using recursion to generate all subsets by either including or excluding the current element. This is achieved through backtracking, where we explore all possible branches of the recursion tree.

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
        cout << "{";
        for (int i = 0; i < subset.size(); i++) {
            cout << subset[i];
            if (i < subset.size() - 1) cout << ", ";
        }
        cout << "}" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3]
Output: 
{}
{1}
{1, 2}
{1, 2, 3}
{1, 3}
{2}
{2, 3}
{3}
```

## Key Takeaways
- Use recursion and backtracking to generate all subsets of a given set.
- The time complexity is exponential due to the nature of the problem, where each element can be either included or excluded from a subset.
- The space complexity is also exponential, as we need to store all generated subsets in memory.