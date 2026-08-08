# Subsets

## Problem Statement
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. For example, if `nums = [1, 2, 3]`, the output should be `[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]`. The input array is guaranteed to be non-empty and contain between 1 and 10 elements.

## Approach
The problem can be solved using recursion and backtracking. The idea is to generate all possible subsets by adding each element to the current subset or not. This approach ensures that all possible subsets are generated. The base case for the recursion is when the current index is equal to the size of the input array.

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
    
    void backtrack(vector<vector<int>>& result, vector<int>& current, vector<int>& nums, int index) {
        result.push_back(current);
        for (int i = index; i < nums.size(); i++) {
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
    for (const auto& subset : subsets) {
        cout << "{";
        for (int i = 0; i < subset.size(); i++) {
            cout << subset[i];
            if (i < subset.size() - 1) {
                cout << ", ";
            }
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
- The power set of a set is the set of all possible subsets, including the empty set and the set itself.
- Recursion and backtracking can be used to generate all possible subsets of a set.
- The time complexity of this solution is O(2^n) because there are 2^n possible subsets of a set with n elements.